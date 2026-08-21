"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639992, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639992, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.346256, 'e_o_k': [0.977141, 0.781713, 0.625371, 0.500296, 0.400237], 'p_i': 10, 'u_i': 1.5213},
        {'id': 1, 'e_m': 3.572738, 'e_o_k': [2.049932, 1.639946, 1.311956], 'p_i': 20, 'u_i': 2.4569},
        {'id': 2, 'e_m': 7.198209, 'e_o_k': [2.997826, 2.398261, 1.918609, 1.534887, 1.227910], 'p_i': 40, 'u_i': 4.9222},
        {'id': 3, 'e_m': 16.542579, 'e_o_k': [7.845396, 6.276317, 5.021054, 4.016843], 'p_i': 80, 'u_i': 1.9107},
    ]
    B_BUDGET = 176.639992
    return processors, tasks, B_BUDGET
