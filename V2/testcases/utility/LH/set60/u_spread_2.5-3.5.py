"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320017, "H": 80, "J": 35, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "utility", "util_per_core": 0.2, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 88.320017, "H": 80, "J": 35, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "utility", "util_per_core": 0.2, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.728311, 'e_o_k': [0.345405, 0.276324, 0.221059, 0.176847], 'p_i': 10, 'u_i': 3.4992},
        {'id': 1, 'e_m': 3.236491, 'e_o_k': [1.857003, 1.485603, 1.188482], 'p_i': 20, 'u_i': 3.0421},
        {'id': 2, 'e_m': 0.535015, 'e_o_k': [0.306976, 0.245581, 0.196465], 'p_i': 40, 'u_i': 2.6208},
        {'id': 3, 'e_m': 4.750488, 'e_o_k': [1.802705, 1.442164, 1.153731, 0.922985, 0.738388, 0.590710], 'p_i': 80, 'u_i': 2.7262},
        {'id': 4, 'e_m': 0.182718, 'e_o_k': [0.142114, 0.113691], 'p_i': 40, 'u_i': 3.3519},
        {'id': 5, 'e_m': 0.092022, 'e_o_k': [0.052800, 0.042240, 0.033792], 'p_i': 10, 'u_i': 3.1505},
        {'id': 6, 'e_m': 2.641333, 'e_o_k': [1.252665, 1.002132, 0.801706, 0.641364], 'p_i': 40, 'u_i': 3.4697},
        {'id': 7, 'e_m': 0.127844, 'e_o_k': [0.060631, 0.048504, 0.038804, 0.031043], 'p_i': 10, 'u_i': 3.0093},
    ]
    B_BUDGET = 88.320017
    return processors, tasks, B_BUDGET
