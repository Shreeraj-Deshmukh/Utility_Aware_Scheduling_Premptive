"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399992, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399992, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.818069, 'e_o_k': [0.477315, 0.381852, 0.305482, 0.244385], 'p_i': 10, 'u_i': 3.6437},
        {'id': 1, 'e_m': 0.935497, 'e_o_k': [0.126786, 0.101429, 0.081143, 0.064914, 0.051931, 0.041545], 'p_i': 20, 'u_i': 3.7824},
        {'id': 2, 'e_m': 5.605572, 'e_o_k': [1.148683, 0.918946, 0.735157], 'p_i': 40, 'u_i': 3.8452},
        {'id': 3, 'e_m': 26.502316, 'e_o_k': [3.591801, 2.873440, 2.298752, 1.839002, 1.471201, 1.176961], 'p_i': 80, 'u_i': 1.8919},
    ]
    B_BUDGET = 110.399992
    return processors, tasks, B_BUDGET
