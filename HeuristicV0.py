import math
from testcase import testcase

def solve_usrt_utility_density():
    # 1. SETUP
    processors, tasks, B_BUDGET = testcase()
    alpha_c, beta_c = 1.0, 1.0
    f_max = sorted(processors[0]['frequencies'])[-1]
    
    # Calculate Hyper-period
    periods = [t['p_i'] for t in tasks]
    hyper_period = periods[0]
    for p in periods[1:]:
        hyper_period = (hyper_period * p) // math.gcd(hyper_period, p)

    # 2. PHASE 1: MANDATORY MAPPING (Worst-Fit)
    tasks_sorted = sorted(enumerate(tasks), key=lambda x: x[1]['e_m']/f_max/x[1]['p_i'], reverse=True)
    processor_utilization = [0.0] * len(processors)
    task_to_core = {}

    for i, t in tasks_sorted:
        target_core = processor_utilization.index(min(processor_utilization))
        util = (t['e_m'] / f_max) / t['p_i']
        if processor_utilization[target_core] + util <= 1.0:
            task_to_core[i] = target_core
            processor_utilization[target_core] += util
        else:
            return "Infeasible Mandatory Mapping"

    # 3. INITIAL STATE
    current_state = []
    for t in tasks:
        num_jobs = hyper_period // t['p_i']
        current_state.append([{'f': f_max, 'k': 0} for _ in range(num_jobs)])

    # 4. PHASE 2: GREEDY UTILITY DENSITY
    improved = True
    while improved:
        improved = False
        best_job = None
        max_density = -1

        # Calculate current global energy
        total_energy = 0
        for i, t in enumerate(tasks):
            for j in range(len(current_state[i])):
                ck = current_state[i][j]['k']
                total_len = t['e_m'] + sum(t['e_o_k'][:ck])
                total_energy += alpha_c * (total_len/f_max) + beta_c * (f_max**2) * total_len

        for i, t in enumerate(tasks):
            for j in range(len(current_state[i])):
                ck = current_state[i][j]['k']
                if ck < len(t['e_o_k']):
                    # UTILITY DENSITY = Utility / Execution Time of this specific segment
                    u_gain = t['u_i'] * t['e_o_k'][ck]
                    t_cost = t['e_o_k'][ck] / f_max
                    density = u_gain / t_cost  # Note: t['e_o_k'][ck] cancels out, so this is effectively t['u_i'] * f_max
                    
                    # More advanced density: U / (Time_Cost + Energy_Cost)
                    # For now, let's use U / Time_Cost
                    if density > max_density:
                        # Feasibility Checks
                        d_en = (alpha_c * t_cost) + (beta_c * (f_max**2) * t['e_o_k'][ck])
                        d_util = t_cost / t['p_i']
                        
                        if (total_energy + d_en <= B_BUDGET) and \
                           (processor_utilization[task_to_core[i]] + d_util <= 1.0):
                            max_density = density
                            best_job = (i, j, d_en, d_util)

        if best_job:
            i, j, d_en, d_util = best_job
            current_state[i][j]['k'] += 1
            processor_utilization[task_to_core[i]] += d_util
            improved = True

    # 5. CALCULATE FINAL UTILITY
    final_utility = sum(t['u_i'] * sum(t['e_o_k'][:current_state[i][j]['k']]) 
                        for i, t in enumerate(tasks) for j in range(len(current_state[i])))
    
    print(f"\nFinal Utility (Density-Based): {final_utility:.2f}")
    print(f"Final Energy: {total_energy:.2f} / {B_BUDGET}")

if __name__ == "__main__":
    solve_usrt_utility_density()