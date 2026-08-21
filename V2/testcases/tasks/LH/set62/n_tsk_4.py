"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.048710, 'e_o_k': [1.593441, 1.274753], 'p_i': 10, 'u_i': 3.2108},
        {'id': 1, 'e_m': 1.584179, 'e_o_k': [1.232140, 0.985712], 'p_i': 20, 'u_i': 1.2189},
        {'id': 2, 'e_m': 1.324389, 'e_o_k': [0.502576, 0.402061, 0.321649, 0.257319, 0.205855, 0.164684], 'p_i': 40, 'u_i': 1.4602},
        {'id': 3, 'e_m': 6.624827, 'e_o_k': [5.152643, 4.122115], 'p_i': 80, 'u_i': 2.5890},
    ]
    B_BUDGET = 88.320008
    return processors, tasks, B_BUDGET
