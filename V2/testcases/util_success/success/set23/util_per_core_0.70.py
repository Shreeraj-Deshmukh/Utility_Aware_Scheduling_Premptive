"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439994, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439994, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.468867, 'e_o_k': [0.047649, 0.038119, 0.030495, 0.024396], 'p_i': 10, 'u_i': 2.0521},
        {'id': 1, 'e_m': 4.158602, 'e_o_k': [0.371127, 0.296902, 0.237521, 0.190017, 0.152014], 'p_i': 20, 'u_i': 4.1261},
        {'id': 2, 'e_m': 7.392229, 'e_o_k': [0.751243, 0.600994, 0.480795, 0.384636], 'p_i': 40, 'u_i': 2.8820},
        {'id': 3, 'e_m': 37.845795, 'e_o_k': [3.077494, 2.461996, 1.969596, 1.575677, 1.260542, 1.008433], 'p_i': 80, 'u_i': 1.8301},
        {'id': 4, 'e_m': 0.008646, 'e_o_k': [0.001441, 0.001153], 'p_i': 20, 'u_i': 2.8656},
        {'id': 5, 'e_m': 4.710684, 'e_o_k': [0.383057, 0.306446, 0.245157, 0.196125, 0.156900, 0.125520], 'p_i': 20, 'u_i': 4.7863},
        {'id': 6, 'e_m': 0.233393, 'e_o_k': [0.018979, 0.015183, 0.012146, 0.009717, 0.007774, 0.006219], 'p_i': 20, 'u_i': 3.1132},
        {'id': 7, 'e_m': 2.396689, 'e_o_k': [0.243566, 0.194853, 0.155882, 0.124706], 'p_i': 10, 'u_i': 2.8421},
    ]
    B_BUDGET = 167.439994
    return processors, tasks, B_BUDGET
