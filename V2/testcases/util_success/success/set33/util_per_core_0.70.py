"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439984, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439984, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.084337, 'e_o_k': [0.010369, 0.008295, 0.006636], 'p_i': 10, 'u_i': 4.1859},
        {'id': 1, 'e_m': 6.384089, 'e_o_k': [0.784929, 0.627943, 0.502355], 'p_i': 20, 'u_i': 1.3758},
        {'id': 2, 'e_m': 9.821378, 'e_o_k': [1.207546, 0.966037, 0.772830], 'p_i': 40, 'u_i': 3.6848},
        {'id': 3, 'e_m': 1.685677, 'e_o_k': [0.280946, 0.224757], 'p_i': 80, 'u_i': 1.6851},
        {'id': 4, 'e_m': 9.526039, 'e_o_k': [0.850134, 0.680107, 0.544086, 0.435269, 0.348215], 'p_i': 20, 'u_i': 1.3700},
        {'id': 5, 'e_m': 2.384584, 'e_o_k': [0.212808, 0.170246, 0.136197, 0.108958, 0.087166], 'p_i': 10, 'u_i': 3.3252},
        {'id': 6, 'e_m': 2.145357, 'e_o_k': [0.357560, 0.286048], 'p_i': 80, 'u_i': 4.3008},
        {'id': 7, 'e_m': 5.134329, 'e_o_k': [0.521781, 0.417425, 0.333940, 0.267152], 'p_i': 80, 'u_i': 2.2362},
    ]
    B_BUDGET = 167.439984
    return processors, tasks, B_BUDGET
