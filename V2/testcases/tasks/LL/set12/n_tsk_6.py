"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199993, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199993, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.779187, 'e_o_k': [0.159669, 0.127735, 0.102188], 'p_i': 10, 'u_i': 2.7610},
        {'id': 1, 'e_m': 2.467882, 'e_o_k': [0.685523, 0.548418], 'p_i': 20, 'u_i': 2.5980},
        {'id': 2, 'e_m': 3.236858, 'e_o_k': [0.899127, 0.719302], 'p_i': 40, 'u_i': 2.9083},
        {'id': 3, 'e_m': 7.795435, 'e_o_k': [1.597425, 1.277940, 1.022352], 'p_i': 80, 'u_i': 4.8275},
        {'id': 4, 'e_m': 1.208982, 'e_o_k': [0.179822, 0.143858, 0.115086, 0.092069, 0.073655], 'p_i': 80, 'u_i': 3.8825},
        {'id': 5, 'e_m': 0.104212, 'e_o_k': [0.021355, 0.017084, 0.013667], 'p_i': 20, 'u_i': 1.8333},
    ]
    B_BUDGET = 55.199993
    return processors, tasks, B_BUDGET
