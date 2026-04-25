import gurobipy as gp
from gurobipy import GRB
import math
# This imports the testcase() function from your external file (e.g., testcase_file.py)
from testcase import testcase 

def solve_usrt_btp():
    # 1. LOAD DATA [cite: 144, 145]
    processors, tasks, B_BUDGET = testcase()
    
    # Constants for Energy Model [cite: 139]
    alpha, beta = 1.0, 1.0
    
    model = gp.Model("USRT_Scheduling")
    model.Params.OutputFlag = 0  # Clean terminal output

    # 2. PREPROCESSING
    # Calculate Hyper-period (h = lcm{p_i}) [cite: 132]
    periods = [t['p_i'] for t in tasks]
    hyper_period = periods[0]
    for p in periods[1:]:
        hyper_period = (hyper_period * p) // math.gcd(hyper_period, p)
    
    # Calculate number of jobs for each task [cite: 133]
    for t in tasks:
        t['num_jobs'] = hyper_period // t['p_i']

    num_processors = len(processors)
    num_tasks = len(tasks)
    frequencies = processors[0]['frequencies'] 

    # 3. DECISION VARIABLES
    # V[i, x]: Task-to-core mapping (1 if task i is on processor x) [cite: 168, 171]
    V = model.addVars(num_tasks, num_processors, vtype=GRB.BINARY, name="V")

    # X[i, j, k, z]: Job configuration [cite: 169, 174]
    # 1 if job j of task i uses freq f_z and executes up to optional segment k
    X = {}
    for i, t in enumerate(tasks):
        num_segments = len(t['e_o_k'])
        for j in range(t['num_jobs']):
            for k in range(num_segments + 1): # k=0 is mandatory only [cite: 127]
                for z, f in enumerate(frequencies):
                    X[i, j, k, z] = model.addVar(vtype=GRB.BINARY, name=f"X_{i}_{j}_{k}_{z}")

    # 4. OBJECTIVE & CONSTRAINTS
    # Objective: Maximize total utility [cite: 186, 192]
    obj = gp.LinExpr()
    total_energy = gp.LinExpr()

    for i, t in enumerate(tasks):
        num_segments = len(t['e_o_k'])
        for j in range(t['num_jobs']):
            # [C2] Each job must have exactly one configuration [cite: 176]
            model.addConstr(gp.quicksum(X[i, j, k, z] for k in range(num_segments + 1) 
                                       for z in range(len(frequencies))) == 1)
            
            for k in range(num_segments + 1):
                # Total execution time at f_max [cite: 131, 132]
                total_exec_fmax = t['e_m'] + sum(t['e_o_k'][:k])
                
                for z, f in enumerate(frequencies):
                    # Utility: u_i * sum of optional segments [cite: 192]
                    if k > 0:
                        obj += t['u_i'] * sum(t['e_o_k'][:k]) * X[i, j, k, z]
                    
                    # Energy Model [cite: 139]
                    e_eff = total_exec_fmax / f
                    energy_val = alpha * e_eff + beta * (f**2) * total_exec_fmax
                    total_energy += energy_val * X[i, j, k, z]

    model.setObjective(obj, GRB.MAXIMIZE)

    # [C1] Each task mapped to exactly one processor [cite: 172]
    for i in range(num_tasks):
        model.addConstr(V.sum(i, '*') == 1)

    # [C4] Energy Budget [cite: 182, 183]
    model.addConstr(total_energy <= B_BUDGET)

    # [C3] Feasibility (Utilization Check per Processor) [cite: 146]
    for x in range(num_processors):
        utilization = gp.LinExpr()
        for i, t in enumerate(tasks):
            for j in range(t['num_jobs']):
                for k in range(len(t['e_o_k']) + 1):
                    total_exec_fmax = t['e_m'] + sum(t['e_o_k'][:k])
                    for z, f in enumerate(frequencies):
                        e_eff = total_exec_fmax / f
                        # Link job execution to the assigned processor
                        # Using indicator: if X is 1 and V is 1, add to utilization
                        aux = model.addVar(vtype=GRB.CONTINUOUS)
                        model.addConstr(aux >= e_eff * (X[i, j, k, z] + V[i, x] - 1))
                        utilization += aux
        model.addConstr(utilization <= hyper_period)

    # 5. SOLVE
    model.optimize()

    # 6. TERMINAL OUTPUT (THE SCHEDULE)
    if model.status == GRB.OPTIMAL:
        print(f"\n{'='*70}")
        print(f"USRT OPTIMAL SCHEDULE (Hyper-period: {hyper_period})")
        print(f"Total Utility: {model.objVal:.2f}")
        print(f"Total Energy: {total_energy.getValue():.2f} / {B_BUDGET}")
        print(f"{'='*70}")
        
        # Get mapping
        task_proc = {i: x for i in range(num_tasks) for x in range(num_processors) if V[i, x].X > 0.5}

        print(f"{'Task':<8} | {'Core':<6} | {'Job':<6} | {'Freq':<6} | {'Segments (Opt/Total)'}")
        print("-" * 70)
        
        for i, t in enumerate(tasks):
            for j in range(t['num_jobs']):
                for k in range(len(t['e_o_k']) + 1):
                    for z, f in enumerate(frequencies):
                        if X[i, j, k, z].X > 0.5:
                            print(f"T{i:<7} | P{task_proc[i]:<5} | J{j:<5} | {f:<6.2f} | {k} / {len(t['e_o_k'])}")
    else:
        print("Optimization failed or was infeasible.")

if __name__ == "__main__":
    solve_usrt_btp()