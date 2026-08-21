"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679993, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679993, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.175817, 'e_o_k': [0.014297, 0.011437, 0.009150, 0.007320, 0.005856, 0.004685], 'p_i': 10, 'u_i': 2.1335},
        {'id': 1, 'e_m': 0.569763, 'e_o_k': [0.046331, 0.037065, 0.029652, 0.023722, 0.018977, 0.015182], 'p_i': 20, 'u_i': 1.1307},
        {'id': 2, 'e_m': 2.984963, 'e_o_k': [0.266388, 0.213110, 0.170488, 0.136391, 0.109112], 'p_i': 40, 'u_i': 4.3260},
        {'id': 3, 'e_m': 1.604801, 'e_o_k': [0.197312, 0.157849, 0.126279], 'p_i': 80, 'u_i': 4.7000},
        {'id': 4, 'e_m': 0.625370, 'e_o_k': [0.104228, 0.083383], 'p_i': 10, 'u_i': 1.4843},
        {'id': 5, 'e_m': 1.194963, 'e_o_k': [0.199160, 0.159328], 'p_i': 20, 'u_i': 4.5666},
        {'id': 6, 'e_m': 4.162884, 'e_o_k': [0.371509, 0.297207, 0.237766, 0.190213, 0.152170], 'p_i': 10, 'u_i': 2.1776},
        {'id': 7, 'e_m': 9.653801, 'e_o_k': [1.186943, 0.949554, 0.759643], 'p_i': 80, 'u_i': 3.5354},
    ]
    B_BUDGET = 95.679993
    return processors, tasks, B_BUDGET
