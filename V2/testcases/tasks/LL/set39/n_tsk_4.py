"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.489567, 'e_o_k': [0.135991, 0.108793], 'p_i': 10, 'u_i': 1.9313},
        {'id': 1, 'e_m': 3.987962, 'e_o_k': [0.593164, 0.474531, 0.379625, 0.303700, 0.242960], 'p_i': 20, 'u_i': 4.6903},
        {'id': 2, 'e_m': 1.905685, 'e_o_k': [0.390509, 0.312407, 0.249926], 'p_i': 40, 'u_i': 4.0696},
        {'id': 3, 'e_m': 8.320245, 'e_o_k': [2.311179, 1.848943], 'p_i': 80, 'u_i': 1.5844},
    ]
    B_BUDGET = 55.199997
    return processors, tasks, B_BUDGET
