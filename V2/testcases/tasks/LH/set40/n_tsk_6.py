"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.846222, 'e_o_k': [0.401325, 0.321060, 0.256848, 0.205478], 'p_i': 10, 'u_i': 3.4352},
        {'id': 1, 'e_m': 0.836504, 'e_o_k': [0.396716, 0.317373, 0.253898, 0.203119], 'p_i': 20, 'u_i': 3.4020},
        {'id': 2, 'e_m': 4.190220, 'e_o_k': [2.404224, 1.923379, 1.538704], 'p_i': 40, 'u_i': 3.4221},
        {'id': 3, 'e_m': 5.291011, 'e_o_k': [2.203539, 1.762831, 1.410265, 1.128212, 0.902569], 'p_i': 80, 'u_i': 3.9841},
        {'id': 4, 'e_m': 0.605237, 'e_o_k': [0.347267, 0.277814, 0.222251], 'p_i': 40, 'u_i': 2.4868},
        {'id': 5, 'e_m': 0.875285, 'e_o_k': [0.332151, 0.265721, 0.212577, 0.170062, 0.136049, 0.108839], 'p_i': 10, 'u_i': 2.1829},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET
