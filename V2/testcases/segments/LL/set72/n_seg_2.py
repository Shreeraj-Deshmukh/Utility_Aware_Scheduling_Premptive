"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199997, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199997, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.115220, 'e_o_k': [0.032005, 0.025604], 'p_i': 10, 'u_i': 4.4014},
        {'id': 1, 'e_m': 0.860352, 'e_o_k': [0.238987, 0.191189], 'p_i': 20, 'u_i': 2.2645},
        {'id': 2, 'e_m': 2.373578, 'e_o_k': [0.659327, 0.527462], 'p_i': 40, 'u_i': 4.9290},
        {'id': 3, 'e_m': 2.744496, 'e_o_k': [0.762360, 0.609888], 'p_i': 80, 'u_i': 2.8289},
        {'id': 4, 'e_m': 1.313968, 'e_o_k': [0.364991, 0.291993], 'p_i': 20, 'u_i': 2.4039},
        {'id': 5, 'e_m': 1.013402, 'e_o_k': [0.281501, 0.225201], 'p_i': 10, 'u_i': 2.7593},
        {'id': 6, 'e_m': 6.162818, 'e_o_k': [1.711894, 1.369515], 'p_i': 80, 'u_i': 4.9185},
        {'id': 7, 'e_m': 0.619272, 'e_o_k': [0.172020, 0.137616], 'p_i': 80, 'u_i': 1.9966},
    ]
    B_BUDGET = 55.199997
    return processors, tasks, B_BUDGET
