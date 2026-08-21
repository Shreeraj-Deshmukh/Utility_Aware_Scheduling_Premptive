"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.879937, 'e_o_k': [0.244427, 0.195542], 'p_i': 10, 'u_i': 3.3070},
        {'id': 1, 'e_m': 2.830555, 'e_o_k': [0.421013, 0.336810, 0.269448, 0.215559, 0.172447], 'p_i': 20, 'u_i': 4.6500},
        {'id': 2, 'e_m': 3.400783, 'e_o_k': [0.576013, 0.460811, 0.368649, 0.294919], 'p_i': 40, 'u_i': 2.3899},
        {'id': 3, 'e_m': 6.836715, 'e_o_k': [1.400966, 1.120773, 0.896618], 'p_i': 80, 'u_i': 1.6802},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
