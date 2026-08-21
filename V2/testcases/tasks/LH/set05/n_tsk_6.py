"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319993, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319993, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.541647, 'e_o_k': [0.205543, 0.164435, 0.131548, 0.105238, 0.084190, 0.067352], 'p_i': 10, 'u_i': 3.6469},
        {'id': 1, 'e_m': 0.175727, 'e_o_k': [0.073185, 0.058548, 0.046838, 0.037471, 0.029976], 'p_i': 20, 'u_i': 1.4903},
        {'id': 2, 'e_m': 2.520518, 'e_o_k': [1.195368, 0.956294, 0.765035, 0.612028], 'p_i': 40, 'u_i': 2.4704},
        {'id': 3, 'e_m': 1.402618, 'e_o_k': [0.804781, 0.643825, 0.515060], 'p_i': 80, 'u_i': 4.2349},
        {'id': 4, 'e_m': 4.379465, 'e_o_k': [1.661910, 1.329528, 1.063622, 0.850898, 0.680718, 0.544575], 'p_i': 40, 'u_i': 4.1771},
        {'id': 5, 'e_m': 5.880664, 'e_o_k': [2.788933, 2.231146, 1.784917, 1.427934], 'p_i': 40, 'u_i': 4.0903},
    ]
    B_BUDGET = 88.319993
    return processors, tasks, B_BUDGET
