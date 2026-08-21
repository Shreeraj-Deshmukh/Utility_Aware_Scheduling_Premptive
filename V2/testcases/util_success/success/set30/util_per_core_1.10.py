"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119998, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119998, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.870411, 'e_o_k': [0.291708, 0.233367, 0.186693, 0.149355], 'p_i': 10, 'u_i': 2.5324},
        {'id': 1, 'e_m': 0.877274, 'e_o_k': [0.107862, 0.086289, 0.069031], 'p_i': 20, 'u_i': 3.3287},
        {'id': 2, 'e_m': 9.118220, 'e_o_k': [0.741463, 0.593171, 0.474537, 0.379629, 0.303703, 0.242963], 'p_i': 40, 'u_i': 1.7649},
        {'id': 3, 'e_m': 29.248147, 'e_o_k': [2.378362, 1.902690, 1.522152, 1.217721, 0.974177, 0.779342], 'p_i': 80, 'u_i': 3.8145},
        {'id': 4, 'e_m': 27.828615, 'e_o_k': [4.638102, 3.710482], 'p_i': 80, 'u_i': 2.1873},
        {'id': 5, 'e_m': 16.025312, 'e_o_k': [1.970325, 1.576260, 1.261008], 'p_i': 40, 'u_i': 4.4760},
        {'id': 6, 'e_m': 13.765642, 'e_o_k': [1.228490, 0.982792, 0.786234, 0.628987, 0.503190], 'p_i': 40, 'u_i': 3.2202},
        {'id': 7, 'e_m': 14.632508, 'e_o_k': [1.305852, 1.044682, 0.835745, 0.668596, 0.534877], 'p_i': 80, 'u_i': 3.5239},
    ]
    B_BUDGET = 263.119998
    return processors, tasks, B_BUDGET
