"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199991, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199991, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.503086, 'e_o_k': [0.254588, 0.203670, 0.162936, 0.130349], 'p_i': 10, 'u_i': 1.9112},
        {'id': 1, 'e_m': 0.915545, 'e_o_k': [0.136177, 0.108942, 0.087153, 0.069723, 0.055778], 'p_i': 20, 'u_i': 4.0850},
        {'id': 2, 'e_m': 0.749753, 'e_o_k': [0.126991, 0.101593, 0.081274, 0.065019], 'p_i': 40, 'u_i': 1.7025},
        {'id': 3, 'e_m': 11.481254, 'e_o_k': [1.707707, 1.366165, 1.092932, 0.874346, 0.699477], 'p_i': 80, 'u_i': 2.0058},
        {'id': 4, 'e_m': 0.208788, 'e_o_k': [0.057997, 0.046397], 'p_i': 10, 'u_i': 3.5722},
        {'id': 5, 'e_m': 1.662061, 'e_o_k': [0.281514, 0.225212, 0.180169, 0.144135], 'p_i': 80, 'u_i': 1.2384},
    ]
    B_BUDGET = 55.199991
    return processors, tasks, B_BUDGET
