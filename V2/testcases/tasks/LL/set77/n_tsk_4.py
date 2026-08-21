"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.493963, 'e_o_k': [0.073471, 0.058777, 0.047022, 0.037617, 0.030094], 'p_i': 10, 'u_i': 1.8790},
        {'id': 1, 'e_m': 3.730438, 'e_o_k': [0.554861, 0.443888, 0.355111, 0.284089, 0.227271], 'p_i': 20, 'u_i': 3.3534},
        {'id': 2, 'e_m': 4.298707, 'e_o_k': [0.880883, 0.704706, 0.563765], 'p_i': 40, 'u_i': 2.5184},
        {'id': 3, 'e_m': 4.529127, 'e_o_k': [0.673656, 0.538925, 0.431140, 0.344912, 0.275930], 'p_i': 80, 'u_i': 4.2996},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET
