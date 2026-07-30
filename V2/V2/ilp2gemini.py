import pulp
import math

def solve_usrt_quanta_final(processors_data, tasks_data, B_BUDGET):
    # --- 1. System Constants ---
    alpha, beta = 1.0, 1.0 # [cite: 53]
    freqs = processors_data[0]['frequencies'] # [cite: 32]
    num_procs = len(processors_data)
    
    # Calculate Quanta based on Task Set 
    periods = [t['p_i'] for t in tasks_data]
    gcd_quanta = math.gcd(*periods) 
    hyper_period = math.lcm(*periods) # [cite: 44]
    
    # --- 2. Job Generation [cite: 36, 37, 45] ---
    all_jobs = []
    for t in tasks_data:
        for j in range(hyper_period // t['p_i']):
            all_jobs.append({
                'task_id': t['id'],
                'job_idx': j,
                'release': j * t['p_i'],
                'deadline': (j + 1) * t['p_i'],
                'e_m': t['e_m'],
                'e_o_k': t['e_o_k'],
                'u_i': t['u_i'],
                'mapped_core': None
            })

    # --- 3. Phase 1: Quanta-Based SPS Mapping [cite: 28, 96, 119] ---
    storage = []
    mapped_jobs = []
    
    for t_start in range(0, hyper_period, gcd_quanta):
        t_end = t_start + gcd_quanta
        # Pull jobs: Arrived now + Carry-over from storage
        current_pool = [j for j in all_jobs if j['release'] == t_start] + storage
        storage = []

        # Compulsory: Jobs that MUST finish by the end of this quanta [cite: 39]
        compulsory = [j for j in current_pool if j['deadline'] <= t_end]
        optional_pool = [j for j in current_pool if j['deadline'] > t_end]
        
        # Iterative Reduction based on your optimization logic
        valid_set = compulsory + optional_pool
        while True:
            # Check if mandatory load fits in current quanta [cite: 75]
            total_load = sum(j['e_m'] for j in valid_set)
            if (total_load / num_procs) <= gcd_quanta or not optional_pool:
                break
            # Optimization: Remove lowest utility density optional job
            optional_pool.sort(key=lambda x: x['u_i']) 
            storage.append(optional_pool.pop(0))
            valid_set = compulsory + optional_pool

        # Finalize mapping for this quanta
        for idx, job in enumerate(valid_set):
            job['mapped_core'] = idx % num_procs 
            mapped_jobs.append(job)

    # --- 4. Phase 2: ILP Refinement [cite: 63, 102] ---
    prob = pulp.LpProblem("USRT_V2_Final", pulp.LpMaximize) # [cite: 85, 114]

    # Variables Y(job_i, segment_k, freq_z) [cite: 64, 100]
    Y = {}
    for i, job in enumerate(mapped_jobs):
        for k in range(len(job['e_o_k']) + 1):
            for z in range(len(freqs)):
                Y[(i, k, z)] = pulp.LpVariable(f"Y_j{i}_k{k}_z{z}", cat='Binary')

    # [C1] Single configuration per job [cite: 66, 103]
    for i in range(len(mapped_jobs)):
        prob += pulp.lpSum(Y[(i, k, z)] for k in range(len(mapped_jobs[i]['e_o_k']) + 1) 
                           for z in range(len(freqs))) == 1

    # [C2] Timing: Demand Bound Function (DBF) per Processor [cite: 69, 106, 111]
    all_deadlines = sorted(list(set(j['deadline'] for j in mapped_jobs)))
    for p_id in range(num_procs):
        core_jobs = [i for i, j in enumerate(mapped_jobs) if j['mapped_core'] == p_id]
        for t_d in all_deadlines:
            demand = []
            for i in core_jobs:
                job = mapped_jobs[i]
                if job['deadline'] <= t_d: 
                    for k in range(len(job['e_o_k']) + 1):
                        base_exec = job['e_m'] + sum(job['e_o_k'][:k]) # [cite: 43]
                        for z, f_z in enumerate(freqs):
                            demand.append(Y[(i, k, z)] * (base_exec / f_z)) # [cite: 53]
            if demand:
                prob += pulp.lpSum(demand) <= t_d # [cite: 75, 113]

    # [C3] Energy Budget [cite: 57, 78, 80]
    total_energy = []
    for i, job in enumerate(mapped_jobs):
        for k in range(len(job['e_o_k']) + 1):
            base_exec = job['e_m'] + sum(job['e_o_k'][:k])
            for z, f_z in enumerate(freqs):
                eff_exec = base_exec / f_z # [cite: 53]
                # E = alpha * eff_time + beta * f^2 * base_time [cite: 53]
                energy_val = (alpha * eff_exec) + (beta * (f_z**2) * base_exec)
                total_energy.append(Y[(i, k, z)] * energy_val)
    prob += pulp.lpSum(total_energy) <= B_BUDGET

    # Objective: Maximize Utility [cite: 48, 85, 91]
    total_utility = []
    for i, job in enumerate(mapped_jobs):
        for k in range(1, len(job['e_o_k']) + 1):
            opt_time = sum(job['e_o_k'][:k]) # [cite: 89]
            for z in range(len(freqs)):
                total_utility.append(Y[(i, k, z)] * job['u_i'] * opt_time)
    prob += pulp.lpSum(total_utility)

    # --- 5. Output ---
    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    print(f"## Final Statistics | GCD Quanta: {gcd_quanta} ##")
    print(f"Status: {pulp.LpStatus[prob.status]}")
    if prob.status == pulp.LpStatusOptimal:
        print(f"Utility: {pulp.value(prob.objective):.2f} | Energy: {sum(pulp.value(e) for e in total_energy if not isinstance(e, int) and pulp.value(e)):.2f}/{B_BUDGET}")
        print("-" * 65)
        print(f"{'Job':<10} | {'Core':<5} | {'Freq':<5} | {'Segments':<10} | {'Utility':<8}")
        for i, job in enumerate(mapped_jobs):
            for k in range(len(job['e_o_k']) + 1):
                for z, f_z in enumerate(freqs):
                    if pulp.value(Y[(i, k, z)]) == 1:
                        u = job['u_i'] * sum(job['e_o_k'][:k]) if k > 0 else 0
                        print(f"T{job['task_id']}J{job['job_idx']:<5} | {job['mapped_core']:<5} | {f_z:<5} | {k:<10} | {u:<8.2f}")
    else:
        print("Result: Infeasible. Mandatory load exceeds capacity.")

# Execute
processors = [{'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], 'id': 0},
              {'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], 'id': 1}]
tasks = [
    {'id': 0, 'e_m': 21.73598, 'e_o_k': [18.62630], 'p_i': 90, 'u_i': 2.97},
    {'id': 1, 'e_m': 5.76079, 'e_o_k': [3.34772, 10.94708, 2.90908, 3.20241, 3.88504], 'p_i': 15, 'u_i': 2.09},
    {'id': 2, 'e_m': 13.71688, 'e_o_k': [21.26160, 24.49777], 'p_i': 180, 'u_i': 2.25},
    {'id': 3, 'e_m': 10.63144, 'e_o_k': [15.53865, 8.25445, 6.01048, 7.58046], 'p_i': 45, 'u_i': 2.93}
]
solve_usrt_quanta_final(processors, tasks, 80000)