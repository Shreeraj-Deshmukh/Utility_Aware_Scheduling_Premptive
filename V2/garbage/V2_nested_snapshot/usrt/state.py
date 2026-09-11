"""
ScheduleState — incremental DBF tracking with atomic moves.

Used by the ScheduleState-based heuristic (heuristic_v1 solver).
Each move (try_inc_seg, try_dec_seg, try_dec_freq, try_inc_freq) atomically
updates the incremental DBF slack structures and the global energy slack.
"""

from .models import energy_val, e_eff_val


def _e_eff(cum_ik, fz):
    return cum_ik / fz


def _energy(cum_ik, fz):
    from .models import ALPHA, BETA
    return ALPHA * (cum_ik / fz) + BETA * (fz ** 2) * cum_ik


class ScheduleState:
    """
    Holds the complete mutable solution state.

    Per-job decisions:
        freq_idx[(i,j)] — index into freq_set  (current frequency)
        seg_k[(i,j)]    — current segment level (0 = mandatory only)

    Incremental slack structures (updated after every accepted move):
        dbf[x][(t1,t2)]         — current DBF demand in window
        slack_time[x][(t1,t2)]  — (t2-t1) - dbf[x][(t1,t2)]
        slack_energy             — B - total energy consumed
    """

    def __init__(self, tasks, processors, cum, N_seg, N_job,
                 periods, freq_set, job_r, job_d, sps_map, B):
        self.tasks    = tasks
        self.N_tsk    = len(tasks)
        self.N_prc    = len(processors)
        self.freq_set = freq_set
        self.N_frq    = len(freq_set)
        self.cum      = cum
        self.N_seg    = N_seg
        self.N_job    = N_job
        self.periods  = periods
        self.job_r    = job_r
        self.job_d    = job_d
        self.sps_map  = sps_map    # (i,j) → proc_idx
        self.B        = B

        self.proc_jobs = {x: [] for x in range(self.N_prc)}
        for (i, j), x in sps_map.items():
            self.proc_jobs[x].append((i, j))

        self.freq_idx = {(i, j): self.N_frq - 1
                         for i in range(self.N_tsk)
                         for j in range(N_job[i])}
        self.seg_k    = {(i, j): 0
                         for i in range(self.N_tsk)
                         for j in range(N_job[i])}

        self.windows    = {}
        self.dbf        = {}
        self.slack_time = {}
        self._build_windows()
        self._init_dbf()
        self.slack_energy = B - self._total_energy()

    # ── window construction ──────────────────────────────────────────────────

    def _build_windows(self):
        for x in range(self.N_prc):
            jobs = self.proc_jobs[x]
            Ax   = sorted({self.job_r[(i, j)] for (i, j) in jobs})
            Dx   = sorted({self.job_d[(i, j)] for (i, j) in jobs})
            wins = [(t1, t2) for t1 in Ax for t2 in Dx if t1 < t2]
            self.windows[x]    = wins
            self.dbf[x]        = {w: 0.0 for w in wins}
            self.slack_time[x] = {}

    def _init_dbf(self):
        for x in range(self.N_prc):
            for (t1, t2) in self.windows[x]:
                d = sum(
                    _e_eff(self.cum[i][self.seg_k[(i, j)]],
                           self.freq_set[self.freq_idx[(i, j)]])
                    for (i, j) in self.proc_jobs[x]
                    if self.job_r[(i, j)] >= t1 and self.job_d[(i, j)] <= t2
                )
                self.dbf[x][(t1, t2)]        = d
                self.slack_time[x][(t1, t2)] = (t2 - t1) - d

    # ── energy ───────────────────────────────────────────────────────────────

    def _job_energy(self, i, j):
        return _energy(self.cum[i][self.seg_k[(i, j)]],
                       self.freq_set[self.freq_idx[(i, j)]])

    def _total_energy(self):
        return sum(self._job_energy(i, j)
                   for i in range(self.N_tsk)
                   for j in range(self.N_job[i]))

    # ── query helpers ─────────────────────────────────────────────────────────

    def windows_of(self, i, j):
        x = self.sps_map[(i, j)]
        r, d = self.job_r[(i, j)], self.job_d[(i, j)]
        return [(t1, t2) for (t1, t2) in self.windows[x]
                if t1 <= r and t2 >= d]

    def overlapping_jobs(self, i, j):
        x  = self.sps_map[(i, j)]
        r0 = self.job_r[(i, j)]
        d0 = self.job_d[(i, j)]
        return [
            (ii, jj) for (ii, jj) in self.proc_jobs[x]
            if (ii, jj) != (i, j)
            and self.job_r[(ii, jj)] < d0
            and self.job_d[(ii, jj)] > r0
        ]

    def min_slack_in_windows(self, i, j):
        wins = self.windows_of(i, j)
        if not wins:
            return float('inf')
        x = self.sps_map[(i, j)]
        return min(self.slack_time[x][w] for w in wins)

    # ── incremental DBF update ────────────────────────────────────────────────

    def _update_dbf_for_job(self, i, j, old_eeff, new_eeff):
        x     = self.sps_map[(i, j)]
        delta = new_eeff - old_eeff
        for (t1, t2) in self.windows_of(i, j):
            self.dbf[x][(t1, t2)]        += delta
            self.slack_time[x][(t1, t2)] -= delta

    # ── atomic moves ─────────────────────────────────────────────────────────

    def try_inc_seg(self, i, j):
        k_cur = self.seg_k[(i, j)]
        if k_cur >= self.N_seg[i]:
            return False

        z_cur    = self.freq_idx[(i, j)]
        fz       = self.freq_set[z_cur]
        old_cum  = self.cum[i][k_cur]
        new_cum  = self.cum[i][k_cur + 1]
        old_eeff = _e_eff(old_cum, fz)
        new_eeff = _e_eff(new_cum, fz)
        delta_e  = _energy(new_cum, fz) - _energy(old_cum, fz)

        if delta_e > self.slack_energy + 1e-9:
            return False

        x = self.sps_map[(i, j)]
        for (t1, t2) in self.windows_of(i, j):
            if self.slack_time[x][(t1, t2)] - (new_eeff - old_eeff) < -1e-9:
                return False

        self.seg_k[(i, j)] = k_cur + 1
        self._update_dbf_for_job(i, j, old_eeff, new_eeff)
        self.slack_energy -= delta_e
        return True

    def try_dec_seg(self, i, j):
        k_cur = self.seg_k[(i, j)]
        if k_cur == 0:
            return False

        z_cur    = self.freq_idx[(i, j)]
        fz       = self.freq_set[z_cur]
        old_cum  = self.cum[i][k_cur]
        new_cum  = self.cum[i][k_cur - 1]
        old_eeff = _e_eff(old_cum, fz)
        new_eeff = _e_eff(new_cum, fz)
        delta_e  = _energy(new_cum, fz) - _energy(old_cum, fz)

        self.seg_k[(i, j)] = k_cur - 1
        self._update_dbf_for_job(i, j, old_eeff, new_eeff)
        self.slack_energy -= delta_e
        return True

    def try_dec_freq(self, i, j):
        z_cur = self.freq_idx[(i, j)]
        if z_cur == 0:
            return False

        k_cur    = self.seg_k[(i, j)]
        old_fz   = self.freq_set[z_cur]
        new_fz   = self.freq_set[z_cur - 1]
        cum_ik   = self.cum[i][k_cur]
        old_eeff = _e_eff(cum_ik, old_fz)
        new_eeff = _e_eff(cum_ik, new_fz)
        delta_e  = _energy(cum_ik, new_fz) - _energy(cum_ik, old_fz)

        x = self.sps_map[(i, j)]
        for (t1, t2) in self.windows_of(i, j):
            if self.slack_time[x][(t1, t2)] - (new_eeff - old_eeff) < -1e-9:
                return False

        self.freq_idx[(i, j)] = z_cur - 1
        self._update_dbf_for_job(i, j, old_eeff, new_eeff)
        self.slack_energy -= delta_e
        return True

    def try_inc_freq(self, i, j):
        z_cur = self.freq_idx[(i, j)]
        if z_cur >= self.N_frq - 1:
            return False

        k_cur    = self.seg_k[(i, j)]
        old_fz   = self.freq_set[z_cur]
        new_fz   = self.freq_set[z_cur + 1]
        cum_ik   = self.cum[i][k_cur]
        old_eeff = _e_eff(cum_ik, old_fz)
        new_eeff = _e_eff(cum_ik, new_fz)
        delta_e  = _energy(cum_ik, new_fz) - _energy(cum_ik, old_fz)

        if delta_e > self.slack_energy + 1e-9:
            return False

        self.freq_idx[(i, j)] = z_cur + 1
        self._update_dbf_for_job(i, j, old_eeff, new_eeff)
        self.slack_energy -= delta_e
        return True
