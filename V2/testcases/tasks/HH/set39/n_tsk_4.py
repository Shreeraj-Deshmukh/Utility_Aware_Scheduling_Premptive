"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.979134, 'e_o_k': [0.761549, 0.609239], 'p_i': 10, 'u_i': 1.9313},
        {'id': 1, 'e_m': 7.975924, 'e_o_k': [3.321720, 2.657376, 2.125901, 1.700721, 1.360576], 'p_i': 20, 'u_i': 4.6903},
        {'id': 2, 'e_m': 3.811370, 'e_o_k': [2.186852, 1.749481, 1.399585], 'p_i': 40, 'u_i': 4.0696},
        {'id': 3, 'e_m': 16.640490, 'e_o_k': [12.942603, 10.354083], 'p_i': 80, 'u_i': 1.5844},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET
