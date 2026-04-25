import gurobipy as gp
from gurobipy import GRB
import math
from testcase import testcase 

def solve_usrt_btp():
    # 1. LOAD DATA 
    processors, tasks, B_BUDGET = testcase()
    
    # Constants for Energy Model 
    alpha, beta = 1.0, 1.0
    
    model = gp.Model("USRT_Full_ILP")
    model.Params.OutputFlag = 1  # Display Gurobi log for complex timing constraints

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
    # V[i, x]: Task-to-core mapping [cite: 168, 171]
    V = model.addVars(num_tasks, num_processors, vtype=GRB.BINARY, name="V")

    # X[i, j, k, z]: Job configuration (freq z, segment k) [cite: 169, 174]
    X = {}
    for i, t in enumerate(tasks):
        num_segments = len(t['e_o_k'])
        for j in range(t['num_jobs']):
            for k in range(num_segments + 1): # k=0 is mandatory only [cite: 127]
                for z, f in enumerate(frequencies):
                    X[i, j, k, z] = model.addVar(vtype=GRB.BINARY, name=f"X_{i}_{j}_{k}_{z}")

    # A[i, j, k, z, x]: Linearized auxiliary variable (V[i,x] * X[i,j,k,z])
    A = {}
    for i, t in enumerate(tasks):
        for j in range(t['num_jobs']):
            for k in range(len(t['e_o_k']) + 1):
                for z in range(len(frequencies)):
                    for x in range(num_processors):
                        A[i, j, k, z, x] = model.addVar(vtype=GRB.BINARY, name=f"A_{i}_{j}_{k}_{z}_{x}")

    # 4. OBJECTIVE & CONSTRAINTS
    obj = gp.LinExpr()
    total_energy = gp.LinExpr()

    for i, t in enumerate(tasks):
        num_segments = len(t['e_o_k'])
        for j in range(t['num_jobs']):
            # [C2] Job configuration constraint: exactly one freq/segment level [cite: 176]
            model.addConstr(gp.quicksum(X[i, j, k, z] for k in range(num_segments + 1) 
                                       for z in range(len(frequencies))) == 1)
            
            for k in range(num_segments + 1):
                # Total exec time at f_max (Task-level constants) [cite: 131, 132]
                total_exec_fmax = t['e_m'] + sum(t['e_o_k'][:k])
                
                for z, f in enumerate(frequencies):
                    # Objective: Maximize total utility [cite: 186, 192]
                    if k > 0:
                        obj += t['u_i'] * sum(t['e_o_k'][:k]) * X[i, j, k, z]
                    
                    # Energy Model 
                    e_eff = total_exec_fmax / f
                    energy_val = alpha * e_eff + beta * (f**2) * total_exec_fmax
                    total_energy += energy_val * X[i, j, k, z]
                    
                    # Linearization for A = V * X [cite: 72, 73]
                    for x in range(num_processors):
                        model.addConstr(A[i, j, k, z, x] <= V[i, x])
                        model.addConstr(A[i, j, k, z, x] <= X[i, j, k, z])
                        model.addConstr(A[i, j, k, z, x] >= V[i, x] + X[i, j, k, z] - 1)

    model.setObjective(obj, GRB.MAXIMIZE)

    # [C1] Each task mapped to exactly one processor [cite: 172]
    for i in range(num_tasks):
        model.addConstr(V.sum(i, '*') == 1)

    # [C4] Total energy consumption <= energy budget B [cite: 182, 183]
    model.addConstr(total_energy <= B_BUDGET)

    # [C3] Interval-Based Timing Constraint (DBF for EDF) [cite: 146]
    # Critical points: release times (t1) and deadlines (t2)
    R = sorted(list(set((j)*t['p_i'] for t in tasks for j in range(t['num_jobs']))))
    D = sorted(list(set((j+1)*t['p_i'] for t in tasks for j in range(t['num_jobs']))))

    for x in range(num_processors):
        for t1 in R:
            for t2 in D:
                if t1 < t2:
                    demand = gp.LinExpr()
                    has_jobs = False
                    for i, t in enumerate(tasks):
                        for j in range(t['num_jobs']):
                            # S(t1, t2): jobs with release >= t1 AND deadline <= t2 [cite: 66]
                            if (j * t['p_i'] >= t1) and ((j+1) * t['p_i'] <= t2):
                                has_jobs = True
                                for k in range(len(t['e_o_k']) + 1):
                                    e_eff_config = (t['e_m'] + sum(t['e_o_k'][:k]))
                                    for z, f in enumerate(frequencies):
                                        # e_eff = (mandatory + optional) / frequency 
                                        e_eff = e_eff_config / f
                                        demand += e_eff * A[i, j, k, z, x]
                    if has_jobs:
                        model.addConstr(demand <= (t2 - t1), name=f"C3_P{x}_{t1}_{t2}")

    # 5. SOLVE
    model.optimize()

    # 6. OUTPUT
    if model.status == GRB.OPTIMAL:
        print(f"\n{'='*75}")
        print(f"USRT OPTIMAL SCHEDULE")
        print(f"Total Utility: {model.objVal:.2f} | Total Energy: {total_energy.getValue():.2f}/{B_BUDGET}")
        print(f"{'='*75}")
        
        task_proc = {i: x for i in range(num_tasks) for x in range(num_processors) if V[i, x].X > 0.5}
        print(f"{'Task':<8} | {'Core':<6} | {'Job':<6} | {'Freq':<6} | {'Segments (Opt/Total)'}")
        print("-" * 75)
        
        for i, t in enumerate(tasks):
            for j in range(t['num_jobs']):
                for k in range(len(t['e_o_k']) + 1):
                    for z, f in enumerate(frequencies):
                        if X[i, j, k, z].X > 0.5:
                            print(f"T{i:<7} | P{task_proc[i]:<5} | J{j:<5} | {f:<6.2f} | {k} / {len(t['e_o_k'])}")
    else:
        print("Optimization failed (check feasibility or energy budget).")

if __name__ == "__main__":
    solve_usrt_btp()