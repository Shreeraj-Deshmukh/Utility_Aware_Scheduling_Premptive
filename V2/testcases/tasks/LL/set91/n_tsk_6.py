"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.20002, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.20002, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.740066, 'e_o_k': [0.100300, 0.080240, 0.064192, 0.051353, 0.041083, 0.032866], 'p_i': 10, 'u_i': 3.3094},
        {'id': 1, 'e_m': 0.275284, 'e_o_k': [0.056411, 0.045129, 0.036103], 'p_i': 20, 'u_i': 3.8452},
        {'id': 2, 'e_m': 8.389668, 'e_o_k': [1.137033, 0.909627, 0.727701, 0.582161, 0.465729, 0.372583], 'p_i': 40, 'u_i': 1.8919},
        {'id': 3, 'e_m': 3.924716, 'e_o_k': [0.531908, 0.425527, 0.340421, 0.272337, 0.217870, 0.174296], 'p_i': 80, 'u_i': 3.0558},
        {'id': 4, 'e_m': 0.092102, 'e_o_k': [0.015600, 0.012480, 0.009984, 0.007987], 'p_i': 10, 'u_i': 1.4898},
        {'id': 5, 'e_m': 1.768735, 'e_o_k': [0.299583, 0.239666, 0.191733, 0.153386], 'p_i': 40, 'u_i': 1.5566},
    ]
    B_BUDGET = 55.200020
    return processors, tasks, B_BUDGET
