"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.350656, 'e_o_k': [0.098184, 0.098184, 0.098184, 0.098184, 0.098184], 'p_i': 10, 'u_i': 4.4298},
        {'id': 1, 'e_m': 3.430445, 'e_o_k': [1.600874, 1.600874, 1.600874], 'p_i': 20, 'u_i': 1.5050},
        {'id': 2, 'e_m': 0.207300, 'e_o_k': [0.145110, 0.145110], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 1.714842, 'e_o_k': [0.400130, 0.400130, 0.400130, 0.400130, 0.400130, 0.400130], 'p_i': 80, 'u_i': 4.0993},
        {'id': 4, 'e_m': 0.699429, 'e_o_k': [0.489600, 0.489600], 'p_i': 20, 'u_i': 2.5958},
        {'id': 5, 'e_m': 2.747339, 'e_o_k': [1.282091, 1.282091, 1.282091], 'p_i': 80, 'u_i': 1.3643},
        {'id': 6, 'e_m': 2.551296, 'e_o_k': [0.595302, 0.595302, 0.595302, 0.595302, 0.595302, 0.595302], 'p_i': 40, 'u_i': 1.6218},
        {'id': 7, 'e_m': 2.695881, 'e_o_k': [0.943559, 0.943559, 0.943559, 0.943559], 'p_i': 80, 'u_i': 1.2955},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
