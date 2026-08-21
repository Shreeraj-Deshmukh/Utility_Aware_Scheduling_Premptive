"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320006, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.320006, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.343272, 'e_o_k': [0.245194, 0.147117, 0.088270], 'p_i': 10, 'u_i': 3.5588},
        {'id': 1, 'e_m': 0.791370, 'e_o_k': [0.692448, 0.415469], 'p_i': 20, 'u_i': 1.0875},
        {'id': 2, 'e_m': 2.553569, 'e_o_k': [1.642921, 0.985753, 0.591452, 0.354871], 'p_i': 40, 'u_i': 2.9446},
        {'id': 3, 'e_m': 0.112895, 'e_o_k': [0.072634, 0.043581, 0.026148, 0.015689], 'p_i': 80, 'u_i': 2.5289},
        {'id': 4, 'e_m': 5.014202, 'e_o_k': [3.044710, 1.826826, 1.096096, 0.657657, 0.394594], 'p_i': 40, 'u_i': 2.8941},
        {'id': 5, 'e_m': 2.695419, 'e_o_k': [1.583305, 0.949983, 0.569990, 0.341994, 0.205196, 0.123118], 'p_i': 40, 'u_i': 4.5618},
        {'id': 6, 'e_m': 0.133194, 'e_o_k': [0.116544, 0.069927], 'p_i': 10, 'u_i': 3.9189},
        {'id': 7, 'e_m': 2.191761, 'e_o_k': [1.410141, 0.846084, 0.507651, 0.304590], 'p_i': 40, 'u_i': 2.1344},
    ]
    B_BUDGET = 88.320006
    return processors, tasks, B_BUDGET
