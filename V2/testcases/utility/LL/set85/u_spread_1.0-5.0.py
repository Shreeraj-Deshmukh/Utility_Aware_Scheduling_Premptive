"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200005, "H": 80, "J": 37, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "utility", "util_per_core": 0.2, "value": "1.0-5.0"}
"""

_SPEC = '{"B": 55.200005, "H": 80, "J": 37, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "utility", "util_per_core": 0.2, "value": "1.0-5.0"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.244220, 'e_o_k': [0.067839, 0.054271], 'p_i': 10, 'u_i': 1.2408},
        {'id': 1, 'e_m': 0.462328, 'e_o_k': [0.078308, 0.062646, 0.050117, 0.040093], 'p_i': 20, 'u_i': 2.7274},
        {'id': 2, 'e_m': 1.144163, 'e_o_k': [0.170181, 0.136145, 0.108916, 0.087133, 0.069706], 'p_i': 40, 'u_i': 3.7398},
        {'id': 3, 'e_m': 2.328605, 'e_o_k': [0.477173, 0.381739, 0.305391], 'p_i': 80, 'u_i': 1.4758},
        {'id': 4, 'e_m': 0.072384, 'e_o_k': [0.009810, 0.007848, 0.006278, 0.005023, 0.004018, 0.003215], 'p_i': 10, 'u_i': 1.9890},
        {'id': 5, 'e_m': 0.070477, 'e_o_k': [0.014442, 0.011554, 0.009243], 'p_i': 40, 'u_i': 1.7667},
        {'id': 6, 'e_m': 2.462336, 'e_o_k': [0.504577, 0.403662, 0.322929], 'p_i': 20, 'u_i': 2.7743},
        {'id': 7, 'e_m': 1.626328, 'e_o_k': [0.275462, 0.220370, 0.176296, 0.141037], 'p_i': 10, 'u_i': 3.3191},
    ]
    B_BUDGET = 55.200005
    return processors, tasks, B_BUDGET
