"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.389062, 'e_o_k': [0.223233, 0.178586, 0.142869], 'p_i': 10, 'u_i': 1.2652},
        {'id': 1, 'e_m': 0.895639, 'e_o_k': [0.513891, 0.411113, 0.328891], 'p_i': 20, 'u_i': 2.8552},
        {'id': 2, 'e_m': 0.010963, 'e_o_k': [0.006290, 0.005032, 0.004026], 'p_i': 40, 'u_i': 3.5059},
        {'id': 3, 'e_m': 4.905019, 'e_o_k': [2.814355, 2.251484, 1.801187], 'p_i': 80, 'u_i': 1.7742},
        {'id': 4, 'e_m': 8.853066, 'e_o_k': [5.079628, 4.063702, 3.250962], 'p_i': 40, 'u_i': 1.4108},
        {'id': 5, 'e_m': 0.037049, 'e_o_k': [0.021258, 0.017006, 0.013605], 'p_i': 40, 'u_i': 2.2719},
        {'id': 6, 'e_m': 1.507728, 'e_o_k': [0.865090, 0.692072, 0.553657], 'p_i': 80, 'u_i': 4.1261},
        {'id': 7, 'e_m': 1.090040, 'e_o_k': [0.625433, 0.500346, 0.400277], 'p_i': 80, 'u_i': 2.8820},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET
