"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.943519, 'e_o_k': [0.159810, 0.127848, 0.102278, 0.081823], 'p_i': 10, 'u_i': 2.3827},
        {'id': 1, 'e_m': 3.438081, 'e_o_k': [0.511376, 0.409101, 0.327280, 0.261824, 0.209459], 'p_i': 20, 'u_i': 2.9856},
        {'id': 2, 'e_m': 0.070381, 'e_o_k': [0.009539, 0.007631, 0.006105, 0.004884, 0.003907, 0.003126], 'p_i': 40, 'u_i': 4.8236},
        {'id': 3, 'e_m': 17.556587, 'e_o_k': [2.973677, 2.378941, 1.903153, 1.522522], 'p_i': 80, 'u_i': 2.2531},
        {'id': 4, 'e_m': 22.420817, 'e_o_k': [3.334843, 2.667874, 2.134300, 1.707440, 1.365952], 'p_i': 80, 'u_i': 4.0598},
        {'id': 5, 'e_m': 0.645340, 'e_o_k': [0.109306, 0.087444, 0.069956, 0.055964], 'p_i': 20, 'u_i': 4.5014},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
