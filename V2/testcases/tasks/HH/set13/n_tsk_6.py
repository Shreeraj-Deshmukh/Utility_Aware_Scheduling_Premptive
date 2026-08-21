"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.157215, 'e_o_k': [0.065475, 0.052380, 0.041904, 0.033523, 0.026819], 'p_i': 10, 'u_i': 4.4619},
        {'id': 1, 'e_m': 1.013271, 'e_o_k': [0.788100, 0.630480], 'p_i': 20, 'u_i': 2.5387},
        {'id': 2, 'e_m': 3.436333, 'e_o_k': [1.629697, 1.303758, 1.043006, 0.834405], 'p_i': 40, 'u_i': 1.0056},
        {'id': 3, 'e_m': 7.676692, 'e_o_k': [3.640708, 2.912566, 2.330053, 1.864042], 'p_i': 80, 'u_i': 1.2987},
        {'id': 4, 'e_m': 1.838053, 'e_o_k': [0.765491, 0.612393, 0.489914, 0.391931, 0.313545], 'p_i': 20, 'u_i': 3.5939},
        {'id': 5, 'e_m': 4.598453, 'e_o_k': [3.576575, 2.861260], 'p_i': 10, 'u_i': 1.8409},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
