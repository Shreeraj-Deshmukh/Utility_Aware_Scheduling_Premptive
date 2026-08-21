"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.770853, 'e_o_k': [0.292522, 0.234017, 0.187214, 0.149771, 0.119817, 0.095854], 'p_i': 10, 'u_i': 4.6443},
        {'id': 1, 'e_m': 5.496848, 'e_o_k': [2.085932, 1.668746, 1.334997, 1.067997, 0.854398, 0.683518], 'p_i': 20, 'u_i': 3.3399},
        {'id': 2, 'e_m': 0.244179, 'e_o_k': [0.092660, 0.074128, 0.059303, 0.047442, 0.037954, 0.030363], 'p_i': 40, 'u_i': 3.1360},
        {'id': 3, 'e_m': 3.357422, 'e_o_k': [1.926390, 1.541112, 1.232890], 'p_i': 80, 'u_i': 4.9615},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
