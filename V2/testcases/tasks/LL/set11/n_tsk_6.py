"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.726786, 'e_o_k': [0.148931, 0.119145, 0.095316], 'p_i': 10, 'u_i': 1.4749},
        {'id': 1, 'e_m': 3.804665, 'e_o_k': [0.644422, 0.515537, 0.412430, 0.329944], 'p_i': 20, 'u_i': 4.2682},
        {'id': 2, 'e_m': 2.401938, 'e_o_k': [0.357261, 0.285809, 0.228647, 0.182918, 0.146334], 'p_i': 40, 'u_i': 4.6830},
        {'id': 3, 'e_m': 2.065129, 'e_o_k': [0.573647, 0.458918], 'p_i': 80, 'u_i': 2.4027},
        {'id': 4, 'e_m': 0.885724, 'e_o_k': [0.246034, 0.196828], 'p_i': 80, 'u_i': 2.7203},
        {'id': 5, 'e_m': 1.606163, 'e_o_k': [0.217680, 0.174144, 0.139315, 0.111452, 0.089162, 0.071329], 'p_i': 40, 'u_i': 2.4000},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
