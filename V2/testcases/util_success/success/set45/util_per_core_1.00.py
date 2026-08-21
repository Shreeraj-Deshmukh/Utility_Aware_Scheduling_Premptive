"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199999, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199999, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.091875, 'e_o_k': [0.181979, 0.145583], 'p_i': 10, 'u_i': 2.8771},
        {'id': 1, 'e_m': 3.839537, 'e_o_k': [0.390197, 0.312157, 0.249726, 0.199781], 'p_i': 20, 'u_i': 3.3920},
        {'id': 2, 'e_m': 6.887948, 'e_o_k': [1.147991, 0.918393], 'p_i': 40, 'u_i': 1.7352},
        {'id': 3, 'e_m': 19.284596, 'e_o_k': [1.721019, 1.376816, 1.101452, 0.881162, 0.704930], 'p_i': 80, 'u_i': 3.3959},
        {'id': 4, 'e_m': 4.969547, 'e_o_k': [0.611010, 0.488808, 0.391046], 'p_i': 10, 'u_i': 3.3950},
        {'id': 5, 'e_m': 7.668920, 'e_o_k': [0.942900, 0.754320, 0.603456], 'p_i': 40, 'u_i': 1.1151},
        {'id': 6, 'e_m': 8.058201, 'e_o_k': [0.719140, 0.575312, 0.460249, 0.368200, 0.294560], 'p_i': 20, 'u_i': 2.3573},
        {'id': 7, 'e_m': 3.879835, 'e_o_k': [0.477029, 0.381623, 0.305299], 'p_i': 20, 'u_i': 2.0853},
    ]
    B_BUDGET = 239.199999
    return processors, tasks, B_BUDGET
