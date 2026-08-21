"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.240581, 'e_o_k': [0.040749, 0.032599, 0.026079, 0.020863], 'p_i': 10, 'u_i': 1.4256},
        {'id': 1, 'e_m': 5.487231, 'e_o_k': [1.524231, 1.219385], 'p_i': 20, 'u_i': 3.1325},
        {'id': 2, 'e_m': 6.057455, 'e_o_k': [1.682626, 1.346101], 'p_i': 40, 'u_i': 4.7073},
        {'id': 3, 'e_m': 28.011520, 'e_o_k': [3.796340, 3.037072, 2.429657, 1.943726, 1.554981, 1.243985], 'p_i': 80, 'u_i': 3.8560},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
