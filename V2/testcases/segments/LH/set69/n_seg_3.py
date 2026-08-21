"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 22, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 22, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.028851, 'e_o_k': [0.016554, 0.013243, 0.010595], 'p_i': 10, 'u_i': 3.1857},
        {'id': 1, 'e_m': 0.425044, 'e_o_k': [0.243877, 0.195102, 0.156082], 'p_i': 20, 'u_i': 3.0673},
        {'id': 2, 'e_m': 0.371477, 'e_o_k': [0.213142, 0.170514, 0.136411], 'p_i': 40, 'u_i': 1.1608},
        {'id': 3, 'e_m': 3.599048, 'e_o_k': [2.065027, 1.652022, 1.321617], 'p_i': 80, 'u_i': 3.0557},
        {'id': 4, 'e_m': 5.420557, 'e_o_k': [3.110156, 2.488125, 1.990500], 'p_i': 80, 'u_i': 1.7105},
        {'id': 5, 'e_m': 15.171358, 'e_o_k': [8.704878, 6.963902, 5.571122], 'p_i': 80, 'u_i': 2.7562},
        {'id': 6, 'e_m': 0.633743, 'e_o_k': [0.363623, 0.290898, 0.232719], 'p_i': 20, 'u_i': 4.1777},
        {'id': 7, 'e_m': 2.600128, 'e_o_k': [1.491877, 1.193501, 0.954801], 'p_i': 80, 'u_i': 1.3396},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET
