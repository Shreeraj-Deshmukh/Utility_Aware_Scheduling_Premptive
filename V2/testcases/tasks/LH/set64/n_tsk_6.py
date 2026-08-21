"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32002, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.32002, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.972467, 'e_o_k': [0.461197, 0.368958, 0.295166, 0.236133], 'p_i': 10, 'u_i': 2.8432},
        {'id': 1, 'e_m': 3.104081, 'e_o_k': [1.781030, 1.424824, 1.139859], 'p_i': 20, 'u_i': 4.5844},
        {'id': 2, 'e_m': 1.034213, 'e_o_k': [0.804388, 0.643510], 'p_i': 40, 'u_i': 1.8342},
        {'id': 3, 'e_m': 2.973567, 'e_o_k': [1.706145, 1.364916, 1.091933], 'p_i': 80, 'u_i': 2.1428},
        {'id': 4, 'e_m': 0.732465, 'e_o_k': [0.347375, 0.277900, 0.222320, 0.177856], 'p_i': 10, 'u_i': 3.7337},
        {'id': 5, 'e_m': 0.451117, 'e_o_k': [0.187876, 0.150301, 0.120241, 0.096192, 0.076954], 'p_i': 40, 'u_i': 3.4112},
    ]
    B_BUDGET = 88.320020
    return processors, tasks, B_BUDGET
