"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679993, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679993, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.920347, 'e_o_k': [0.237473, 0.189978, 0.151983, 0.121586, 0.097269, 0.077815], 'p_i': 10, 'u_i': 3.0949},
        {'id': 1, 'e_m': 0.834414, 'e_o_k': [0.102592, 0.082073, 0.065659], 'p_i': 20, 'u_i': 1.9752},
        {'id': 2, 'e_m': 4.634773, 'e_o_k': [0.413622, 0.330898, 0.264718, 0.211774, 0.169420], 'p_i': 40, 'u_i': 3.9662},
        {'id': 3, 'e_m': 0.634609, 'e_o_k': [0.078026, 0.062421, 0.049936], 'p_i': 80, 'u_i': 1.9890},
        {'id': 4, 'e_m': 3.457185, 'e_o_k': [0.308530, 0.246824, 0.197459, 0.157968, 0.126374], 'p_i': 40, 'u_i': 3.3639},
        {'id': 5, 'e_m': 0.421109, 'e_o_k': [0.042796, 0.034236, 0.027389, 0.021911], 'p_i': 10, 'u_i': 4.7869},
        {'id': 6, 'e_m': 0.414008, 'e_o_k': [0.042074, 0.033659, 0.026927, 0.021542], 'p_i': 10, 'u_i': 2.7944},
        {'id': 7, 'e_m': 1.725014, 'e_o_k': [0.287502, 0.230002], 'p_i': 10, 'u_i': 4.7769},
    ]
    B_BUDGET = 95.679993
    return processors, tasks, B_BUDGET
