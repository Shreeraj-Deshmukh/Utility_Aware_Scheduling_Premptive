"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319982, "H": 80, "J": 25, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319982, "H": 80, "J": 25, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.439041, 'e_o_k': [0.313600, 0.188160, 0.112896], 'p_i': 10, 'u_i': 1.3531},
        {'id': 1, 'e_m': 0.880194, 'e_o_k': [0.517031, 0.310219, 0.186131, 0.111679, 0.067007, 0.040204], 'p_i': 20, 'u_i': 3.7145},
        {'id': 2, 'e_m': 7.606803, 'e_o_k': [6.655952, 3.993571], 'p_i': 40, 'u_i': 2.6488},
        {'id': 3, 'e_m': 0.610708, 'e_o_k': [0.358733, 0.215240, 0.129144, 0.077486, 0.046492, 0.027895], 'p_i': 80, 'u_i': 4.3024},
        {'id': 4, 'e_m': 0.933835, 'e_o_k': [0.667025, 0.400215, 0.240129], 'p_i': 20, 'u_i': 4.8206},
        {'id': 5, 'e_m': 0.975572, 'e_o_k': [0.573057, 0.343834, 0.206300, 0.123780, 0.074268, 0.044561], 'p_i': 20, 'u_i': 3.2508},
        {'id': 6, 'e_m': 0.921104, 'e_o_k': [0.657931, 0.394759, 0.236855], 'p_i': 80, 'u_i': 3.3334},
        {'id': 7, 'e_m': 0.583852, 'e_o_k': [0.510871, 0.306522], 'p_i': 80, 'u_i': 2.1081},
    ]
    B_BUDGET = 88.319982
    return processors, tasks, B_BUDGET
