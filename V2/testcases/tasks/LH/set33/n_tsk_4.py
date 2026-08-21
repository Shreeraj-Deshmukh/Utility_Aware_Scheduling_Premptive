"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.055999, 'e_o_k': [0.043555, 0.034844], 'p_i': 10, 'u_i': 3.5447},
        {'id': 1, 'e_m': 4.278233, 'e_o_k': [2.454724, 1.963779, 1.571023], 'p_i': 20, 'u_i': 1.0370},
        {'id': 2, 'e_m': 5.252208, 'e_o_k': [2.187379, 1.749903, 1.399922, 1.119938, 0.895950], 'p_i': 40, 'u_i': 1.6130},
        {'id': 3, 'e_m': 3.934656, 'e_o_k': [2.257590, 1.806072, 1.444857], 'p_i': 80, 'u_i': 1.3758},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET
