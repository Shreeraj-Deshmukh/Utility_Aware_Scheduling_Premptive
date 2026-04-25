# Gurobi USRT BTP ILP Formulation brute-force optimal solution for small instances (Section IV-B)

import gurobipy as gp
from gurobipy import GRB
import math
from testcase import testcase 

def solve_usrt_btp():
    # 1. LOAD DATA & SYSTEM CONSTANTS
    # get processor , tasks and B from testcase file
    processors, tasks, B_BUDGET = testcase()
    alpha, beta = 1.0, 1.0 # Energy model constants 
    
    model = gp.Model("USRT_Full_ILP")
    model.Params.OutputFlag = 0

    # 2. PREPROCESSING: Hyper-period and Job Calculation
    # Calculated as h = lcm{pi} 
    periods = [t['p_i'] for t in tasks]
    hyper_period = periods[0]
    for p in periods[1:]:
        hyper_period = (hyper_period * p) // math.gcd(hyper_period, p)
    # getting number of jobs as Nj = H/Pi
    for t in tasks:
        t['num_jobs'] = hyper_period // t['p_i'] # Ni_job = h / pi 

    num_processors = len(processors)
    num_tasks = len(tasks)
    frequencies = processors[0]['frequencies'] # Discrete set F = {fz} 

    # 3. DECISION VARIABLES
    # V(ix): Binary variable: 1 if task Ti is on processor Px
    V = model.addVars(num_tasks, num_processors, vtype=GRB.BINARY, name="V")
    
    # X(ijkz): Binary variable: 1 if job Ti,j executes frequency fz up to k segments 
    X = {}
    for i, t in enumerate(tasks):
        num_segments = len(t['e_o_k'])
        for j in range(t['num_jobs']):
            for k in range(num_segments + 1): 
                for z, f in enumerate(frequencies):
                    X[i, j, k, z] = model.addVar(vtype=GRB.BINARY, name=f"X_{i}_{j}_{k}_{z}")

    # A(ijkxz): Auxiliary linearized variable A = V(ix) * X(ijkz) [cite: 86, 87]
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

    # C2: Job must execute with exactly one frequency and segment level
    for i, t in enumerate(tasks):
        num_segments = len(t['e_o_k'])
        for j in range(t['num_jobs']):
            model.addConstr(gp.quicksum(X[i, j, k, z] for k in range(num_segments + 1) 
                                       for z in range(len(frequencies))) == 1)
            
            for k in range(num_segments + 1):
                # Effective execution time with segments
                total_exec_fmax = t['e_m'] + sum(t['e_o_k'][:k]) 
                for z, f in enumerate(frequencies):
                    # Objective: Maximize total weighted utility
                    if k > 0:
                        obj += t['u_i'] * sum(t['e_o_k'][:k]) * X[i, j, k, z]
                    
                    # Energy Model 
                    e_eff = total_exec_fmax / f 
                    energy_val = alpha * e_eff + beta * (f**2) * total_exec_fmax
                    total_energy += energy_val * X[i, j, k, z] 
                    
                    # Linearization for the Auxiliary Variable A 
                    for x in range(num_processors):
                        model.addConstr(A[i, j, k, z, x] <= V[i, x])
                        model.addConstr(A[i, j, k, z, x] <= X[i, j, k, z])
                        model.addConstr(A[i, j, k, z, x] >= V[i, x] + X[i, j, k, z] - 1)

    # Set Maximize Utility Objective 
    model.setObjective(obj, GRB.MAXIMIZE) 
    
    # C1: Task-to-Processor Mapping (exactly one processor) 
    for i in range(num_tasks):
        model.addConstr(V.sum(i, '*') == 1) 
        
    # C4: Total Energy <= Budget B 
    model.addConstr(total_energy <= B_BUDGET)

    # C3: Timing Constraint using Demand Bound Function (DBF) for EDF [cite: 72, 92, 95, 101]
    # Arrivals (R) and Deadlines (D) for all jobs in hyper-period [cite: 93, 97]
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
                            # Job belongs to interval [t1, t2] [cite: 93]
                            if (j * t['p_i'] >= t1) and ((j+1) * t['p_i'] <= t2):
                                has_jobs = True
                                for k in range(len(t['e_o_k']) + 1):
                                    for z, f in enumerate(frequencies):
                                        # dbf calculation [cite: 95]
                                        e_eff = (t['e_m'] + sum(t['e_o_k'][:k])) / f
                                        demand += e_eff * A[i, j, k, z, x]
                    if has_jobs:
                        # dbf(t1, t2) <= t2 - t1 [cite: 101]
                        model.addConstr(demand <= (t2 - t1))

    model.optimize()
    
    # 5. OUTPUT GENERATION (Hyper-period Schedule)
    if model.status == GRB.OPTIMAL:
        print(f"\n{'='*105}")
        print(f"USRT SCHEDULE (Hyper-period: {hyper_period})")
        print(f"Total Utility: {model.objVal:.2f} | Total Energy: {total_energy.getValue():.2f}/{B_BUDGET}")
        print(f"{'='*105}")
        print(f"{'Start':<8} | {'End':<8} | {'Task':<6} | {'Core':<5} | {'Job':<5} | {'Freq':<6} | {'Segments':<10} | {'Energy':<10}")
        print("-" * 105)

        full_schedule = []
        for x in range(num_processors):
            core_jobs = []
            for i, t in enumerate(tasks):
                if V[i, x].X > 0.5:
                    for j in range(t['num_jobs']):
                        for k in range(len(t['e_o_k']) + 1):
                            for z, f in enumerate(frequencies):
                                if X[i, j, k, z].X > 0.5:
                                    total_exec_fmax = t['e_m'] + sum(t['e_o_k'][:k])
                                    e_eff = total_exec_fmax / f
                                    energy = alpha * e_eff + beta * (f**2) * total_exec_fmax
                                    
                                    core_jobs.append({
                                        'release': j * t['p_i'],
                                        'deadline': (j + 1) * t['p_i'],
                                        'e_eff': e_eff,
                                        'task': i, 'job': j, 'freq': f, 'k': k, 'seg_total': len(t['e_o_k']),
                                        'core': x, 'energy': energy
                                    })
            
            # Sort by deadline to follow EDF per processor [cite: 49, 72]
            core_jobs.sort(key=lambda x: x['deadline'])
            
            proc_time = 0
            for cj in core_jobs:
                start_time = max(proc_time, cj['release'])
                end_time = start_time + cj['e_eff']
                cj['start'] = round(start_time, 2)
                cj['end'] = round(end_time, 2)
                proc_time = end_time
                full_schedule.append(cj)

        # Print chronological execution across all cores
        full_schedule.sort(key=lambda x: x['start'])
        for item in full_schedule:
            print(f"{item['start']:<8} | {item['end']:<8} | T{item['task']:<5} | P{item['core']:<4} | J{item['job']:<4} | {item['freq']:<6.2f} | {item['k']}/{item['seg_total']:<8} | {item['energy']:<10.2f}")
    else:
        print("Optimization failed. Status code:", model.status)

if __name__ == "__main__":
    solve_usrt_btp()
    