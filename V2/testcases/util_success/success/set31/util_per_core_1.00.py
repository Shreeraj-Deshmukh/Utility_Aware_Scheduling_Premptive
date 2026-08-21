"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.2, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.2, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.570206, 'e_o_k': [0.193058, 0.154446, 0.123557], 'p_i': 10, 'u_i': 4.8356},
        {'id': 1, 'e_m': 2.137684, 'e_o_k': [0.217244, 0.173795, 0.139036, 0.111229], 'p_i': 20, 'u_i': 2.0758},
        {'id': 2, 'e_m': 17.025280, 'e_o_k': [2.093272, 1.674618, 1.339694], 'p_i': 40, 'u_i': 3.9792},
        {'id': 3, 'e_m': 22.949421, 'e_o_k': [2.821650, 2.257320, 1.805856], 'p_i': 80, 'u_i': 1.3854},
        {'id': 4, 'e_m': 0.610676, 'e_o_k': [0.062061, 0.049648, 0.039719, 0.031775], 'p_i': 40, 'u_i': 2.0294},
        {'id': 5, 'e_m': 34.346340, 'e_o_k': [4.222911, 3.378329, 2.702663], 'p_i': 80, 'u_i': 2.2362},
        {'id': 6, 'e_m': 7.520915, 'e_o_k': [0.611576, 0.489261, 0.391409, 0.313127, 0.250501, 0.200401], 'p_i': 20, 'u_i': 4.4908},
        {'id': 7, 'e_m': 4.059072, 'e_o_k': [0.676512, 0.541210], 'p_i': 20, 'u_i': 1.3350},
    ]
    B_BUDGET = 239.200000
    return processors, tasks, B_BUDGET
