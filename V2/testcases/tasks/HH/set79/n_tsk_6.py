"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.935752, 'e_o_k': [0.355097, 0.284078, 0.227262, 0.181810, 0.145448, 0.116358], 'p_i': 10, 'u_i': 2.7067},
        {'id': 1, 'e_m': 2.374259, 'e_o_k': [0.900979, 0.720783, 0.576626, 0.461301, 0.369041, 0.295233], 'p_i': 20, 'u_i': 4.2680},
        {'id': 2, 'e_m': 0.780802, 'e_o_k': [0.325179, 0.260143, 0.208115, 0.166492, 0.133193], 'p_i': 40, 'u_i': 4.9110},
        {'id': 3, 'e_m': 26.630915, 'e_o_k': [10.105842, 8.084674, 6.467739, 5.174191, 4.139353, 3.311482], 'p_i': 80, 'u_i': 1.5555},
        {'id': 4, 'e_m': 1.850169, 'e_o_k': [1.061573, 0.849258, 0.679406], 'p_i': 20, 'u_i': 1.9189},
        {'id': 5, 'e_m': 11.423752, 'e_o_k': [8.885141, 7.108113], 'p_i': 80, 'u_i': 3.1608},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
