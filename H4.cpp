/*
 * heuristic_v4.cpp
 * ================
 * Utility-Aware Energy-Constrained Real-Time Scheduling
 * Preemptive EDF | Per-job f_max baseline | Per-job optional segments
 *
 * Compile:
 *   g++ -O2 -std=c++17 -o heuristic_v4 heuristic_v4.cpp
 *
 * Run:
 *   ./heuristic_v4 testcase.txt
 *
 * Testcase file format (testcase.txt):
 * ─────────────────────────────────────
 *   <num_processors>
 *   <num_freqs>  <f1> <f2> ... <fN>        (one line per processor)
 *   <budget B>
 *   <num_tasks>
 *   <id> <period> <e_m> <u_i> <num_opt> <e_o1> <e_o2> ...  (one line per task)
 *
 * Assumptions
 * ───────────
 * A1. Preemptive EDF scheduling.  Feasibility is verified via the Demand
 *     Bound Function (DBF); no explicit timeline is constructed.
 * A2. Per-job frequency and optional-segment count.  Different activations
 *     of the same task may have different (f, k) assignments.
 * A3. Phase 1 assigns f_max to every job.  This minimises execution time,
 *     maximising utilisation headroom for optional segments in Phase 2.
 * A4. Phase 2 adds optional segments greedily, scored by
 *         ΔUtility / (λ·ΔE + (1-λ)·Δt),  λ = E_total / B.
 *     Three move types: INC_K, INC_F_INC_K, DEC_F_INC_K.
 * A5. Homogeneous processors (same frequency set).
 * A6. WFDU (Worst-Fit Decreasing Utilisation) partitions tasks.
 *     Mandatory utilisation u = e_m / p used as proxy.
 * A7. Energy model: E = α·(e_nom/f) + β·f²·e_nom  (paper Eq.2).
 * A8. DBF check uses implicit-deadline condition: dbf(0,t) ≤ (1-ε)·t
 *     at all deadline instants t.
 * A9. Pointers into job vectors (used in Phase 2 for best_move.job)
 *     are stable because no vector reallocation occurs during Phase 2.
 */

#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <climits>

// ── Energy model constants ────────────────────────────────────────────────────
static const double ALPHA   = 1.0;
static const double BETA    = 1.0;
static const double EPSILON = 1e-4;   // DBF safety margin

// ── ANSI colours (disable on Windows if needed) ───────────────────────────────
static const std::string GREEN  = "\033[92m";
static const std::string RED    = "\033[91m";
static const std::string YELLOW = "\033[93m";
static const std::string RESET  = "\033[0m";


// ══════════════════════════════════════════════════════════════════════════════
//  Data structures
// ══════════════════════════════════════════════════════════════════════════════

struct Task {
    int    id;
    int    p_i;
    double e_m;
    double u_i;
    std::vector<double> e_o_k;   // optional segment exec times at f_max
};

struct Processor {
    int id;
    std::vector<double> frequencies;   // sorted ascending
};

// One job = one activation of a task.
// f and k are the only mutable fields after creation.
struct Job {
    int    task_id;
    int    task_idx;    // index into global tasks vector
    int    job_idx;     // j-th activation (0-based)
    double release;     // j * p_i
    double deadline;    // (j+1) * p_i
    double period;      // p_i
    double e_m;
    double u_i;
    std::vector<double> e_o_list;   // same as task's e_o_k

    double f;           // ← assigned frequency (mutable)
    int    k;           // ← optional segments executed (mutable)

    // ── derived quantities ────────────────────────────────────────────────────
    double nom() const {
        double s = e_m;
        for (int q = 0; q < k; ++q) s += e_o_list[q];
        return s;
    }
    double nom_at(int kk) const {
        double s = e_m;
        for (int q = 0; q < kk; ++q) s += e_o_list[q];
        return s;
    }
    double exec_t()     const { return nom() / f; }
    double energy_val() const {
        double n = nom();
        return ALPHA * (n / f) + BETA * (f * f) * n;
    }
    double utility()    const {
        if (k == 0) return 0.0;
        double s = 0.0;
        for (int q = 0; q < k; ++q) s += e_o_list[q];
        return u_i * s;
    }
};


// ══════════════════════════════════════════════════════════════════════════════
//  Math / model helpers
// ══════════════════════════════════════════════════════════════════════════════

static long long gcd(long long a, long long b) {
    while (b) { a %= b; std::swap(a, b); }
    return a;
}
static long long lcm(long long a, long long b) {
    return (a / gcd(a, b)) * b;
}

static long long hyperperiod(const std::vector<Task>& tasks) {
    long long h = 1;
    for (auto& t : tasks) h = lcm(h, (long long)t.p_i);
    return h;
}

// nominal execution time at f_max for mandatory + first k optional segs
static double nom_fn(double e_m, const std::vector<double>& eo, int k) {
    double s = e_m;
    for (int q = 0; q < k; ++q) s += eo[q];
    return s;
}

// paper Eq.(2): E = α·(e_nom/f) + β·f²·e_nom
static double energy_fn(double nom, double f) {
    return ALPHA * (nom / f) + BETA * (f * f) * nom;
}

static double exec_fn(double nom, double f) {
    return nom / f;
}


// ══════════════════════════════════════════════════════════════════════════════
//  Job generation
// ══════════════════════════════════════════════════════════════════════════════

static std::vector<Job> make_jobs(const Task& task, int task_idx,
                                   long long H, double f_init) {
    std::vector<Job> jobs;
    int p  = task.p_i;
    int nj = (int)(H / p);
    jobs.reserve(nj);
    for (int j = 0; j < nj; ++j) {
        Job jb;
        jb.task_id  = task.id;
        jb.task_idx = task_idx;
        jb.job_idx  = j;
        jb.release  = (double)(j * p);
        jb.deadline = (double)((j + 1) * p);
        jb.period   = (double)p;
        jb.e_m      = task.e_m;
        jb.u_i      = task.u_i;
        jb.e_o_list = task.e_o_k;
        jb.f        = f_init;
        jb.k        = 0;
        jobs.push_back(std::move(jb));
    }
    return jobs;
}


// ══════════════════════════════════════════════════════════════════════════════
//  DBF helpers
// ══════════════════════════════════════════════════════════════════════════════

// Returns sorted list of all distinct deadline instants in (0, H].
static std::vector<double> make_checkpoints(const std::vector<Job>& jobs,
                                             long long H) {
    std::set<double> pts;
    for (auto& j : jobs)
        if (j.deadline > 0.0 && j.deadline <= (double)H)
            pts.insert(j.deadline);
    return {pts.begin(), pts.end()};
}

// Total execution time demanded by jobs with deadline <= t.
static double dbf_at(double t, const std::vector<Job>& jobs) {
    double s = 0.0;
    for (auto& j : jobs)
        if (j.deadline <= t + 1e-12)
            s += j.exec_t();
    return s;
}

// Returns true iff DBF check passes for all checkpoints >= from_deadline.
// Incremental optimisation: a change to a job with deadline d can only
// affect check points t >= d.
static bool dbf_feasible(const std::vector<Job>& jobs,
                          const std::vector<double>& cps,
                          double from_deadline = 0.0) {
    for (double t : cps) {
        if (t < from_deadline - 1e-9) continue;
        if (dbf_at(t, jobs) > (1.0 - EPSILON) * t)
            return false;
    }
    return true;
}


// ══════════════════════════════════════════════════════════════════════════════
//  WFDU Partition
// ══════════════════════════════════════════════════════════════════════════════

static bool partition_WFDU(const std::vector<Task>&      tasks,
                            const std::vector<Processor>& processors,
                            long long                      H,
                            std::vector<std::vector<int>>& tasks_by_proc,
                            std::vector<std::vector<Job>>& jobs_by_proc) {
    int num_proc = (int)processors.size();
    tasks_by_proc.assign(num_proc, {});
    jobs_by_proc .assign(num_proc, {});
    std::vector<double> proc_util(num_proc, 0.0);

    // Sort task indices by mandatory util descending
    std::vector<int> order((int)tasks.size());
    std::iota(order.begin(), order.end(), 0);
    std::sort(order.begin(), order.end(), [&](int a, int b) {
        return (tasks[a].e_m / tasks[a].p_i) > (tasks[b].e_m / tasks[b].p_i);
    });

    std::cout << "WFDU partitioning ...\n";

    for (int ti : order) {
        const Task& task = tasks[ti];
        double u = task.e_m / (double)task.p_i;

        if (u >= 1.0 - 1e-9) {
            std::cout << RED << "  Task " << task.id << " u=" << u
                      << " >= 1.0 - unschedulable." << RESET << "\n";
            return false;
        }

        // Worst-fit: least-loaded processor whose resulting util < 1
        int    best_pid = -1;
        double best_u   = std::numeric_limits<double>::infinity();
        for (int pid = 0; pid < num_proc; ++pid) {
            double new_u = proc_util[pid] + u;
            if (new_u < 1.0 - 1e-9 && proc_util[pid] < best_u) {
                best_u   = proc_util[pid];
                best_pid = pid;
            }
        }

        if (best_pid == -1) {
            std::cout << RED << "  Task " << task.id
                      << " (u=" << u << ") cannot be placed." << RESET << "\n";
            return false;
        }

        proc_util[best_pid] += u;
        tasks_by_proc[best_pid].push_back(ti);
    }

    // Build all jobs at f_max
    for (int pid = 0; pid < num_proc; ++pid) {
        double f_max = processors[pid].frequencies.back();  // already sorted asc
        for (int ti : tasks_by_proc[pid]) {
            auto jbs = make_jobs(tasks[ti], ti, H, f_max);
            for (auto& j : jbs)
                jobs_by_proc[pid].push_back(std::move(j));
        }
    }

    // DBF check at f_max, k=0 per processor
    for (int pid = 0; pid < num_proc; ++pid) {
        auto cps = make_checkpoints(jobs_by_proc[pid], H);
        if (!dbf_feasible(jobs_by_proc[pid], cps)) {
            std::cout << RED << "  DBF failed on P" << pid
                      << " at f_max - partition infeasible." << RESET << "\n";
            return false;
        }
    }

    // Print summary
    std::cout << std::fixed << std::setprecision(4);
    for (int pid = 0; pid < num_proc; ++pid) {
        double u = 0.0;
        for (int ti : tasks_by_proc[pid]) u += tasks[ti].e_m / tasks[ti].p_i;
        std::cout << "  P" << pid << "  u_mand=" << u << "  tasks=[";
        for (int i = 0; i < (int)tasks_by_proc[pid].size(); ++i) {
            if (i) std::cout << ", ";
            std::cout << tasks[tasks_by_proc[pid][i]].id;
        }
        std::cout << "]\n";
    }
    std::cout << GREEN << "  Partition + DBF OK" << RESET << "\n";
    return true;
}


// ══════════════════════════════════════════════════════════════════════════════
//  Phase 1 — Assign f_max to all jobs
// ══════════════════════════════════════════════════════════════════════════════

static double phase1(std::vector<std::vector<Job>>& jobs_by_proc,
                     const std::vector<Processor>&  processors) {
    std::cout << "\nPhase 1 - assigning f_max to all jobs ...\n";
    double total_energy = 0.0;

    for (int pid = 0; pid < (int)jobs_by_proc.size(); ++pid) {
        double f_max = processors[pid].frequencies.back();
        for (auto& job : jobs_by_proc[pid]) {
            job.f = f_max;
            job.k = 0;
            total_energy += job.energy_val();
        }
    }

    std::cout << std::fixed << std::setprecision(4);
    std::cout << GREEN << "  Phase 1 OK  -  energy used: "
              << total_energy << RESET << "\n";
    return total_energy;
}


// ══════════════════════════════════════════════════════════════════════════════
//  Phase 2 — Bang-for-buck greedy upgrade
// ══════════════════════════════════════════════════════════════════════════════

static double compute_score(double d_util, double d_e,
                             double d_t,   double lam) {
    if (d_util <= 1e-8) return -1.0;

    double cost_e = lam * d_e;
    double cost_t = (1.0 - lam) * d_t;
    double denom  = cost_e + cost_t;

    if (denom <= 1e-12) return std::numeric_limits<double>::infinity();
    return d_util / denom;
}

// Holds enough info to identify and commit the winning move.
// job is a raw pointer into jobs_by_proc — safe because we never
// resize or reorder those vectors during Phase 2 (A9).
struct BestMove {
    Job*        job    = nullptr;
    int         pid    = -1;
    double      f_new  = 0.0;
    int         k_new  = 0;
    double      d_e    = 0.0;
    double      d_util = 0.0;
    std::string label;
};

static double phase2(std::vector<std::vector<Job>>& jobs_by_proc,
                     const std::vector<Processor>&  processors,
                     long long H, double B, double total_energy) {
    std::cout << "\nPhase 2 - bang-for-buck greedy upgrade ...\n";

    // Pre-compute checkpoints per processor (reused every iteration)
    std::vector<std::vector<double>> cps_by_proc;
    for (auto& jobs : jobs_by_proc)
        cps_by_proc.push_back(make_checkpoints(jobs, H));

    // Sorted frequency lists per processor (already sorted from reader)
    std::vector<std::vector<double>> freqs_by_proc;
    for (auto& p : processors)
        freqs_by_proc.push_back(p.frequencies);   // ascending

    // Upper bound on iterations
    int MAX_ITER = 1;
    for (auto& jobs : jobs_by_proc)
        for (auto& j : jobs)
            MAX_ITER += (int)j.e_o_list.size() * 3;

    int applied = 0;
    bool converged = false;

    for (int iter = 0; iter < MAX_ITER; ++iter) {
        double   lam        = total_energy / B;
        BestMove best;
        double   best_score = -1.0;

        for (int pid = 0; pid < (int)jobs_by_proc.size(); ++pid) {
            std::vector<Job>& jobs  = jobs_by_proc[pid];
            std::vector<double>& freqs = freqs_by_proc[pid];
            std::vector<double>& cps   = cps_by_proc[pid];

            for (Job& job : jobs) {
                int cur_k = job.k;
                int max_k = (int)job.e_o_list.size();
                if (cur_k >= max_k) continue;

                // Locate current frequency in sorted list
                // Use lower_bound for O(log Nf) instead of linear search
                int f_idx = (int)(std::lower_bound(freqs.begin(), freqs.end(),
                                                    job.f - 1e-12) - freqs.begin());

                // Three candidate moves
                struct Candidate { std::string label; double f_new; };
                std::vector<Candidate> candidates;
                candidates.push_back({"INC_K",       job.f});
                if (f_idx + 1 < (int)freqs.size())
                    candidates.push_back({"INC_F_INC_K", freqs[f_idx + 1]});
                if (f_idx - 1 >= 0)
                    candidates.push_back({"DEC_F_INC_K", freqs[f_idx - 1]});

                double nom_old = nom_fn(job.e_m, job.e_o_list, cur_k);
                double nom_new = nom_fn(job.e_m, job.e_o_list, cur_k + 1);
                double e_old   = energy_fn(nom_old, job.f);
                double d_util  = job.u_i * job.e_o_list[cur_k];

                for (int ci = 0; ci < (int)candidates.size(); ++ci) {
                    const std::string& move_label = candidates[ci].label;
                    double f_new = candidates[ci].f_new;
                    double e_new = energy_fn(nom_new, f_new);
                    double d_e   = e_new - e_old;
                    double d_t   = exec_fn(nom_new, f_new)
                                 - exec_fn(nom_old, job.f);

                    // Gate 1: global energy budget
                    if (total_energy + d_e > B + 1e-9) continue;

                    // Gate 2: tentative apply → incremental DBF → revert
                    double old_f = job.f;
                    int    old_k = job.k;
                    job.f = f_new;
                    job.k = cur_k + 1;
                    bool feasible = dbf_feasible(jobs, cps, job.deadline);
                    job.f = old_f;   // always revert
                    job.k = old_k;

                    if (!feasible) continue;

                    double score = compute_score(d_util, d_e, d_t, lam);
                    if (score < 0.0) continue;

                    // Three-level tie-break:
                    // 1. Higher score  2. Higher d_util  3. Lower d_e
                    bool better = (score > best_score + 1e-12);
                    if (!better && std::fabs(score - best_score) < 1e-12) {
                        if (best.job == nullptr) {
                            better = true;
                        } else if (d_util > best.d_util + 1e-12) {
                            better = true;
                        } else if (std::fabs(d_util - best.d_util) < 1e-12
                                   && d_e < best.d_e - 1e-12) {
                            better = true;
                        }
                    }

                    if (better) {
                        best_score  = score;
                        best.job    = &job;
                        best.pid    = pid;
                        best.f_new  = f_new;
                        best.k_new  = cur_k + 1;
                        best.d_e    = d_e;
                        best.d_util = d_util;
                        best.label  = move_label;
                    }
                } // end candidates loop
            }
        }

        if (best.job == nullptr) {
            std::cout << "  Converged after " << applied << " upgrade(s).\n";
            converged = true;
            break;
        }

        // Commit the winning move — mutate job in-place
        best.job->f  = best.f_new;
        best.job->k  = best.k_new;
        total_energy += best.d_e;
        ++applied;
    }

    if (!converged)
        std::cout << "  Reached MAX_ITER (" << MAX_ITER
                  << "). Applied " << applied << " upgrade(s).\n";

    return total_energy;
}


// ══════════════════════════════════════════════════════════════════════════════
//  Verification
// ══════════════════════════════════════════════════════════════════════════════

static bool verify(const std::vector<std::vector<Job>>& jobs_by_proc,
                   long long H, double B) {
    bool   ok           = true;
    double total_energy = 0.0;

    for (int pid = 0; pid < (int)jobs_by_proc.size(); ++pid) {
        auto& jobs = jobs_by_proc[pid];
        auto cps   = make_checkpoints(jobs, H);
        for (double t : cps) {
            double d = dbf_at(t, jobs);
            if (d > t + 1e-6) {
                std::cout << RED << "  VERIFY FAIL: P" << pid
                          << " DBF(" << t << ")=" << d << " > " << t
                          << RESET << "\n";
                ok = false;
            }
        }
        for (auto& j : jobs) total_energy += j.energy_val();
    }

    if (total_energy > B + 1e-6) {
        std::cout << std::fixed << std::setprecision(4);
        std::cout << RED << "  VERIFY FAIL: energy " << total_energy
                  << " > B=" << B << RESET << "\n";
        ok = false;
    }

    if (ok)
        std::cout << GREEN << "  Verification passed." << RESET << "\n";
    return ok;
}


// ══════════════════════════════════════════════════════════════════════════════
//  Output
// ══════════════════════════════════════════════════════════════════════════════

static void print_schedule(const std::vector<std::vector<Job>>& jobs_by_proc,
                            double total_energy, double B, long long H) {
    double total_utility = 0.0;
    for (auto& jobs : jobs_by_proc)
        for (auto& j : jobs)
            total_utility += j.utility();

    constexpr int W = 85;
    std::string eq_line(W, '=');
    std::string dash_line(W, '-');

    // Lambda that writes the full block to any ostream
    auto block = [&](std::ostream& out) {
        out << std::fixed << std::setprecision(4);
        out << eq_line << "\n";
        out << "  USRT HEURISTIC v4  -  Preemptive EDF | Per-job f & k\n";
        out << "  WFDU | Phase1: f_max baseline | Phase2: bang-for-buck\n";
        out << eq_line << "\n\n";
        out << "  Total Utility : " << total_utility << "\n";
        out << "  Total Energy  : " << total_energy << " / " << B
            << std::setprecision(1)
            << "  (" << 100.0 * total_energy / B << "% used)\n"
            << std::setprecision(4);
        out << "  Hyper-period  : " << H << "\n";

        // Utilisation summary
        out << "\n  Processor Utilisation Summary\n";
        out << "  " << std::left
            << std::setw(8)  << "Proc"
            << std::setw(12) << "U_mand"
            << std::setw(12) << "U_total"
            << std::setw(10) << "U_used%"
            << std::setw(12) << "Energy"
            << "Utility\n";
        out << "  " << std::string(60, '-') << "\n";

        for (int pid = 0; pid < (int)jobs_by_proc.size(); ++pid) {
            auto& jobs  = jobs_by_proc[pid];
            double u_mand = 0, u_total = 0, p_e = 0, p_u = 0;
            for (auto& j : jobs) {
                u_mand  += j.e_m / j.f;
                u_total += j.exec_t();
                p_e     += j.energy_val();
                p_u     += j.utility();
            }
            u_mand  /= H;
            u_total /= H;
            out << "  P" << std::left << std::setw(7) << pid
                << std::setw(12) << u_mand
                << std::setw(12) << u_total
                << std::setprecision(2) << std::setw(10) << 100.0 * u_total
                << std::setprecision(4)
                << std::setw(12) << p_e
                << p_u << "\n";
        }

        // Per-processor job detail
        for (int pid = 0; pid < (int)jobs_by_proc.size(); ++pid) {
            // Copy and sort by EDF order
            std::vector<Job> jobs = jobs_by_proc[pid];
            std::sort(jobs.begin(), jobs.end(), [](const Job& a, const Job& b) {
                if (a.deadline != b.deadline) return a.deadline < b.deadline;
                return a.release < b.release;
            });

            double p_e = 0, p_u = 0, p_et = 0;
            for (auto& j : jobs) { p_e += j.energy_val(); p_u += j.utility(); p_et += j.exec_t(); }
            double u_total = p_et / H;

            out << "\n" << dash_line << "\n";
            out << "  Processor " << pid
                << "   jobs=" << jobs.size()
                << "   U_total=" << std::setprecision(4) << u_total
                << "   energy=" << p_e
                << "   utility=" << p_u << "\n";
            out << dash_line << "\n";

            // Header row
            out << "  " << std::left
                << std::setw(14) << "Job"
                << std::setw(4)  << "k"
                << std::setw(6)  << "f"
                << std::setw(10) << "ExecTime"
                << std::setw(12) << "Energy"
                << std::setw(10) << "Utility"
                << std::setw(9)  << "Release"
                << "Deadline\n";
            out << "  " << std::string(W - 2, '-') << "\n";

            for (auto& j : jobs) {
                std::string label = "T" + std::to_string(j.task_id)
                                  + ".J" + std::to_string(j.job_idx);
                out << "  " << std::left << std::setw(14) << label
                    << std::setw(4) << j.k
                    << std::setprecision(2) << std::setw(6) << j.f
                    << std::setprecision(4)
                    << std::setw(10) << j.exec_t()
                    << std::setw(12) << j.energy_val()
                    << std::setw(10) << j.utility()
                    << std::setw(9)  << (int)j.release
                    << (int)j.deadline << "\n";
            }

            // Per-task summary within this processor
            out << "\n  Task summary\n";
            std::set<int> tids;
            for (auto& j : jobs) tids.insert(j.task_id);
            for (int tid : tids) {
                double t_e = 0, t_u = 0, t_et = 0;
                int    tk_min = INT_MAX, tk_max = INT_MIN;
                double tf_min = 1e18,   tf_max = -1e18;
                int    cnt   = 0;
                for (auto& j : jobs) {
                    if (j.task_id != tid) continue;
                    ++cnt;
                    t_e   += j.energy_val();
                    t_u   += j.utility();
                    t_et  += j.exec_t();
                    tk_min = std::min(tk_min, j.k);
                    tk_max = std::max(tk_max, j.k);
                    tf_min = std::min(tf_min, j.f);
                    tf_max = std::max(tf_max, j.f);
                }
                out << "    T" << tid
                    << "  jobs=" << cnt
                    << "  k=[" << tk_min << "," << tk_max << "]"
                    << "  f=[" << std::setprecision(2) << tf_min
                    << "," << tf_max << "]"
                    << std::setprecision(4)
                    << "  U=" << t_et / H
                    << "  energy=" << t_e
                    << "  utility=" << t_u << "\n";
            }
        }
        out << "\n" << eq_line << "\n";
    };

    std::cout << "\n";
    block(std::cout);

    std::ofstream fh("output_heuristic_cpp.txt");
    if (fh.is_open()) {
        block(fh);
        std::cout << GREEN << "Schedule also saved to 'output_heuristic_cpp.txt'"
                  << RESET << "\n";
    } else {
        std::cerr << RED << "Warning: could not write output_heuristic_cpp.txt"
                  << RESET << "\n";
    }
}


// ══════════════════════════════════════════════════════════════════════════════
//  Testcase reader
//
//  File format:
//    <num_processors>
//    <num_freqs> <f1> <f2> ... <fN>      (one line per processor)
//    <budget>
//    <num_tasks>
//    <id> <period> <e_m> <u_i> <num_opt> <e_o1> ... <e_oM>  (one line/task)
// ══════════════════════════════════════════════════════════════════════════════

static bool read_testcase(const std::string&       fname,
                           std::vector<Processor>& processors,
                           std::vector<Task>&      tasks,
                           double&                 B) {
    std::ifstream fin(fname);
    if (!fin.is_open()) {
        std::cerr << RED << "Cannot open: " << fname << RESET << "\n";
        return false;
    }

    int num_proc;
    fin >> num_proc;
    processors.resize(num_proc);
    for (int i = 0; i < num_proc; ++i) {
        processors[i].id = i;
        int nf; fin >> nf;
        processors[i].frequencies.resize(nf);
        for (int z = 0; z < nf; ++z) fin >> processors[i].frequencies[z];
        std::sort(processors[i].frequencies.begin(),
                  processors[i].frequencies.end());
    }

    fin >> B;

    int num_tasks;
    fin >> num_tasks;
    tasks.resize(num_tasks);
    for (int i = 0; i < num_tasks; ++i) {
        int num_opt;
        fin >> tasks[i].id >> tasks[i].p_i
            >> tasks[i].e_m >> tasks[i].u_i >> num_opt;
        tasks[i].e_o_k.resize(num_opt);
        for (int k = 0; k < num_opt; ++k) fin >> tasks[i].e_o_k[k];
    }

    if (!fin) {
        std::cerr << RED << "Error reading testcase file." << RESET << "\n";
        return false;
    }
    return true;
}


// ══════════════════════════════════════════════════════════════════════════════
//  Main
// ══════════════════════════════════════════════════════════════════════════════

int main(int argc, char* argv[]) {
    std::string fname = (argc > 1) ? argv[1] : "testcase.txt";

    std::vector<Processor> processors;
    std::vector<Task>      tasks;
    double B = 0.0;

    if (!read_testcase(fname, processors, tasks, B)) return 1;

    long long H = hyperperiod(tasks);
    if (H > 10000)
        std::cout << YELLOW << "Warning: H=" << H
                  << " is large - may be slow." << RESET << "\n";
    std::cout << "Hyper-period H = " << H << "\n\n";

    std::vector<std::vector<int>> tasks_by_proc;
    std::vector<std::vector<Job>> jobs_by_proc;

    if (!partition_WFDU(tasks, processors, H, tasks_by_proc, jobs_by_proc)) {
        std::cout << RED << "Partitioning failed." << RESET << "\n";
        return 1;
    }

    double E = phase1(jobs_by_proc, processors);
    E = phase2(jobs_by_proc, processors, H, B, E);

    std::cout << "\nVerifying schedule ...\n";
    verify(jobs_by_proc, H, B);
    print_schedule(jobs_by_proc, E, B, H);

    return 0;
}