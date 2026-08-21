"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.527400, 'e_o_k': [0.200137, 0.160109, 0.128087, 0.102470, 0.081976, 0.065581], 'p_i': 10, 'u_i': 3.5665},
        {'id': 1, 'e_m': 4.435332, 'e_o_k': [2.103477, 1.682782, 1.346226, 1.076980], 'p_i': 20, 'u_i': 1.8299},
        {'id': 2, 'e_m': 12.827845, 'e_o_k': [9.977213, 7.981770], 'p_i': 40, 'u_i': 2.7998},
        {'id': 3, 'e_m': 16.383782, 'e_o_k': [12.742942, 10.194353], 'p_i': 80, 'u_i': 4.4830},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET
