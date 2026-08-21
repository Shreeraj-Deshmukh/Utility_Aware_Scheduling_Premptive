"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.177414, 'e_o_k': [0.067325, 0.053860, 0.043088, 0.034470, 0.027576, 0.022061], 'p_i': 10, 'u_i': 2.4636},
        {'id': 1, 'e_m': 1.270085, 'e_o_k': [0.602344, 0.481875, 0.385500, 0.308400], 'p_i': 20, 'u_i': 2.5536},
        {'id': 2, 'e_m': 3.439272, 'e_o_k': [2.674989, 2.139991], 'p_i': 40, 'u_i': 3.8458},
        {'id': 3, 'e_m': 1.662565, 'e_o_k': [0.953931, 0.763145, 0.610516], 'p_i': 80, 'u_i': 4.1906},
        {'id': 4, 'e_m': 0.274669, 'e_o_k': [0.213631, 0.170905], 'p_i': 10, 'u_i': 2.6385},
        {'id': 5, 'e_m': 14.761889, 'e_o_k': [6.147860, 4.918288, 3.934630, 3.147704, 2.518163], 'p_i': 80, 'u_i': 2.8958},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET
