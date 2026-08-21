"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520016, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520016, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.727447, 'e_o_k': [0.064920, 0.051936, 0.041549, 0.033239, 0.026591], 'p_i': 10, 'u_i': 1.7042},
        {'id': 1, 'e_m': 1.104960, 'e_o_k': [0.135856, 0.108685, 0.086948], 'p_i': 20, 'u_i': 4.3788},
        {'id': 2, 'e_m': 6.851423, 'e_o_k': [0.696283, 0.557026, 0.445621, 0.356497], 'p_i': 40, 'u_i': 3.2500},
        {'id': 3, 'e_m': 3.885724, 'e_o_k': [0.647621, 0.518097], 'p_i': 80, 'u_i': 3.9101},
        {'id': 4, 'e_m': 1.794540, 'e_o_k': [0.182372, 0.145898, 0.116718, 0.093374], 'p_i': 80, 'u_i': 2.7187},
        {'id': 5, 'e_m': 8.466351, 'e_o_k': [0.688456, 0.550764, 0.440612, 0.352489, 0.281991, 0.225593], 'p_i': 40, 'u_i': 3.8755},
        {'id': 6, 'e_m': 38.993829, 'e_o_k': [4.794323, 3.835459, 3.068367], 'p_i': 80, 'u_i': 3.4836},
        {'id': 7, 'e_m': 5.225472, 'e_o_k': [0.642476, 0.513981, 0.411185], 'p_i': 40, 'u_i': 4.1699},
    ]
    B_BUDGET = 143.520016
    return processors, tasks, B_BUDGET
