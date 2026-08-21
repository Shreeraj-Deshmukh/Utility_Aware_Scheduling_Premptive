"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120002, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120002, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.208313, 'e_o_k': [0.098256, 0.078605, 0.062884, 0.050307, 0.040246, 0.032197], 'p_i': 10, 'u_i': 3.3901},
        {'id': 1, 'e_m': 9.298358, 'e_o_k': [0.756112, 0.604889, 0.483911, 0.387129, 0.309703, 0.247763], 'p_i': 20, 'u_i': 2.3217},
        {'id': 2, 'e_m': 12.378044, 'e_o_k': [1.257931, 1.006345, 0.805076, 0.644061], 'p_i': 40, 'u_i': 2.1118},
        {'id': 3, 'e_m': 3.565849, 'e_o_k': [0.362383, 0.289906, 0.231925, 0.185540], 'p_i': 80, 'u_i': 4.2305},
        {'id': 4, 'e_m': 39.979335, 'e_o_k': [6.663223, 5.330578], 'p_i': 80, 'u_i': 2.0791},
        {'id': 5, 'e_m': 21.857593, 'e_o_k': [3.642932, 2.914346], 'p_i': 80, 'u_i': 1.4810},
        {'id': 6, 'e_m': 19.899325, 'e_o_k': [3.316554, 2.653243], 'p_i': 80, 'u_i': 3.5439},
        {'id': 7, 'e_m': 2.385234, 'e_o_k': [0.193959, 0.155167, 0.124134, 0.099307, 0.079446, 0.063557], 'p_i': 10, 'u_i': 4.1958},
    ]
    B_BUDGET = 263.120002
    return processors, tasks, B_BUDGET
