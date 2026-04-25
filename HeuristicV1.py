import math
import random
from testcase import testcase

def solve_usrt_heuristic():
    # 1. LOAD DATA & PREPROCESSING
    processors, tasks, B_BUDGET = testcase()
    alpha_const, beta_const = 1.0, 1.0  # Energy constants    
    #  -- Hyper-period 
    periods = [t['p_i'] for t in tasks]
    hyper_period = periods[0]
    for p in periods[1:]:
        hyper_period = (hyper_period * p) // math.gcd(hyper_period, p)
    
    for t in tasks:
        t['num_jobs'] = hyper_period // t['p_i'] 

    num_processors = len(processors)
    frequencies = sorted(processors[0]['frequencies'])
    f_max = frequencies[-1]

    # 2. PHASE 1: FEASIBLE MAPPING (Worst-Fit / Load Balanced) 
    # Sort tasks by decreasing utilization (e_m / p_i)
    tasks_sorted = sorted(enumerate(tasks), key=lambda x: x[1]['e_m']/x[1]['p_i'], reverse=True)
    
    processor_utilization = [0.0] * num_processors
    task_to_core = {}

    for i, t in tasks_sorted:
        # Load balancing: Find processor with minimum current utilization 
        target_core = processor_utilization.index(min(processor_utilization))
        
        # UDF Feasibility Check at f_max with 0 optional segments
        task_util = (t['e_m'] / f_max) / t['p_i']
        if processor_utilization[target_core] + task_util <= 1.0:
            task_to_core[i] = target_core
            processor_utilization[target_core] += task_util
        else:
            print(f"Phase 1 Failed: Task {i} is not feasible on any core.")
            return

    # 3. INITIALIZE STATE (Mandatory only, f_max)
    # current_state[task_idx][job_idx] = {'f': frequency, 'k': num_segments}
    current_state = []
    for i, t in enumerate(tasks):
        current_state.append([{'f': f_max, 'k': 0} for _ in range(t['num_jobs'])])

    # 4. PHASE 2: LOCAL SEARCH (Gradient-Based) 
    # alpha_w and beta_w are the preference weights for the Weighted Efficiency Gradient
    alpha_w, beta_w = 1,1
    
    improved = True
    while improved:
        improved = False
        best_move = None
        max_gradient = -float('inf')

        # Check total energy consumption of current state
        total_energy = 0
        for i, t in enumerate(tasks):
            for j in range(t['num_jobs']):
                cf, ck = current_state[i][j]['f'], current_state[i][j]['k']
                e_eff = (t['e_m'] + sum(t['e_o_k'][:ck])) / cf 
                total_energy += alpha_const * e_eff + beta_const * (cf**2) * (t['e_m'] + sum(t['e_o_k'][:ck])) 
        # Evaluate Operation 7: Dec Freq + Inc Optional Seg 
        for i, t in enumerate(tasks):
            for j in range(t['num_jobs']):
                cf, ck = current_state[i][j]['f'], current_state[i][j]['k']
                
                # Check if we can apply Operation 7 (Dec Freq + Inc Seg)
                if ck < len(t['e_o_k']) and cf > frequencies[0]:
                    new_f = frequencies[frequencies.index(cf) - 1]
                    new_k = ck + 1
                    
                    # Calculate Gradient Components
                    delta_phi = t['u_i'] * t['e_o_k'][ck]
                    
                    old_e_eff = (t['e_m'] + sum(t['e_o_k'][:ck])) / cf
                    new_e_eff = (t['e_m'] + sum(t['e_o_k'][:new_k])) / new_f
                    delta_time = new_e_eff - old_e_eff
                    
                    old_en = alpha_const * old_e_eff + beta_const * (cf**2) * (t['e_m'] + sum(t['e_o_k'][:ck]))
                    new_en = alpha_const * new_e_eff + beta_const * (new_f**2) * (t['e_m'] + sum(t['e_o_k'][:new_k]))
                    delta_en = new_en - old_en
                    
                    # Weighted Efficiency Gradient calculation
                    gradient = delta_phi / (alpha_w * delta_time + beta_w * delta_en)

                    # Feasibility check for Energy and Timing (simplified)
                    if (total_energy + delta_en <= B_BUDGET):
                        # Timing check: check if new utilization on its core is still <= 1.0
                        core = task_to_core[i]
                        util_change = (new_e_eff / t['p_i']) - (old_e_eff / t['p_i'])
                        if processor_utilization[core] + util_change <= 1.0:
                            if gradient > max_gradient:
                                max_gradient = gradient
                                best_move = (i, j, new_f, new_k, delta_en, util_change)

        if best_move:
            i, j, nf, nk, d_en, d_util = best_move
            current_state[i][j]['f'] = nf
            current_state[i][j]['k'] = nk
            processor_utilization[task_to_core[i]] += d_util
            improved = True

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
                    energy = alpha_const * e_eff + beta_const * (cf**2) * total_exec_fmax
                    
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
    solve_usrt_heuristic()