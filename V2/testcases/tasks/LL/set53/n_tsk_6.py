"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199991, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199991, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.220858, 'e_o_k': [0.029932, 0.023946, 0.019157, 0.015325, 0.012260, 0.009808], 'p_i': 10, 'u_i': 2.3061},
        {'id': 1, 'e_m': 1.725451, 'e_o_k': [0.479292, 0.383433], 'p_i': 20, 'u_i': 3.0150},
        {'id': 2, 'e_m': 1.459005, 'e_o_k': [0.217010, 0.173608, 0.138887, 0.111109, 0.088887], 'p_i': 40, 'u_i': 1.0989},
        {'id': 3, 'e_m': 8.154120, 'e_o_k': [1.670926, 1.336741, 1.069393], 'p_i': 80, 'u_i': 1.3802},
        {'id': 4, 'e_m': 1.651349, 'e_o_k': [0.245620, 0.196496, 0.157197, 0.125757, 0.100606], 'p_i': 40, 'u_i': 2.4137},
        {'id': 5, 'e_m': 8.956505, 'e_o_k': [2.487918, 1.990335], 'p_i': 80, 'u_i': 1.6729},
    ]
    B_BUDGET = 55.199991
    return processors, tasks, B_BUDGET
