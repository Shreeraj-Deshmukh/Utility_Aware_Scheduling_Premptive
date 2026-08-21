"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 25, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 25, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.573508, 'e_o_k': [0.401456, 0.401456], 'p_i': 10, 'u_i': 2.5980},
        {'id': 1, 'e_m': 1.886878, 'e_o_k': [1.320814, 1.320814], 'p_i': 20, 'u_i': 2.9083},
        {'id': 2, 'e_m': 2.675239, 'e_o_k': [1.248445, 1.248445, 1.248445], 'p_i': 40, 'u_i': 4.8275},
        {'id': 3, 'e_m': 8.484623, 'e_o_k': [2.375695, 2.375695, 2.375695, 2.375695, 2.375695], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 0.549748, 'e_o_k': [0.256549, 0.256549, 0.256549], 'p_i': 20, 'u_i': 1.8333},
        {'id': 5, 'e_m': 0.074482, 'e_o_k': [0.020855, 0.020855, 0.020855, 0.020855, 0.020855], 'p_i': 20, 'u_i': 4.5368},
        {'id': 6, 'e_m': 1.648956, 'e_o_k': [0.384756, 0.384756, 0.384756, 0.384756, 0.384756, 0.384756], 'p_i': 80, 'u_i': 4.6383},
        {'id': 7, 'e_m': 1.883445, 'e_o_k': [0.527365, 0.527365, 0.527365, 0.527365, 0.527365], 'p_i': 80, 'u_i': 3.5515},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
