"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.918816, 'e_o_k': [0.255227, 0.204181], 'p_i': 10, 'u_i': 4.1192},
        {'id': 1, 'e_m': 1.455508, 'e_o_k': [0.246529, 0.197223, 0.157779, 0.126223], 'p_i': 20, 'u_i': 2.9903},
        {'id': 2, 'e_m': 7.213412, 'e_o_k': [1.221784, 0.977427, 0.781942, 0.625553], 'p_i': 40, 'u_i': 3.9277},
        {'id': 3, 'e_m': 11.236205, 'e_o_k': [1.671258, 1.337007, 1.069605, 0.855684, 0.684547], 'p_i': 80, 'u_i': 2.3920},
        {'id': 4, 'e_m': 1.039177, 'e_o_k': [0.176012, 0.140810, 0.112648, 0.090118], 'p_i': 40, 'u_i': 2.2588},
        {'id': 5, 'e_m': 23.086059, 'e_o_k': [6.412794, 5.130235], 'p_i': 80, 'u_i': 4.0829},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
