"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 29, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "utility", "util_per_core": 0.4, "value": "1.0-5.0"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 29, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "utility", "util_per_core": 0.4, "value": "1.0-5.0"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.048193, 'e_o_k': [0.027652, 0.022121, 0.017697], 'p_i': 10, 'u_i': 4.1859},
        {'id': 1, 'e_m': 3.648051, 'e_o_k': [2.093144, 1.674515, 1.339612], 'p_i': 20, 'u_i': 1.3758},
        {'id': 2, 'e_m': 5.612216, 'e_o_k': [3.220124, 2.576099, 2.060879], 'p_i': 40, 'u_i': 3.6848},
        {'id': 3, 'e_m': 0.963244, 'e_o_k': [0.749190, 0.599352], 'p_i': 80, 'u_i': 1.6851},
        {'id': 4, 'e_m': 5.443451, 'e_o_k': [2.267025, 1.813620, 1.450896, 1.160717, 0.928573], 'p_i': 20, 'u_i': 1.3700},
        {'id': 5, 'e_m': 1.362619, 'e_o_k': [0.567488, 0.453990, 0.363192, 0.290554, 0.232443], 'p_i': 10, 'u_i': 3.3252},
        {'id': 6, 'e_m': 1.225919, 'e_o_k': [0.953492, 0.762794], 'p_i': 80, 'u_i': 4.3008},
        {'id': 7, 'e_m': 2.933902, 'e_o_k': [1.391417, 1.113134, 0.890507, 0.712405], 'p_i': 80, 'u_i': 2.2362},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET
