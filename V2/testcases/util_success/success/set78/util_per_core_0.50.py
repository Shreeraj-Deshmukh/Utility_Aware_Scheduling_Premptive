"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600005, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600005, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.858050, 'e_o_k': [0.290452, 0.232362, 0.185889, 0.148712], 'p_i': 10, 'u_i': 1.7025},
        {'id': 1, 'e_m': 1.804051, 'e_o_k': [0.160999, 0.128799, 0.103040, 0.082432, 0.065945], 'p_i': 20, 'u_i': 2.0058},
        {'id': 2, 'e_m': 1.403038, 'e_o_k': [0.233840, 0.187072], 'p_i': 40, 'u_i': 3.5722},
        {'id': 3, 'e_m': 24.767845, 'e_o_k': [2.517057, 2.013646, 1.610917, 1.288733], 'p_i': 80, 'u_i': 1.2384},
        {'id': 4, 'e_m': 2.312250, 'e_o_k': [0.385375, 0.308300], 'p_i': 40, 'u_i': 4.5379},
        {'id': 5, 'e_m': 3.278455, 'e_o_k': [0.546409, 0.437127], 'p_i': 20, 'u_i': 1.9982},
        {'id': 6, 'e_m': 0.381898, 'e_o_k': [0.063650, 0.050920], 'p_i': 20, 'u_i': 2.1252},
        {'id': 7, 'e_m': 3.079566, 'e_o_k': [0.312964, 0.250371, 0.200297, 0.160238], 'p_i': 80, 'u_i': 4.2384},
    ]
    B_BUDGET = 119.600005
    return processors, tasks, B_BUDGET
