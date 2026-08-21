"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 40, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "segments", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 40, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "segments", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.259080, 'e_o_k': [0.213259, 0.170607, 0.136486, 0.109189], 'p_i': 10, 'u_i': 2.8729},
        {'id': 1, 'e_m': 3.910652, 'e_o_k': [0.662373, 0.529899, 0.423919, 0.339135], 'p_i': 20, 'u_i': 4.4646},
        {'id': 2, 'e_m': 0.555334, 'e_o_k': [0.094061, 0.075249, 0.060199, 0.048159], 'p_i': 40, 'u_i': 2.8456},
        {'id': 3, 'e_m': 5.117361, 'e_o_k': [0.866762, 0.693409, 0.554728, 0.443782], 'p_i': 80, 'u_i': 4.6357},
        {'id': 4, 'e_m': 0.830972, 'e_o_k': [0.140747, 0.112598, 0.090078, 0.072063], 'p_i': 10, 'u_i': 3.1275},
        {'id': 5, 'e_m': 13.997484, 'e_o_k': [2.370848, 1.896678, 1.517342, 1.213874], 'p_i': 80, 'u_i': 2.7677},
        {'id': 6, 'e_m': 1.327086, 'e_o_k': [0.224777, 0.179822, 0.143858, 0.115086], 'p_i': 10, 'u_i': 2.2237},
        {'id': 7, 'e_m': 0.099346, 'e_o_k': [0.016827, 0.013462, 0.010769, 0.008615], 'p_i': 10, 'u_i': 3.7702},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
