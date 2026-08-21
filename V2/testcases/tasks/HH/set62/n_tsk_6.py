"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.799476, 'e_o_k': [2.177370, 1.741896], 'p_i': 10, 'u_i': 4.3165},
        {'id': 1, 'e_m': 2.384351, 'e_o_k': [1.854496, 1.483596], 'p_i': 20, 'u_i': 4.1600},
        {'id': 2, 'e_m': 1.700493, 'e_o_k': [0.708201, 0.566561, 0.453249, 0.362599, 0.290079], 'p_i': 40, 'u_i': 2.4258},
        {'id': 3, 'e_m': 2.594088, 'e_o_k': [1.230259, 0.984207, 0.787366, 0.629892], 'p_i': 80, 'u_i': 2.6711},
        {'id': 4, 'e_m': 25.043045, 'e_o_k': [9.503281, 7.602625, 6.082100, 4.865680, 3.892544, 3.114035], 'p_i': 80, 'u_i': 3.0914},
        {'id': 5, 'e_m': 0.128584, 'e_o_k': [0.060981, 0.048785, 0.039028, 0.031223], 'p_i': 10, 'u_i': 2.6989},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
