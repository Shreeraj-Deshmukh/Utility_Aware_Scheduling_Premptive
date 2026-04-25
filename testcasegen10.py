import random
import pprint
import math

def uunifast(n, U_total):
    s = [0.0] * (n + 1)
    s[n] = U_total
    for i in range(n, 1, -1):
        rand_num = random.random()
        s[i-1] = s[i] * (rand_num ** (1.0 / (i - 1)))
    return [s[i] - s[i-1] for i in range(1, n + 1)]

def generate_tasks(task_count, total_utilization):
    utilizations = uunifast(task_count, total_utilization)
    tasks = []
    PERIOD_CHOICES = [200, 300, 500, 600, 800] # Adjusted to match your example p_i values

    for i in range(task_count):
        task_util = utilizations[i]
        p_i = random.choice(PERIOD_CHOICES)
        total_e = task_util * p_i
        e_m = total_e * random.uniform(0.4, 0.6) 
        e_opt_total = total_e - e_m
        
        e_o_k = []
        num_optional_segments = random.randint(1, 8)
        if num_optional_segments > 0 and e_opt_total > 0:
            seg_times = [random.random() for _ in range(num_optional_segments)]
            total_rand = sum(seg_times)
            e_o_k = [(t / total_rand) * e_opt_total for t in seg_times]
        
        tasks.append({
            'id': i, 
            'p_i': p_i, 
            'e_m': e_m, 
            'e_o_k': e_o_k,
            'u_i': round(random.uniform(1.0, 3.5), 2)
        })
    return tasks

def create_formatted_testcase_file(num_tasks=5):
    print(f"Generating testcase.py with {num_tasks} tasks...")
    
    processors = [{'frequencies': [0.6, 0.8, 1.0], 'id': i} for i in range(3)]
    tasks = generate_tasks(num_tasks, total_utilization=1.1)
    B_BUDGET = 500000

    with open("testcase.py", "w") as f:
        f.write("import math\n\n")
        f.write("def testcase():\n")
        
        # Write Processors
        f.write(f"    processors = {pprint.pformat(processors, indent=4)}\n\n")
        
        # Write Tasks
        f.write(f"    tasks = {pprint.pformat(tasks, indent=4)}\n\n")
        
        # Write Budget and Return statement
        f.write(f"    B_BUDGET = {B_BUDGET}\n")
        f.write("    return processors, tasks, B_BUDGET\n")
        
    print("Successfully created 'testcase.py'")

if __name__ == "__main__":
    # You can change '5' to any number of tasks you need for your experiment
    create_formatted_testcase_file(7)