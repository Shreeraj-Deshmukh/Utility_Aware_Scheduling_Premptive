"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320008, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320008, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.220858, 'e_o_k': [0.083811, 0.067049, 0.053639, 0.042911, 0.034329, 0.027463], 'p_i': 10, 'u_i': 2.3061},
        {'id': 1, 'e_m': 1.725451, 'e_o_k': [1.342017, 1.073614], 'p_i': 20, 'u_i': 3.0150},
        {'id': 2, 'e_m': 1.459005, 'e_o_k': [0.607629, 0.486103, 0.388883, 0.311106, 0.248885], 'p_i': 40, 'u_i': 1.0989},
        {'id': 3, 'e_m': 8.154120, 'e_o_k': [4.678593, 3.742875, 2.994300], 'p_i': 80, 'u_i': 1.3802},
        {'id': 4, 'e_m': 1.651349, 'e_o_k': [0.687735, 0.550188, 0.440150, 0.352120, 0.281696], 'p_i': 40, 'u_i': 2.4137},
        {'id': 5, 'e_m': 8.956505, 'e_o_k': [6.966171, 5.572937], 'p_i': 80, 'u_i': 1.6729},
    ]
    B_BUDGET = 88.320008
    return processors, tasks, B_BUDGET
