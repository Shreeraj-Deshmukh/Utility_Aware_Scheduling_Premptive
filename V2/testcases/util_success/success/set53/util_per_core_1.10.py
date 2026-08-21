"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119994, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119994, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.874668, 'e_o_k': [0.145778, 0.116622], 'p_i': 10, 'u_i': 1.8047},
        {'id': 1, 'e_m': 6.703542, 'e_o_k': [1.117257, 0.893806], 'p_i': 20, 'u_i': 1.0945},
        {'id': 2, 'e_m': 5.476856, 'e_o_k': [0.488772, 0.391018, 0.312814, 0.250251, 0.200201], 'p_i': 40, 'u_i': 2.4137},
        {'id': 3, 'e_m': 29.534248, 'e_o_k': [4.922375, 3.937900], 'p_i': 80, 'u_i': 1.6729},
        {'id': 4, 'e_m': 5.051687, 'e_o_k': [0.410786, 0.328629, 0.262903, 0.210323, 0.168258, 0.134606], 'p_i': 40, 'u_i': 2.8481},
        {'id': 5, 'e_m': 4.683046, 'e_o_k': [0.475919, 0.380735, 0.304588, 0.243671], 'p_i': 10, 'u_i': 3.6691},
        {'id': 6, 'e_m': 7.866202, 'e_o_k': [0.799411, 0.639529, 0.511623, 0.409298], 'p_i': 20, 'u_i': 3.0767},
        {'id': 7, 'e_m': 22.667981, 'e_o_k': [1.843285, 1.474628, 1.179702, 0.943762, 0.755010, 0.604008], 'p_i': 80, 'u_i': 1.7471},
    ]
    B_BUDGET = 263.119994
    return processors, tasks, B_BUDGET
