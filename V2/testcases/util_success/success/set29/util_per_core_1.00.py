"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199998, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199998, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.849585, 'e_o_k': [0.473310, 0.378648, 0.302918], 'p_i': 10, 'u_i': 1.6136},
        {'id': 1, 'e_m': 1.244429, 'e_o_k': [0.101193, 0.080954, 0.064763, 0.051811, 0.041449, 0.033159], 'p_i': 20, 'u_i': 3.6316},
        {'id': 2, 'e_m': 9.153258, 'e_o_k': [1.125401, 0.900320, 0.720256], 'p_i': 40, 'u_i': 1.6985},
        {'id': 3, 'e_m': 30.698458, 'e_o_k': [3.119762, 2.495810, 1.996648, 1.597318], 'p_i': 80, 'u_i': 2.0121},
        {'id': 4, 'e_m': 4.788727, 'e_o_k': [0.427361, 0.341889, 0.273511, 0.218809, 0.175047], 'p_i': 10, 'u_i': 4.0442},
        {'id': 5, 'e_m': 5.094172, 'e_o_k': [0.849029, 0.679223], 'p_i': 80, 'u_i': 3.4092},
        {'id': 6, 'e_m': 5.797505, 'e_o_k': [0.712808, 0.570246, 0.456197], 'p_i': 20, 'u_i': 3.7580},
        {'id': 7, 'e_m': 2.156656, 'e_o_k': [0.175372, 0.140298, 0.112238, 0.089791, 0.071832, 0.057466], 'p_i': 20, 'u_i': 3.6538},
    ]
    B_BUDGET = 239.199998
    return processors, tasks, B_BUDGET
