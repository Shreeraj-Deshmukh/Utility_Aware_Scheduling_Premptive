"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.130152, 'e_o_k': [0.026671, 0.021336, 0.017069], 'p_i': 10, 'u_i': 3.2721},
        {'id': 1, 'e_m': 0.967654, 'e_o_k': [0.268793, 0.215034], 'p_i': 20, 'u_i': 2.5377},
        {'id': 2, 'e_m': 4.222704, 'e_o_k': [1.172973, 0.938379], 'p_i': 40, 'u_i': 2.5387},
        {'id': 3, 'e_m': 18.642755, 'e_o_k': [3.157648, 2.526118, 2.020895, 1.616716], 'p_i': 80, 'u_i': 1.0056},
    ]
    B_BUDGET = 55.199991
    return processors, tasks, B_BUDGET
