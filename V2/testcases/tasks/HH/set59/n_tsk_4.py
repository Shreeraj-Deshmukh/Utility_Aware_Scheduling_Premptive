"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.240581, 'e_o_k': [0.114097, 0.091277, 0.073022, 0.058417], 'p_i': 10, 'u_i': 1.4256},
        {'id': 1, 'e_m': 5.487231, 'e_o_k': [4.267846, 3.414277], 'p_i': 20, 'u_i': 3.1325},
        {'id': 2, 'e_m': 6.057455, 'e_o_k': [4.711354, 3.769083], 'p_i': 40, 'u_i': 4.7073},
        {'id': 3, 'e_m': 28.011520, 'e_o_k': [10.629751, 8.503801, 6.803041, 5.442432, 4.353946, 3.483157], 'p_i': 80, 'u_i': 3.8560},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET
