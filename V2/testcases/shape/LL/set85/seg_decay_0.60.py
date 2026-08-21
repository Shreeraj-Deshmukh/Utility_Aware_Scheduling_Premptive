"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199987, "H": 80, "J": 37, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.199987, "H": 80, "J": 37, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.244220, 'e_o_k': [0.076319, 0.045791], 'p_i': 10, 'u_i': 1.2408},
        {'id': 1, 'e_m': 0.462328, 'e_o_k': [0.106233, 0.063740, 0.038244, 0.022946], 'p_i': 20, 'u_i': 2.7274},
        {'id': 2, 'e_m': 1.144163, 'e_o_k': [0.248127, 0.148876, 0.089326, 0.053595, 0.032157], 'p_i': 40, 'u_i': 3.7398},
        {'id': 3, 'e_m': 2.328605, 'e_o_k': [0.594032, 0.356419, 0.213851], 'p_i': 80, 'u_i': 1.4758},
        {'id': 4, 'e_m': 0.072384, 'e_o_k': [0.015185, 0.009111, 0.005467, 0.003280, 0.001968, 0.001181], 'p_i': 10, 'u_i': 1.9890},
        {'id': 5, 'e_m': 0.070477, 'e_o_k': [0.017979, 0.010787, 0.006472], 'p_i': 40, 'u_i': 1.7667},
        {'id': 6, 'e_m': 2.462336, 'e_o_k': [0.628147, 0.376888, 0.226133], 'p_i': 20, 'u_i': 2.7743},
        {'id': 7, 'e_m': 1.626328, 'e_o_k': [0.373697, 0.224218, 0.134531, 0.080718], 'p_i': 10, 'u_i': 3.3191},
    ]
    B_BUDGET = 55.199987
    return processors, tasks, B_BUDGET
