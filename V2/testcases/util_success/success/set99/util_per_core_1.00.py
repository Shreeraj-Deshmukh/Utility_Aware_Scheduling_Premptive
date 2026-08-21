"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199991, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199991, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.300887, 'e_o_k': [0.159945, 0.127956, 0.102365], 'p_i': 10, 'u_i': 2.4453},
        {'id': 1, 'e_m': 1.994226, 'e_o_k': [0.177971, 0.142377, 0.113902, 0.091121, 0.072897], 'p_i': 20, 'u_i': 4.4841},
        {'id': 2, 'e_m': 1.308336, 'e_o_k': [0.160861, 0.128689, 0.102951], 'p_i': 40, 'u_i': 2.2759},
        {'id': 3, 'e_m': 36.666794, 'e_o_k': [6.111132, 4.888906], 'p_i': 80, 'u_i': 4.2544},
        {'id': 4, 'e_m': 6.222022, 'e_o_k': [0.632319, 0.505855, 0.404684, 0.323747], 'p_i': 20, 'u_i': 1.1205},
        {'id': 5, 'e_m': 14.082859, 'e_o_k': [1.731499, 1.385199, 1.108159], 'p_i': 40, 'u_i': 1.0704},
        {'id': 6, 'e_m': 8.580765, 'e_o_k': [0.697759, 0.558207, 0.446566, 0.357253, 0.285802, 0.228642], 'p_i': 20, 'u_i': 1.5805},
        {'id': 7, 'e_m': 7.477834, 'e_o_k': [1.246306, 0.997045], 'p_i': 40, 'u_i': 2.6610},
    ]
    B_BUDGET = 239.199991
    return processors, tasks, B_BUDGET
