"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 41, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 41, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.460174, 'e_o_k': [0.554104, 0.443283, 0.354626, 0.283701, 0.226961, 0.181569], 'p_i': 10, 'u_i': 3.0712},
        {'id': 1, 'e_m': 0.417207, 'e_o_k': [0.239381, 0.191505, 0.153204], 'p_i': 20, 'u_i': 2.2314},
        {'id': 2, 'e_m': 2.317386, 'e_o_k': [0.965118, 0.772094, 0.617676, 0.494140, 0.395312], 'p_i': 40, 'u_i': 3.7246},
        {'id': 3, 'e_m': 0.317304, 'e_o_k': [0.182060, 0.145648, 0.116518], 'p_i': 80, 'u_i': 2.2417},
        {'id': 4, 'e_m': 1.728593, 'e_o_k': [0.719904, 0.575923, 0.460739, 0.368591, 0.294873], 'p_i': 40, 'u_i': 3.2729},
        {'id': 5, 'e_m': 0.210554, 'e_o_k': [0.099856, 0.079885, 0.063908, 0.051126], 'p_i': 10, 'u_i': 4.3402},
        {'id': 6, 'e_m': 0.207004, 'e_o_k': [0.098173, 0.078538, 0.062830, 0.050264], 'p_i': 10, 'u_i': 2.8458},
        {'id': 7, 'e_m': 0.862507, 'e_o_k': [0.670839, 0.536671], 'p_i': 10, 'u_i': 4.3327},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
