"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640011, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640011, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.325171, 'e_o_k': [0.882351, 0.705881, 0.564705, 0.451764, 0.361411, 0.289129], 'p_i': 10, 'u_i': 2.0153},
        {'id': 1, 'e_m': 9.308795, 'e_o_k': [3.876819, 3.101455, 2.481164, 1.984931, 1.587945], 'p_i': 20, 'u_i': 4.1190},
        {'id': 2, 'e_m': 1.500088, 'e_o_k': [0.860706, 0.688565, 0.550852], 'p_i': 40, 'u_i': 4.7975},
        {'id': 3, 'e_m': 5.163273, 'e_o_k': [1.959348, 1.567478, 1.253983, 1.003186, 0.802549, 0.642039], 'p_i': 80, 'u_i': 4.0424},
    ]
    B_BUDGET = 176.640011
    return processors, tasks, B_BUDGET
