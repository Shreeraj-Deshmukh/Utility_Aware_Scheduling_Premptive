"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399989, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399989, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.259839, 'e_o_k': [0.336125, 0.268900, 0.215120, 0.172096, 0.137677], 'p_i': 10, 'u_i': 3.3453},
        {'id': 1, 'e_m': 6.374227, 'e_o_k': [1.306194, 1.044955, 0.835964], 'p_i': 20, 'u_i': 2.8841},
        {'id': 2, 'e_m': 9.556570, 'e_o_k': [1.958313, 1.566651, 1.253321], 'p_i': 40, 'u_i': 2.2513},
        {'id': 3, 'e_m': 1.311243, 'e_o_k': [0.222094, 0.177675, 0.142140, 0.113712], 'p_i': 80, 'u_i': 1.5109},
    ]
    B_BUDGET = 110.399989
    return processors, tasks, B_BUDGET
