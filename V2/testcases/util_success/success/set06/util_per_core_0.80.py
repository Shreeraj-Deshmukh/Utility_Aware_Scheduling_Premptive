"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359994, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359994, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.435178, 'e_o_k': [0.239196, 0.191357], 'p_i': 10, 'u_i': 2.0470},
        {'id': 1, 'e_m': 1.285167, 'e_o_k': [0.130606, 0.104485, 0.083588, 0.066870], 'p_i': 20, 'u_i': 4.9556},
        {'id': 2, 'e_m': 11.658534, 'e_o_k': [1.943089, 1.554471], 'p_i': 40, 'u_i': 1.3741},
        {'id': 3, 'e_m': 33.154642, 'e_o_k': [2.958827, 2.367062, 1.893649, 1.514919, 1.211936], 'p_i': 80, 'u_i': 4.6107},
        {'id': 4, 'e_m': 16.114287, 'e_o_k': [1.438091, 1.150473, 0.920378, 0.736302, 0.589042], 'p_i': 40, 'u_i': 2.5105},
        {'id': 5, 'e_m': 0.186862, 'e_o_k': [0.018990, 0.015192, 0.012154, 0.009723], 'p_i': 10, 'u_i': 2.2972},
        {'id': 6, 'e_m': 7.334539, 'e_o_k': [1.222423, 0.977939], 'p_i': 40, 'u_i': 3.0996},
        {'id': 7, 'e_m': 0.814206, 'e_o_k': [0.072662, 0.058130, 0.046504, 0.037203, 0.029763], 'p_i': 10, 'u_i': 4.5299},
    ]
    B_BUDGET = 191.359994
    return processors, tasks, B_BUDGET
