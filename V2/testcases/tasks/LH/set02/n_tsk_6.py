"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.489096, 'e_o_k': [0.185601, 0.148481, 0.118785, 0.095028, 0.076022, 0.060818], 'p_i': 10, 'u_i': 1.1924},
        {'id': 1, 'e_m': 1.364837, 'e_o_k': [0.783103, 0.626482, 0.501186], 'p_i': 20, 'u_i': 4.9854},
        {'id': 2, 'e_m': 4.474162, 'e_o_k': [3.479904, 2.783923], 'p_i': 40, 'u_i': 2.6844},
        {'id': 3, 'e_m': 8.740934, 'e_o_k': [3.316991, 2.653593, 2.122874, 1.698299, 1.358639, 1.086912], 'p_i': 80, 'u_i': 3.2251},
        {'id': 4, 'e_m': 0.318567, 'e_o_k': [0.182785, 0.146228, 0.116982], 'p_i': 10, 'u_i': 4.0273},
        {'id': 5, 'e_m': 2.390086, 'e_o_k': [1.371361, 1.097089, 0.877671], 'p_i': 80, 'u_i': 2.2476},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET
