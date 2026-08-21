"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319993, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319993, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.363511, 'e_o_k': [0.567859, 0.454287, 0.363430, 0.290744, 0.232595], 'p_i': 10, 'u_i': 4.2653},
        {'id': 1, 'e_m': 0.224102, 'e_o_k': [0.085042, 0.068033, 0.054427, 0.043541, 0.034833, 0.027866], 'p_i': 20, 'u_i': 3.8195},
        {'id': 2, 'e_m': 8.637417, 'e_o_k': [3.277708, 2.622167, 2.097733, 1.678187, 1.342549, 1.074039], 'p_i': 40, 'u_i': 1.2105},
        {'id': 3, 'e_m': 0.668357, 'e_o_k': [0.383483, 0.306787, 0.245429], 'p_i': 80, 'u_i': 1.7971},
        {'id': 4, 'e_m': 0.183998, 'e_o_k': [0.105573, 0.084458, 0.067567], 'p_i': 20, 'u_i': 3.9776},
        {'id': 5, 'e_m': 0.758160, 'e_o_k': [0.315750, 0.252600, 0.202080, 0.161664, 0.129331], 'p_i': 40, 'u_i': 2.5595},
    ]
    B_BUDGET = 88.319993
    return processors, tasks, B_BUDGET
