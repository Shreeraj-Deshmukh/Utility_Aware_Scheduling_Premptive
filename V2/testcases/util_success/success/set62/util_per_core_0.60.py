"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519994, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519994, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.177753, 'e_o_k': [0.258404, 0.206723, 0.165379, 0.132303, 0.105842, 0.084674], 'p_i': 10, 'u_i': 2.4480},
        {'id': 1, 'e_m': 2.811752, 'e_o_k': [0.228642, 0.182914, 0.146331, 0.117065, 0.093652, 0.074922], 'p_i': 20, 'u_i': 3.0914},
        {'id': 2, 'e_m': 1.929944, 'e_o_k': [0.196133, 0.156906, 0.125525, 0.100420], 'p_i': 40, 'u_i': 2.6989},
        {'id': 3, 'e_m': 2.569412, 'e_o_k': [0.428235, 0.342588], 'p_i': 80, 'u_i': 4.1647},
        {'id': 4, 'e_m': 4.361504, 'e_o_k': [0.443242, 0.354594, 0.283675, 0.226940], 'p_i': 10, 'u_i': 1.2796},
        {'id': 5, 'e_m': 0.726097, 'e_o_k': [0.073790, 0.059032, 0.047226, 0.037781], 'p_i': 10, 'u_i': 2.4526},
        {'id': 6, 'e_m': 11.346754, 'e_o_k': [1.395093, 1.116074, 0.892859], 'p_i': 80, 'u_i': 3.7482},
        {'id': 7, 'e_m': 0.427054, 'e_o_k': [0.038112, 0.030489, 0.024391, 0.019513, 0.015611], 'p_i': 40, 'u_i': 2.1247},
    ]
    B_BUDGET = 143.519994
    return processors, tasks, B_BUDGET
