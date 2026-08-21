"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199991, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199991, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.489096, 'e_o_k': [0.066286, 0.053029, 0.042423, 0.033938, 0.027151, 0.021721], 'p_i': 10, 'u_i': 1.1924},
        {'id': 1, 'e_m': 1.364837, 'e_o_k': [0.279680, 0.223744, 0.178995], 'p_i': 20, 'u_i': 4.9854},
        {'id': 2, 'e_m': 4.474162, 'e_o_k': [1.242823, 0.994258], 'p_i': 40, 'u_i': 2.6844},
        {'id': 3, 'e_m': 8.740934, 'e_o_k': [1.184640, 0.947712, 0.758169, 0.606535, 0.485228, 0.388183], 'p_i': 80, 'u_i': 3.2251},
        {'id': 4, 'e_m': 0.318567, 'e_o_k': [0.065280, 0.052224, 0.041779], 'p_i': 10, 'u_i': 4.0273},
        {'id': 5, 'e_m': 2.390086, 'e_o_k': [0.489772, 0.391817, 0.313454], 'p_i': 80, 'u_i': 2.2476},
    ]
    B_BUDGET = 55.199991
    return processors, tasks, B_BUDGET
