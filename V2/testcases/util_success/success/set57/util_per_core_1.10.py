"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119976, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119976, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.114094, 'e_o_k': [0.382880, 0.306304, 0.245043], 'p_i': 10, 'u_i': 4.3585},
        {'id': 1, 'e_m': 7.991367, 'e_o_k': [0.812131, 0.649705, 0.519764, 0.415811], 'p_i': 20, 'u_i': 3.8315},
        {'id': 2, 'e_m': 2.904249, 'e_o_k': [0.295147, 0.236118, 0.188894, 0.151115], 'p_i': 40, 'u_i': 2.9907},
        {'id': 3, 'e_m': 35.198546, 'e_o_k': [5.866424, 4.693139], 'p_i': 80, 'u_i': 1.2622},
        {'id': 4, 'e_m': 6.744601, 'e_o_k': [0.829254, 0.663403, 0.530723], 'p_i': 20, 'u_i': 2.2522},
        {'id': 5, 'e_m': 7.898898, 'e_o_k': [0.642312, 0.513850, 0.411080, 0.328864, 0.263091, 0.210473], 'p_i': 80, 'u_i': 4.2198},
        {'id': 6, 'e_m': 19.155166, 'e_o_k': [1.709469, 1.367575, 1.094060, 0.875248, 0.700198], 'p_i': 40, 'u_i': 3.6769},
        {'id': 7, 'e_m': 1.231774, 'e_o_k': [0.125180, 0.100144, 0.080115, 0.064092], 'p_i': 20, 'u_i': 3.0538},
    ]
    B_BUDGET = 263.119976
    return processors, tasks, B_BUDGET
