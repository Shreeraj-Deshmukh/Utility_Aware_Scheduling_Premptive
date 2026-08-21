"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.176248, 'e_o_k': [1.692637, 1.354110], 'p_i': 10, 'u_i': 2.0210},
        {'id': 1, 'e_m': 1.214833, 'e_o_k': [0.944870, 0.755896], 'p_i': 20, 'u_i': 2.6755},
        {'id': 2, 'e_m': 1.222123, 'e_o_k': [0.579597, 0.463678, 0.370942, 0.296754], 'p_i': 40, 'u_i': 1.9112},
        {'id': 3, 'e_m': 7.286441, 'e_o_k': [3.034572, 2.427658, 1.942126, 1.553701, 1.242961], 'p_i': 80, 'u_i': 4.0850},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET
