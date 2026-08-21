"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 36, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.4, "seed": 1007, "set": 7, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 36, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.4, "seed": 1007, "set": 7, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.175817, 'e_o_k': [0.023828, 0.019062, 0.015250, 0.012200, 0.009760, 0.007808], 'p_i': 10, 'u_i': 2.1335},
        {'id': 1, 'e_m': 0.569763, 'e_o_k': [0.077219, 0.061775, 0.049420, 0.039536, 0.031629, 0.025303], 'p_i': 20, 'u_i': 1.1307},
        {'id': 2, 'e_m': 2.984963, 'e_o_k': [0.443980, 0.355184, 0.284147, 0.227318, 0.181854], 'p_i': 40, 'u_i': 4.3260},
        {'id': 3, 'e_m': 1.604801, 'e_o_k': [0.328853, 0.263082, 0.210466], 'p_i': 80, 'u_i': 4.7000},
        {'id': 4, 'e_m': 0.625370, 'e_o_k': [0.173714, 0.138971], 'p_i': 10, 'u_i': 1.4843},
        {'id': 5, 'e_m': 1.194963, 'e_o_k': [0.331934, 0.265547], 'p_i': 20, 'u_i': 4.5666},
        {'id': 6, 'e_m': 4.162884, 'e_o_k': [0.619182, 0.495346, 0.396276, 0.317021, 0.253617], 'p_i': 10, 'u_i': 2.1776},
        {'id': 7, 'e_m': 9.653801, 'e_o_k': [1.978238, 1.582590, 1.266072], 'p_i': 80, 'u_i': 3.5354},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
