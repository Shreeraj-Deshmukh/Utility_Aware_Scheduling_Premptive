"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.350656, 'e_o_k': [0.272733, 0.218186], 'p_i': 10, 'u_i': 4.4298},
        {'id': 1, 'e_m': 3.430445, 'e_o_k': [2.668124, 2.134499], 'p_i': 20, 'u_i': 1.5050},
        {'id': 2, 'e_m': 0.207300, 'e_o_k': [0.161233, 0.128986], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 1.714842, 'e_o_k': [1.333766, 1.067013], 'p_i': 80, 'u_i': 2.5958},
        {'id': 4, 'e_m': 0.699429, 'e_o_k': [0.544000, 0.435200], 'p_i': 20, 'u_i': 1.3643},
        {'id': 5, 'e_m': 2.747339, 'e_o_k': [2.136819, 1.709455], 'p_i': 80, 'u_i': 4.2904},
        {'id': 6, 'e_m': 2.551296, 'e_o_k': [1.984342, 1.587473], 'p_i': 40, 'u_i': 4.4714},
        {'id': 7, 'e_m': 2.695881, 'e_o_k': [2.096797, 1.677437], 'p_i': 80, 'u_i': 4.7028},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET
