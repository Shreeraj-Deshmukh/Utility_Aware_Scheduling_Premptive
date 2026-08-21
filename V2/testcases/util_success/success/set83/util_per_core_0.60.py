"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519995, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519995, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.360551, 'e_o_k': [0.210663, 0.168531, 0.134824, 0.107860, 0.086288], 'p_i': 10, 'u_i': 3.6650},
        {'id': 1, 'e_m': 2.233055, 'e_o_k': [0.181585, 0.145268, 0.116214, 0.092971, 0.074377, 0.059502], 'p_i': 20, 'u_i': 1.3163},
        {'id': 2, 'e_m': 1.704135, 'e_o_k': [0.173184, 0.138548, 0.110838, 0.088670], 'p_i': 40, 'u_i': 1.2768},
        {'id': 3, 'e_m': 20.629709, 'e_o_k': [2.536440, 2.029152, 1.623321], 'p_i': 80, 'u_i': 1.7506},
        {'id': 4, 'e_m': 8.973568, 'e_o_k': [1.103308, 0.882646, 0.706117], 'p_i': 40, 'u_i': 4.5685},
        {'id': 5, 'e_m': 1.011017, 'e_o_k': [0.090226, 0.072181, 0.057745, 0.046196, 0.036957], 'p_i': 10, 'u_i': 2.7344},
        {'id': 6, 'e_m': 1.331751, 'e_o_k': [0.221958, 0.177567], 'p_i': 40, 'u_i': 1.1398},
        {'id': 7, 'e_m': 15.446611, 'e_o_k': [1.378505, 1.102804, 0.882243, 0.705795, 0.564636], 'p_i': 80, 'u_i': 4.8954},
    ]
    B_BUDGET = 143.519995
    return processors, tasks, B_BUDGET
