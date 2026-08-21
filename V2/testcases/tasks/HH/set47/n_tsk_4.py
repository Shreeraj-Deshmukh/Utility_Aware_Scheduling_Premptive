"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.567714, 'e_o_k': [1.902308, 1.521847, 1.217477, 0.973982, 0.779185], 'p_i': 10, 'u_i': 1.7421},
        {'id': 1, 'e_m': 2.660477, 'e_o_k': [1.009592, 0.807674, 0.646139, 0.516911, 0.413529, 0.330823], 'p_i': 20, 'u_i': 1.9951},
        {'id': 2, 'e_m': 4.513749, 'e_o_k': [3.510693, 2.808555], 'p_i': 40, 'u_i': 1.2617},
        {'id': 3, 'e_m': 7.788884, 'e_o_k': [2.955709, 2.364567, 1.891654, 1.513323, 1.210658, 0.968527], 'p_i': 80, 'u_i': 4.5683},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET
