"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.322098, 'e_o_k': [0.054556, 0.043645, 0.034916, 0.027933], 'p_i': 10, 'u_i': 1.2518},
        {'id': 1, 'e_m': 1.335603, 'e_o_k': [0.273689, 0.218951, 0.175161], 'p_i': 20, 'u_i': 3.1387},
        {'id': 2, 'e_m': 10.846720, 'e_o_k': [1.613327, 1.290662, 1.032529, 0.826023, 0.660819], 'p_i': 40, 'u_i': 1.5213},
        {'id': 3, 'e_m': 2.387361, 'e_o_k': [0.489213, 0.391371, 0.313097], 'p_i': 80, 'u_i': 2.4569},
    ]
    B_BUDGET = 55.200002
    return processors, tasks, B_BUDGET
