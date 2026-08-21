"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.283614, 'e_o_k': [0.866581, 0.693265, 0.554612, 0.443689, 0.354952, 0.283961], 'p_i': 10, 'u_i': 1.6837},
        {'id': 1, 'e_m': 4.288893, 'e_o_k': [3.335806, 2.668645], 'p_i': 20, 'u_i': 2.3942},
        {'id': 2, 'e_m': 9.305656, 'e_o_k': [3.875511, 3.100409, 2.480327, 1.984262, 1.587409], 'p_i': 40, 'u_i': 1.1399},
        {'id': 3, 'e_m': 9.964201, 'e_o_k': [3.781193, 3.024955, 2.419964, 1.935971, 1.548777, 1.239021], 'p_i': 80, 'u_i': 4.6324},
    ]
    B_BUDGET = 176.639998
    return processors, tasks, B_BUDGET
