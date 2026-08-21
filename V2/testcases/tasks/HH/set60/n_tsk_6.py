"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640006, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640006, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.962087, 'e_o_k': [1.526067, 1.220854], 'p_i': 10, 'u_i': 2.4321},
        {'id': 1, 'e_m': 7.737294, 'e_o_k': [2.936132, 2.348905, 1.879124, 1.503299, 1.202639, 0.962112], 'p_i': 20, 'u_i': 1.0700},
        {'id': 2, 'e_m': 1.138036, 'e_o_k': [0.652971, 0.522377, 0.417902], 'p_i': 40, 'u_i': 3.1686},
        {'id': 3, 'e_m': 9.481208, 'e_o_k': [5.440037, 4.352030, 3.481624], 'p_i': 80, 'u_i': 1.4833},
        {'id': 4, 'e_m': 0.197047, 'e_o_k': [0.074775, 0.059820, 0.047856, 0.038285, 0.030628, 0.024502], 'p_i': 20, 'u_i': 1.9048},
        {'id': 5, 'e_m': 2.404333, 'e_o_k': [1.870037, 1.496029], 'p_i': 40, 'u_i': 4.4078},
    ]
    B_BUDGET = 176.640006
    return processors, tasks, B_BUDGET
