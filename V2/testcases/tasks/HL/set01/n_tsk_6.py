"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.355596, 'e_o_k': [0.052891, 0.042313, 0.033850, 0.027080, 0.021664], 'p_i': 10, 'u_i': 3.8879},
        {'id': 1, 'e_m': 7.765711, 'e_o_k': [1.052470, 0.841976, 0.673581, 0.538865, 0.431092, 0.344873], 'p_i': 20, 'u_i': 3.5961},
        {'id': 2, 'e_m': 1.313886, 'e_o_k': [0.195426, 0.156341, 0.125072, 0.100058, 0.080046], 'p_i': 40, 'u_i': 4.1247},
        {'id': 3, 'e_m': 1.954973, 'e_o_k': [0.400609, 0.320487, 0.256390], 'p_i': 80, 'u_i': 3.4312},
        {'id': 4, 'e_m': 23.181270, 'e_o_k': [6.439242, 5.151393], 'p_i': 80, 'u_i': 1.1226},
        {'id': 5, 'e_m': 0.582092, 'e_o_k': [0.086580, 0.069264, 0.055411, 0.044329, 0.035463], 'p_i': 20, 'u_i': 3.8598},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET
