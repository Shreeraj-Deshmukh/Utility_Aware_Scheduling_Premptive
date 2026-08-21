"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.042066, 'e_o_k': [0.213538, 0.170831, 0.136664], 'p_i': 10, 'u_i': 2.9415},
        {'id': 1, 'e_m': 2.975949, 'e_o_k': [0.826653, 0.661322], 'p_i': 20, 'u_i': 4.1135},
        {'id': 2, 'e_m': 1.326184, 'e_o_k': [0.179735, 0.143788, 0.115030, 0.092024, 0.073619, 0.058896], 'p_i': 40, 'u_i': 3.4980},
        {'id': 3, 'e_m': 9.107305, 'e_o_k': [2.529807, 2.023846], 'p_i': 80, 'u_i': 2.1751},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
