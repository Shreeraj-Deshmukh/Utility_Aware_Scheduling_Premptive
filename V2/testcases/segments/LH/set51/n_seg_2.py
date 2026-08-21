"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.415588, 'e_o_k': [1.101013, 0.880811], 'p_i': 10, 'u_i': 2.5682},
        {'id': 1, 'e_m': 1.559525, 'e_o_k': [1.212964, 0.970371], 'p_i': 20, 'u_i': 2.9074},
        {'id': 2, 'e_m': 1.007726, 'e_o_k': [0.783787, 0.627030], 'p_i': 40, 'u_i': 4.2053},
        {'id': 3, 'e_m': 1.342241, 'e_o_k': [1.043966, 0.835172], 'p_i': 80, 'u_i': 2.1233},
        {'id': 4, 'e_m': 4.007853, 'e_o_k': [3.117219, 2.493775], 'p_i': 80, 'u_i': 2.8725},
        {'id': 5, 'e_m': 0.593098, 'e_o_k': [0.461299, 0.369039], 'p_i': 20, 'u_i': 1.8909},
        {'id': 6, 'e_m': 1.066826, 'e_o_k': [0.829754, 0.663803], 'p_i': 20, 'u_i': 4.9900},
        {'id': 7, 'e_m': 0.431948, 'e_o_k': [0.335960, 0.268768], 'p_i': 80, 'u_i': 1.9407},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
