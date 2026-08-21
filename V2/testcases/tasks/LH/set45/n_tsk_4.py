"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.110152, 'e_o_k': [0.085674, 0.068539], 'p_i': 10, 'u_i': 3.8084},
        {'id': 1, 'e_m': 1.382030, 'e_o_k': [0.575572, 0.460457, 0.368366, 0.294693, 0.235754], 'p_i': 20, 'u_i': 2.8237},
        {'id': 2, 'e_m': 0.048486, 'e_o_k': [0.037711, 0.030169], 'p_i': 40, 'u_i': 2.8601},
        {'id': 3, 'e_m': 25.493694, 'e_o_k': [12.090505, 9.672404, 7.737923, 6.190339], 'p_i': 80, 'u_i': 4.7969},
    ]
    B_BUDGET = 88.320006
    return processors, tasks, B_BUDGET
