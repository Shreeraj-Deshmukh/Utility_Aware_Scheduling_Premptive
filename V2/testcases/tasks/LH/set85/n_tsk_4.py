"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.546811, 'e_o_k': [0.207503, 0.166002, 0.132802, 0.106241, 0.084993, 0.067995], 'p_i': 10, 'u_i': 4.7125},
        {'id': 1, 'e_m': 1.198359, 'e_o_k': [0.568328, 0.454662, 0.363730, 0.290984], 'p_i': 20, 'u_i': 3.2766},
        {'id': 2, 'e_m': 3.939056, 'e_o_k': [3.063711, 2.450968], 'p_i': 40, 'u_i': 2.3226},
        {'id': 3, 'e_m': 14.953960, 'e_o_k': [11.630858, 9.304686], 'p_i': 80, 'u_i': 1.3159},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET
