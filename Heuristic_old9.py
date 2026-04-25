import math
import sys
from testcase import testcase  # Assumes testcasev2.py is in the same directory

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

#Energy Model Parameters
ALPHA_PARAM = 1.0
BETA_PARAM = 1.0


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b) if a and b else 0

def hyperperiod(tasks):
    h = 1
    for t in tasks:
        h = lcm(h, t['p_i'])
    return h

# Job Data Structure

class Job:
    def __init__(self, task_id, task_index, release, deadline, e_m, e_o_list, u_i, p_i):
        self.task_id = task_id
        self.task_index = task_index
        self.release = release
        self.deadline = deadline
        self.e_m_nominal = e_m
        self.e_o_list_nominal = e_o_list
        self.u_i = u_i
        self.p_i = p_i

    def __repr__(self):
        return f"Job(T{self.task_id}, R:{self.release}, D:{self.deadline})"

#Helper

def calculate_total_exec_time_nominal(job, k):
    if k == 0:
        return job.e_m_nominal
    return job.e_m_nominal + sum(job.e_o_list_nominal[:k])

def calculate_actual_exec_time(nominal_exec_time, f):
    return nominal_exec_time / f

def calculate_energy(nominal_exec_time, f):
    if f <= 0: return float('inf')
    e_total = nominal_exec_time
    energy = ALPHA_PARAM * (e_total / f) * (BETA_PARAM * (f**2) + e_total)
    return energy

def calculate_utility(job, k):
    if k == 0:
        return 0.0
    optional_time = sum(job.e_o_list_nominal[:k])
    return job.u_i * optional_time

# Job Generation 
def generate_jobs_for_task(task, task_index, H):
    """Generates all jobs for a SINGLE task."""
    all_jobs = []
    p = task['p_i']
    num_jobs = H // p
    for j in range(num_jobs):
        release = j * p
        deadline = (j + 1) * p
        job = Job(task['id'], task_index, release, deadline, task['e_m'], task['e_o_k'], task['u_i'], p)
        all_jobs.append(job)
    return all_jobs

# WFDU TASK PARTITIONING 
def partition_tasks_WFDU(tasks, processors, max_util_limit=1.0):
    """
    Assigns each task to a processor using Best-Fit Decreasing Utilization.
    Returns (tasks_by_proc, success_flag)
    """
    num_processors = len(processors)
    tasks_by_proc = [[] for _ in range(num_processors)]
    
    # 1. Calculate utilization 
    task_data = []
    for i, task in enumerate(tasks):
        util = task['e_m'] / task['p_i'] # Mandatory utilization
        task_data.append({'original_index': i, 'util': util, 'task': task})
        
    # 2. Sort by utilization (Decreasing)
    task_data.sort(key=lambda x: x['util'], reverse=True)

    proc_utilization = [0.0] * num_processors
    
    print("Partitioning tasks using WFDU...")
    
    # 3. Assign tasks
    for td in task_data:
        task_idx = td['original_index']
        util = td['util']
        
        best_pid = -1
        min_resulting_util = float('inf') 

        # Find the processor that provides the "best fit"
        for pid in range(num_processors):
            resulting_util = proc_utilization[pid] + util
            
            # 1. Check if it's a valid fit (under the limit)
            if resulting_util <= max_util_limit + 1e-9:
                # 2. Check if it's the "best" (tightest) fit found so far
                if resulting_util < min_resulting_util: 
                    min_resulting_util = resulting_util
                    best_pid = pid

        if best_pid != -1:
            proc_utilization[best_pid] += util
            tasks_by_proc[best_pid].append({'task': td['task'], 'original_index': task_idx})
        else:
            # 4. If no processor could fit this task, partitioning fails
            print(f"{RED}WFDU Partitioning Failed: Task {td['task']['id']} (U={util:.4f}) could not be assigned.{RESET}")
            return None, False

    print(f"WFDU Partitioning Success:")
    for pid, task_list in enumerate(tasks_by_proc):
        task_ids = [t['task']['id'] for t in task_list]
        print(f"  Processor {pid} (Util: {proc_utilization[pid]:.4f}): Tasks {task_ids}")
        
    return tasks_by_proc, True


# --- PHASE 1 
def heuristic_scheduler_phase1_baseline(tasks_by_proc, processors, H, B_BUDGET):
    """
    Phase 1: Generates a mandatory-only (k=0) baseline schedule
    based on a *fixed task partitioning*.
    """
    print("Running Phase 1: Generating Max-Laxity Baseline...")
    
    baseline_schedule = []
    total_energy_used = 0.0 
    
    for pid, processor_data in enumerate(processors):
        
        proc_timeline_free_time = 0.0
        processor = processors[pid]
        task_list_for_this_proc = tasks_by_proc[pid]
        
        if not task_list_for_this_proc:
            continue 
        proc_jobs = []
        for task_info in task_list_for_this_proc:
            task = task_info['task']
            task_index = task_info['original_index']
            proc_jobs.extend(generate_jobs_for_task(task, task_index, H))
            
        if not proc_jobs:
            continue
            
        # --- Sort *this processor's* jobs by EDF ---
        proc_jobs.sort(key=lambda j: j.deadline)
        
        # 
        for job in proc_jobs:
            possible_choices = []
            time_options_found = 0 
            remaining_energy = B_BUDGET - total_energy_used

            #
            for frequency in processor['frequencies']:
                k = 0
                start_t = max(job.release, proc_timeline_free_time)
                nominal_time = calculate_total_exec_time_nominal(job, k)
                actual_time = calculate_actual_exec_time(nominal_time, frequency)
                finish_time = start_t + actual_time
                
                # Check 1: Time
                if finish_time <= job.deadline + 1e-9:
                    time_options_found += 1 
                    energy_cost = calculate_energy(nominal_time, frequency)
                    
                    # Check 2: Energy
                    if energy_cost <= remaining_energy + 1e-9: 
                        possible_choices.append({
                            "job": job, "processor_id": pid, "frequency": frequency,
                            "opt_k": k, "start_time": start_t, "finish_time": finish_time,
                            "utility": 0.0, "energy": energy_cost, "laxity": job.deadline - finish_time
                        })
            
            if possible_choices:
                # Greedy choice 
                best_choice = min(possible_choices, key=lambda x: x['finish_time'])
                
                baseline_schedule.append(best_choice)
                proc_timeline_free_time = best_choice['finish_time'] # Update *local* timeline
                total_energy_used += best_choice['energy'] # Update *global* energy
            else:
                # No valid choice found for this job.
                if time_options_found > 0:
                    return None, 0.0, "FAILURE_ENERGY"
                else:
                    return None, 0.0, "FAILURE_TIME"

    # If all loops complete, it's a success
    print(f"{GREEN}Phase 1 Success: Mandatory baseline is schedulable.{RESET}")
    return baseline_schedule, total_energy_used, "SUCCESS"


# 
def heuristic_scheduler_phase2_constrained_upgrade(baseline_schedule, processors, B_budget, total_baseline_energy):
    print("Running Phase 2: Full-Constraint Utility Upgrade...")
    remaining_energy = B_budget - total_baseline_energy
    if remaining_energy < 1e-9:
        print(f"{YELLOW}Warning: No energy budget left for optional segments.{RESET}")
        return baseline_schedule

    schedule_by_proc = [[] for _ in range(len(processors))]
    for jc in baseline_schedule:
        schedule_by_proc[jc['processor_id']].append(jc)
    for lst in schedule_by_proc:
        lst.sort(key=lambda x: x['start_time'])

    iteration = 0
    
    max_e_o_k_len = 0
    if baseline_schedule:
         max_e_o_k_len = max(len(jc['job'].e_o_list_nominal) for jc in baseline_schedule)
    MAX_ITER = len(baseline_schedule) * max_e_o_k_len + 1

    while iteration < MAX_ITER:
        iteration += 1
        best_upgrade = None
        best_density = -1
        for pid, proc_list in enumerate(schedule_by_proc):
            for jidx, jc in enumerate(proc_list):
                job = jc['job']
                cur_k = jc['opt_k']
                max_k = len(job.e_o_list_nominal)
                if cur_k >= max_k: continue
                new_k = cur_k + 1
                f = jc['frequency']
                util_new = calculate_utility(job, new_k)
                util_old = calculate_utility(job, cur_k)
                marg_util = util_new - util_old
                if marg_util <= 1e-9: continue
                nom_new = calculate_total_exec_time_nominal(job, new_k)
                nom_old = calculate_total_exec_time_nominal(job, cur_k)
                e_new = calculate_energy(nom_new, f)
                e_old = calculate_energy(nom_old, f)
                marg_e = e_new - e_old
                t_new = calculate_actual_exec_time(nom_new, f)
                t_old = calculate_actual_exec_time(nom_old, f)
                marg_t = t_new - t_old
                if marg_e > remaining_energy + 1e-9: continue
                if jc['laxity'] < marg_t - 1e-9: continue
                if any(succ['laxity'] < marg_t - 1e-9 for succ in proc_list[jidx+1:]): continue
                density = marg_util / marg_e if marg_e > 1e-9 else float('inf')
                if density > best_density:
                    best_density = density
                    best_upgrade = {"pid": pid, "jidx": jidx, "new_k": new_k, "marg_e": marg_e, "marg_t": marg_t}
        if not best_upgrade:
            break
        pid, jidx = best_upgrade['pid'], best_upgrade['jidx']
        jc = schedule_by_proc[pid][jidx]
        job = jc['job']
        f = jc['frequency']
        remaining_energy -= best_upgrade['marg_e']
        jc['opt_k'] = best_upgrade['new_k']
        nom_time = calculate_total_exec_time_nominal(job, best_upgrade['new_k'])
        jc['finish_time'] = jc['start_time'] + calculate_actual_exec_time(nom_time, f)
        jc['utility'] = calculate_utility(job, best_upgrade['new_k'])
        jc['energy'] = calculate_energy(nom_time, f)
        jc['laxity'] = job.deadline - jc['finish_time']
        prev_ft = jc['finish_time']
        for i in range(jidx+1, len(schedule_by_proc[pid])):
            sc = schedule_by_proc[pid][i]
            jb = sc['job']
            f_j = sc['frequency']
            k_j = sc['opt_k']
            nom_j = calculate_total_exec_time_nominal(jb, k_j)
            act_j = calculate_actual_exec_time(nom_j, f_j)
            sc['start_time'] = max(jb.release, prev_ft)
            sc['finish_time'] = sc['start_time'] + act_j
            sc['laxity'] = jb.deadline - sc['finish_time']
            prev_ft = sc['finish_time']

    print(f"Phase 2: Finished after {iteration-1} successful upgrade iterations.")
    final_schedule = [jc for proc in schedule_by_proc for jc in proc]
    return final_schedule

# PRINT FUNCTION
def print_schedule(schedule, total_energy, total_utility, B_budget, processors):
    schedule_by_proc = {}
    for c in schedule:
        pid = c['processor_id']
        schedule_by_proc.setdefault(pid, []).append(c)
    
    for lst in schedule_by_proc.values():
        lst.sort(key=lambda x: x['start_time'])

    with open("output_heuristic.txt", "w") as f:
        f.write("="*60 + "\n")
        f.write("--- (WFDU) MAX-LAXITY-BASELINE HEURISTIC RESULTS ---\n")
        f.write("="*60 + "\n\n")
        f.write(f"Total Utility: {total_utility:.4f}\n")
        f.write(f"Total Energy:  {total_energy:.4f} / {B_budget:.4f}\n\n")
        f.write(f"All {len(schedule)} jobs were scheduled successfully!\n") 

        f.write("\n--- Full Schedule (Processor-wise) ---\n\n")

        for pid in sorted(schedule_by_proc.keys()):
            proc_list = schedule_by_proc[pid]
            f.write(f"Processor {pid} ({len(proc_list)} jobs):\n")
            header = f"{'Job':<8} {'k':<2} {'f':<5} {'Start':<10} {'Finish':<10} {'Util':<10} {'Energy':<10} {'Laxity':<10}\n"
            f.write(header)
            f.write("-" * len(header) + "\n")
            for c in proc_list:
                j = c['job']
                f.write(f"T{j.task_id}.J{j.release//j.p_i:<4} "
                        f"{c['opt_k']:<2} {c['frequency']:<5.2f} "
                        f"{c['start_time']:<10.2f} {c['finish_time']:<10.2f} "
                        f"{c['utility']:<10.2f} {c['energy']:<10.2f} "
                        f"{c['laxity']:<10.2f}\n")
            f.write("\n")

    # Summary on console only
    print(f"{GREEN}Total Utility: {total_utility:.4f}{RESET}")
    print(f"Total Energy:  {total_energy:.4f} / {B_BUDGET:.4f}")
    print("="*40)
    print(f"{GREEN}All jobs scheduled successfully!{RESET}")
    print(">< :)")
    print(f"\n{GREEN}Full, processor-wise schedule saved to 'output_heuristic.txt'{RESET}")

#Main Execution (MODIFIED)
if __name__ == "__main__":
    try:
        processors, TASKS, B_BUDGET = testcase()
        processors_copy = [p.copy() for p in processors]
        H = hyperperiod(TASKS)
        if H > 2000:
            print(f"{YELLOW}Warning: Hyperperiod is very large (H={H}).{RESET}")
        
        tasks_by_proc, partition_success = partition_tasks_WFDU(TASKS, processors_copy, max_util_limit=1.0)
        
        if not partition_success:
            print(f"\n{RED}The tasks are not schedulable using WFDU partitioning.{RESET}")
            sys.exit() # 
        baseline_schedule, base_e, status = heuristic_scheduler_phase1_baseline(
            tasks_by_proc, processors_copy, H, B_BUDGET
        )
        
        if status == "SUCCESS":
            final_schedule = heuristic_scheduler_phase2_constrained_upgrade(baseline_schedule, processors_copy, B_BUDGET, base_e)
            
            final_energy = sum(c['energy'] for c in final_schedule)
            final_utility = sum(c['utility'] for c in final_schedule)
            
            print_schedule(final_schedule, final_energy, final_utility, B_BUDGET, processors)
        
        elif status == "FAILURE_ENERGY":
            print(f"\n{RED}Energy budget too low for this task partition.{RESET}")
            
        elif status == "FAILURE_TIME":
            print(f"\n{RED}The tasks are not schedulable using EDF with this WFDU partition.{RESET}")
        
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")
        import traceback; traceback.print_exc()