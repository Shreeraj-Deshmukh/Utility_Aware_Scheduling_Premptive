"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359984, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359984, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.492232, 'e_o_k': [0.311658, 0.249326, 0.199461, 0.159569, 0.127655], 'p_i': 10, 'u_i': 4.9659},
        {'id': 1, 'e_m': 2.994921, 'e_o_k': [0.267276, 0.213821, 0.171057, 0.136846, 0.109476], 'p_i': 20, 'u_i': 4.3569},
        {'id': 2, 'e_m': 9.503263, 'e_o_k': [1.168434, 0.934747, 0.747798], 'p_i': 40, 'u_i': 3.1411},
        {'id': 3, 'e_m': 3.826176, 'e_o_k': [0.388839, 0.311071, 0.248857, 0.199086], 'p_i': 80, 'u_i': 3.1206},
        {'id': 4, 'e_m': 4.498565, 'e_o_k': [0.553102, 0.442482, 0.353985], 'p_i': 20, 'u_i': 4.7030},
        {'id': 5, 'e_m': 1.265289, 'e_o_k': [0.210881, 0.168705], 'p_i': 10, 'u_i': 2.0532},
        {'id': 6, 'e_m': 32.939949, 'e_o_k': [2.939667, 2.351734, 1.881387, 1.505110, 1.204088], 'p_i': 80, 'u_i': 1.9357},
        {'id': 7, 'e_m': 2.096617, 'e_o_k': [0.187109, 0.149687, 0.119750, 0.095800, 0.076640], 'p_i': 40, 'u_i': 4.8494},
    ]
    B_BUDGET = 191.359984
    return processors, tasks, B_BUDGET
