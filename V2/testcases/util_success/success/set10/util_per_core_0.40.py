"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680013, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680013, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.443224, 'e_o_k': [0.036041, 0.028833, 0.023067, 0.018453, 0.014763, 0.011810], 'p_i': 10, 'u_i': 3.7777},
        {'id': 1, 'e_m': 0.385037, 'e_o_k': [0.034362, 0.027490, 0.021992, 0.017593, 0.014075], 'p_i': 20, 'u_i': 2.9102},
        {'id': 2, 'e_m': 7.186952, 'e_o_k': [0.730381, 0.584305, 0.467444, 0.373955], 'p_i': 40, 'u_i': 3.0744},
        {'id': 3, 'e_m': 20.620712, 'e_o_k': [3.436785, 2.749428], 'p_i': 80, 'u_i': 3.1102},
        {'id': 4, 'e_m': 1.451540, 'e_o_k': [0.118034, 0.094428, 0.075542, 0.060434, 0.048347, 0.038678], 'p_i': 20, 'u_i': 3.9746},
        {'id': 5, 'e_m': 1.346300, 'e_o_k': [0.165529, 0.132423, 0.105938], 'p_i': 10, 'u_i': 1.5757},
        {'id': 6, 'e_m': 2.067937, 'e_o_k': [0.254255, 0.203404, 0.162723], 'p_i': 40, 'u_i': 4.9941},
        {'id': 7, 'e_m': 1.603507, 'e_o_k': [0.267251, 0.213801], 'p_i': 40, 'u_i': 1.7632},
    ]
    B_BUDGET = 95.680013
    return processors, tasks, B_BUDGET
