"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640015, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640015, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.730494, 'e_o_k': [1.345940, 1.076752], 'p_i': 10, 'u_i': 2.4127},
        {'id': 1, 'e_m': 2.545488, 'e_o_k': [1.979824, 1.583859], 'p_i': 20, 'u_i': 2.1691},
        {'id': 2, 'e_m': 16.173972, 'e_o_k': [12.579756, 10.063805], 'p_i': 40, 'u_i': 3.6581},
        {'id': 3, 'e_m': 7.626156, 'e_o_k': [3.176053, 2.540842, 2.032674, 1.626139, 1.300911], 'p_i': 80, 'u_i': 4.4037},
    ]
    B_BUDGET = 176.640015
    return processors, tasks, B_BUDGET
