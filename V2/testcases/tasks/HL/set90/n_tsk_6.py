"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399997, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399997, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.172080, 'e_o_k': [0.325578, 0.260462], 'p_i': 10, 'u_i': 3.4053},
        {'id': 1, 'e_m': 2.847079, 'e_o_k': [0.482229, 0.385783, 0.308626, 0.246901], 'p_i': 20, 'u_i': 3.7246},
        {'id': 2, 'e_m': 2.581376, 'e_o_k': [0.437225, 0.349780, 0.279824, 0.223859], 'p_i': 40, 'u_i': 3.7938},
        {'id': 3, 'e_m': 1.215373, 'e_o_k': [0.164717, 0.131773, 0.105419, 0.084335, 0.067468, 0.053974], 'p_i': 80, 'u_i': 1.4474},
        {'id': 4, 'e_m': 1.244808, 'e_o_k': [0.185151, 0.148121, 0.118497, 0.094797, 0.075838], 'p_i': 10, 'u_i': 3.1824},
        {'id': 5, 'e_m': 26.898454, 'e_o_k': [3.645488, 2.916391, 2.333113, 1.866490, 1.493192, 1.194554], 'p_i': 80, 'u_i': 3.3367},
    ]
    B_BUDGET = 110.399997
    return processors, tasks, B_BUDGET
