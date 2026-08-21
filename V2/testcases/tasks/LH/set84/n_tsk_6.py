"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320016, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320016, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.335308, 'e_o_k': [0.127242, 0.101794, 0.081435, 0.065148, 0.052118, 0.041695], 'p_i': 10, 'u_i': 3.3883},
        {'id': 1, 'e_m': 0.532174, 'e_o_k': [0.221634, 0.177307, 0.141846, 0.113477, 0.090781], 'p_i': 20, 'u_i': 2.1673},
        {'id': 2, 'e_m': 3.423766, 'e_o_k': [1.299243, 1.039395, 0.831516, 0.665213, 0.532170, 0.425736], 'p_i': 40, 'u_i': 3.4649},
        {'id': 3, 'e_m': 2.134665, 'e_o_k': [1.012375, 0.809900, 0.647920, 0.518336], 'p_i': 80, 'u_i': 2.8434},
        {'id': 4, 'e_m': 0.350071, 'e_o_k': [0.200860, 0.160688, 0.128551], 'p_i': 20, 'u_i': 4.3788},
        {'id': 5, 'e_m': 2.100795, 'e_o_k': [0.996312, 0.797049, 0.637640, 0.510112], 'p_i': 10, 'u_i': 3.2500},
    ]
    B_BUDGET = 88.320016
    return processors, tasks, B_BUDGET
