"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.565390, 'e_o_k': [0.084095, 0.067276, 0.053821, 0.043057, 0.034445], 'p_i': 10, 'u_i': 3.2031},
        {'id': 1, 'e_m': 0.264926, 'e_o_k': [0.044872, 0.035898, 0.028718, 0.022975], 'p_i': 20, 'u_i': 2.0803},
        {'id': 2, 'e_m': 11.606642, 'e_o_k': [1.726357, 1.381085, 1.104868, 0.883895, 0.707116], 'p_i': 40, 'u_i': 3.1382},
        {'id': 3, 'e_m': 3.203895, 'e_o_k': [0.476543, 0.381234, 0.304988, 0.243990, 0.195192], 'p_i': 80, 'u_i': 3.0103},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET
