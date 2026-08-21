"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.119976, 'e_o_k': [0.024585, 0.019668, 0.015735], 'p_i': 10, 'u_i': 4.5752},
        {'id': 1, 'e_m': 6.256174, 'e_o_k': [1.059650, 0.847720, 0.678176, 0.542541], 'p_i': 20, 'u_i': 3.6570},
        {'id': 2, 'e_m': 10.041186, 'e_o_k': [1.700743, 1.360594, 1.088475, 0.870780], 'p_i': 40, 'u_i': 3.9951},
        {'id': 3, 'e_m': 17.933122, 'e_o_k': [3.674820, 2.939856, 2.351885], 'p_i': 80, 'u_i': 2.8657},
    ]
    B_BUDGET = 110.399994
    return processors, tasks, B_BUDGET
