"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640018, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 176.640018, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.599440, 'e_o_k': [1.119608, 1.119608], 'p_i': 10, 'u_i': 2.3541},
        {'id': 1, 'e_m': 5.185523, 'e_o_k': [2.419911, 2.419911, 2.419911], 'p_i': 20, 'u_i': 4.5958},
        {'id': 2, 'e_m': 2.922224, 'e_o_k': [1.022778, 1.022778, 1.022778, 1.022778], 'p_i': 40, 'u_i': 4.0042},
        {'id': 3, 'e_m': 7.584490, 'e_o_k': [5.309143, 5.309143], 'p_i': 80, 'u_i': 1.4529},
        {'id': 4, 'e_m': 1.038987, 'e_o_k': [0.242430, 0.242430, 0.242430, 0.242430, 0.242430, 0.242430], 'p_i': 40, 'u_i': 4.9580},
        {'id': 5, 'e_m': 1.421690, 'e_o_k': [0.331728, 0.331728, 0.331728, 0.331728, 0.331728, 0.331728], 'p_i': 20, 'u_i': 2.0799},
        {'id': 6, 'e_m': 3.169787, 'e_o_k': [2.218851, 2.218851], 'p_i': 40, 'u_i': 1.2465},
        {'id': 7, 'e_m': 0.366143, 'e_o_k': [0.170867, 0.170867, 0.170867], 'p_i': 10, 'u_i': 3.7304},
    ]
    B_BUDGET = 176.640018
    return processors, tasks, B_BUDGET
