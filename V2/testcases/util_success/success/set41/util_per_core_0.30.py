"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.76, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.76, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.658561, 'e_o_k': [0.080971, 0.064776, 0.051821], 'p_i': 10, 'u_i': 1.3531},
        {'id': 1, 'e_m': 1.320292, 'e_o_k': [0.107362, 0.085889, 0.068712, 0.054969, 0.043975, 0.035180], 'p_i': 20, 'u_i': 3.7145},
        {'id': 2, 'e_m': 11.410204, 'e_o_k': [1.901701, 1.521361], 'p_i': 40, 'u_i': 2.6488},
        {'id': 3, 'e_m': 0.916062, 'e_o_k': [0.074491, 0.059593, 0.047674, 0.038139, 0.030512, 0.024409], 'p_i': 80, 'u_i': 4.3024},
        {'id': 4, 'e_m': 1.400753, 'e_o_k': [0.172224, 0.137779, 0.110223], 'p_i': 20, 'u_i': 4.8206},
        {'id': 5, 'e_m': 1.463358, 'e_o_k': [0.118995, 0.095196, 0.076157, 0.060926, 0.048741, 0.038992], 'p_i': 20, 'u_i': 3.2508},
        {'id': 6, 'e_m': 1.381656, 'e_o_k': [0.169876, 0.135901, 0.108720], 'p_i': 80, 'u_i': 3.3334},
        {'id': 7, 'e_m': 0.875778, 'e_o_k': [0.145963, 0.116770], 'p_i': 80, 'u_i': 2.1081},
    ]
    B_BUDGET = 71.760000
    return processors, tasks, B_BUDGET
