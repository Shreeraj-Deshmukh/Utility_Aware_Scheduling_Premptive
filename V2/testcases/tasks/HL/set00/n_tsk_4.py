"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.346256, 'e_o_k': [0.348979, 0.279183, 0.223347, 0.178677, 0.142942], 'p_i': 10, 'u_i': 1.5213},
        {'id': 1, 'e_m': 3.572738, 'e_o_k': [0.732119, 0.585695, 0.468556], 'p_i': 20, 'u_i': 2.4569},
        {'id': 2, 'e_m': 7.198209, 'e_o_k': [1.070652, 0.856522, 0.685217, 0.548174, 0.438539], 'p_i': 40, 'u_i': 4.9222},
        {'id': 3, 'e_m': 16.542579, 'e_o_k': [2.801927, 2.241542, 1.793233, 1.434587], 'p_i': 80, 'u_i': 1.9107},
    ]
    B_BUDGET = 110.399998
    return processors, tasks, B_BUDGET
