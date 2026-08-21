"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199991, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199991, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.711139, 'e_o_k': [0.451856, 0.361485], 'p_i': 10, 'u_i': 2.4344},
        {'id': 1, 'e_m': 8.339597, 'e_o_k': [0.744252, 0.595402, 0.476322, 0.381057, 0.304846], 'p_i': 20, 'u_i': 4.3497},
        {'id': 2, 'e_m': 9.227199, 'e_o_k': [1.537866, 1.230293], 'p_i': 40, 'u_i': 1.9085},
        {'id': 3, 'e_m': 34.571279, 'e_o_k': [2.811222, 2.248977, 1.799182, 1.439345, 1.151476, 0.921181], 'p_i': 80, 'u_i': 4.5985},
        {'id': 4, 'e_m': 1.840806, 'e_o_k': [0.226329, 0.181063, 0.144850], 'p_i': 10, 'u_i': 1.1568},
        {'id': 5, 'e_m': 0.302316, 'e_o_k': [0.030723, 0.024578, 0.019663, 0.015730], 'p_i': 40, 'u_i': 3.3218},
        {'id': 6, 'e_m': 17.819300, 'e_o_k': [1.449006, 1.159205, 0.927364, 0.741891, 0.593513, 0.474810], 'p_i': 40, 'u_i': 3.9399},
        {'id': 7, 'e_m': 0.478572, 'e_o_k': [0.079762, 0.063810], 'p_i': 40, 'u_i': 2.8364},
    ]
    B_BUDGET = 239.199991
    return processors, tasks, B_BUDGET
