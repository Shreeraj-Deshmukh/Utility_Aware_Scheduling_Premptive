"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32002, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.32002, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.740066, 'e_o_k': [0.280839, 0.224671, 0.179737, 0.143789, 0.115032, 0.092025], 'p_i': 10, 'u_i': 3.3094},
        {'id': 1, 'e_m': 0.275284, 'e_o_k': [0.157950, 0.126360, 0.101088], 'p_i': 20, 'u_i': 3.8452},
        {'id': 2, 'e_m': 8.389668, 'e_o_k': [3.183693, 2.546954, 2.037564, 1.630051, 1.304041, 1.043233], 'p_i': 40, 'u_i': 1.8919},
        {'id': 3, 'e_m': 3.924716, 'e_o_k': [1.489343, 1.191474, 0.953179, 0.762544, 0.610035, 0.488028], 'p_i': 80, 'u_i': 3.0558},
        {'id': 4, 'e_m': 0.092102, 'e_o_k': [0.043680, 0.034944, 0.027955, 0.022364], 'p_i': 10, 'u_i': 1.4898},
        {'id': 5, 'e_m': 1.768735, 'e_o_k': [0.838831, 0.671065, 0.536852, 0.429482], 'p_i': 40, 'u_i': 1.5566},
    ]
    B_BUDGET = 88.320020
    return processors, tasks, B_BUDGET
