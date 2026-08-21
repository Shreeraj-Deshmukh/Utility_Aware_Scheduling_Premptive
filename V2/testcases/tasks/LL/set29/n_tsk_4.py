"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.617973, 'e_o_k': [0.083753, 0.067002, 0.053602, 0.042881, 0.034305, 0.027444], 'p_i': 10, 'u_i': 3.2393},
        {'id': 1, 'e_m': 1.095309, 'e_o_k': [0.148445, 0.118756, 0.095005, 0.076004, 0.060803, 0.048642], 'p_i': 20, 'u_i': 4.1852},
        {'id': 2, 'e_m': 5.386398, 'e_o_k': [0.912330, 0.729864, 0.583891, 0.467113], 'p_i': 40, 'u_i': 4.0538},
        {'id': 3, 'e_m': 11.902184, 'e_o_k': [2.015953, 1.612762, 1.290210, 1.032168], 'p_i': 80, 'u_i': 4.3622},
    ]
    B_BUDGET = 55.200006
    return processors, tasks, B_BUDGET
