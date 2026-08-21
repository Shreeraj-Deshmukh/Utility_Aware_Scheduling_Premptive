"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.111998, 'e_o_k': [0.031111, 0.024889], 'p_i': 10, 'u_i': 3.5447},
        {'id': 1, 'e_m': 8.556467, 'e_o_k': [1.753374, 1.402699, 1.122160], 'p_i': 20, 'u_i': 1.0370},
        {'id': 2, 'e_m': 10.504417, 'e_o_k': [1.562413, 1.249931, 0.999944, 0.799956, 0.639964], 'p_i': 40, 'u_i': 1.6130},
        {'id': 3, 'e_m': 7.869313, 'e_o_k': [1.612564, 1.290051, 1.032041], 'p_i': 80, 'u_i': 1.3758},
    ]
    B_BUDGET = 110.400003
    return processors, tasks, B_BUDGET
