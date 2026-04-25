import math
from testcase import testcase

def solve_usrt_enhanced_heuristic():
    # 1. LOAD DATA & SYSTEM SETUP
    processors, tasks, B_BUDGET = testcase()
    alpha_c, beta_c = 1.0, 1.0 # Energy constants [cite: 99]
    alpha_w, beta_w = 1.0, 1.0 # Gradient Weights [cite: 120, 122]
    
    num_processors = len(processors)
    frequencies = sorted(processors[0]['frequencies'])
    periods = [t['p_i'] for t in tasks]
    hyper_period = periods[0]
    for p in periods[1:]:
        hyper_period = (hyper_period * p) // math.gcd(hyper_period, p)
    
    for t in tasks:
        t['num_jobs'] = hyper_period // t['p_i'] 

    num_processors = len(processors)
    frequencies = sorted(processors[0]['frequencies'])
    f_max = frequencies[-1]
    
    # 2. PHASE 1: FEASIBLE MAPPING (Worst-Fit) [cite: 130, 131]
    tasks_sorted = sorted(enumerate(tasks), key=lambda x: x[1]['e_m']/frequencies[-1]/x[1]['p_i'], reverse=True)
    processor_utilization = [0.0] * num_processors
    task_to_core = {}

    for i, t in tasks_sorted:
        target_core = processor_utilization.index(min(processor_utilization))
        util = (t['e_m'] / frequencies[-1]) / t['p_i']
        if processor_utilization[target_core] + util <= 1.0:
            task_to_core[i] = target_core
            processor_utilization[target_core] += util
        else:
            return "Infeasible Mapping"

    # 3. INITIAL STATE (Mandatory only, f_max) [cite: 130]
    current_state = []
    for t in tasks:
        current_state.append([{'f': frequencies[-1], 'k': 0} for _ in range(t['num_jobs'])])

    # 4. PHASE 2: MULTI-OPERATION LOCAL SEARCH [cite: 132, 134]
    improved = True
    while improved:
        improved = False
        best_move = None
        max_gradient = -float('inf')

        # Current Global Energy check
        total_energy = sum((alpha_c * ((t['e_m'] + sum(t['e_o_k'][:current_state[i][j]['k']])) / current_state[i][j]['f']) + 
                            beta_c * (current_state[i][j]['f']**2) * (t['e_m'] + sum(t['e_o_k'][:current_state[i][j]['k']])))
                           for i, t in enumerate(tasks) for j in range(t['num_jobs']))

        for i, t in enumerate(tasks):
            for j in range(t['num_jobs']):
                cf, ck = current_state[i][j]['f'], current_state[i][j]['k']
                f_idx = frequencies.index(cf)

                # EVALUATE OPERATIONS (O1 - O8) [cite: 134, 135-138, 120-123]
                potential_moves = []
                
                # Op 3: Inc Seg only 
                if ck < len(t['e_o_k']): potential_moves.append((cf, ck + 1))
                # Op 2: Dec Freq only [cite: 136]
                if f_idx > 0: potential_moves.append((frequencies[f_idx - 1], ck))
                # Op 7: Dec Freq + Inc Seg [cite: 122]
                if ck < len(t['e_o_k']) and f_idx > 0: potential_moves.append((frequencies[f_idx - 1], ck + 1))
                # Op 5: Inc Freq + Inc Seg [cite: 120]
                if ck < len(t['e_o_k']) and f_idx < len(frequencies)-1: potential_moves.append((frequencies[f_idx + 1], ck + 1))

                for nf, nk in potential_moves:
                    # Calculate Changes
                    delta_phi = t['u_i'] * (sum(t['e_o_k'][:nk]) - sum(t['e_o_k'][:ck]))
                    
                    old_e_eff = (t['e_m'] + sum(t['e_o_k'][:ck])) / cf
                    new_e_eff = (t['e_m'] + sum(t['e_o_k'][:nk])) / nf
                    delta_time = new_e_eff - old_e_eff
                    
                    old_en = alpha_c * old_e_eff + beta_c * (cf**2) * (t['e_m'] + sum(t['e_o_k'][:ck]))
                    new_en = alpha_c * new_e_eff + beta_c * (nf**2) * (t['e_m'] + sum(t['e_o_k'][:nk]))
                    delta_en = new_en - old_en

                    # Weighted Efficiency Gradient [cite: 122]
                    # Note: We divide by absolute values to handle negative utility/energy moves
                    denom = (alpha_w * delta_time + beta_w * delta_en)
                    gradient = delta_phi / denom if denom != 0 else 0

                    # Feasibility Check [cite: 69, 72]
                    if (total_energy + delta_en <= B_BUDGET):
                        util_change = (new_e_eff / t['p_i']) - (old_e_eff / t['p_i'])
                        if processor_utilization[task_to_core[i]] + util_change <= 1.0:
                            if gradient > max_gradient:
                                max_gradient = gradient
                                best_move = (i, j, nf, nk, delta_en, util_change)

        if best_move:
            i, j, nf, nk, d_en, d_util = best_move
            current_state[i][j]['f'], current_state[i][j]['k'] = nf, nk
            processor_utilization[task_to_core[i]] += d_util
            improved = True

    # 5. OUTPUT GENERATION (Same as previous versions)

    # 5. TERMINAL OUTPUT GENERATION
    print(f"\n{'='*105}")
    print(f"HEURISTIC USRT SCHEDULE (Hyper-period: {hyper_period})")
    print(f"{'='*105}")
    print(f"{'Start':<8} | {'End':<8} | {'Task':<6} | {'Core':<5} | {'Job':<5} | {'Freq':<6} | {'Segments':<10} | {'Energy':<10}")
    print("-" * 105)

    full_schedule = []
    final_utility = 0
    final_energy = 0

    for x in range(num_processors):
        core_jobs = []
        for i, t in enumerate(tasks):
            if task_to_core[i] == x:
                for j in range(t['num_jobs']):
                    cf, ck = current_state[i][j]['f'], current_state[i][j]['k']
                    total_exec_fmax = t['e_m'] + sum(t['e_o_k'][:ck])
                    e_eff = total_exec_fmax / cf
                    energy = alpha_c * e_eff + beta_c * (cf**2) * total_exec_fmax
                    
                    final_utility += t['u_i'] * sum(t['e_o_k'][:ck])
                    final_energy += energy
                    
                    core_jobs.append({
                        'release': j * t['p_i'],
                        'deadline': (j + 1) * t['p_i'],
                        'e_eff': e_eff,
                        'task': i, 'job': j, 'freq': cf, 'k': ck, 'seg_total': len(t['e_o_k']),
                        'core': x, 'energy': energy
                    })
        
        # EDF Sort on core x [cite: 49]
        core_jobs.sort(key=lambda x: x['deadline'])
        proc_time = 0
        for cj in core_jobs:
            start_time = max(proc_time, cj['release'])
            end_time = start_time + cj['e_eff']
            cj['start'] = round(start_time, 2)
            cj['end'] = round(end_time, 2)
            proc_time = end_time
            full_schedule.append(cj)

    full_schedule.sort(key=lambda x: x['start'])
    for item in full_schedule:
        print(f"{item['start']:<8} | {item['end']:<8} | T{item['task']:<5} | P{item['core']:<4} | J{item['job']:<4} | {item['freq']:<6.2f} | {item['k']}/{item['seg_total']:<8} | {item['energy']:<10.2f}")

    print("-" * 105)
    print(f"Total Utility: {final_utility:.2f} | Total Energy: {final_energy:.2f}/{B_BUDGET}")

if __name__ == "__main__":
    solve_usrt_enhanced_heuristic()