"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759992, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759992, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.840893, 'e_o_k': [0.140149, 0.112119], 'p_i': 10, 'u_i': 2.9208},
        {'id': 1, 'e_m': 3.409844, 'e_o_k': [0.277277, 0.221822, 0.177457, 0.141966, 0.113573, 0.090858], 'p_i': 20, 'u_i': 4.6964},
        {'id': 2, 'e_m': 7.929922, 'e_o_k': [0.974990, 0.779992, 0.623994], 'p_i': 40, 'u_i': 4.6519},
        {'id': 3, 'e_m': 2.760194, 'e_o_k': [0.460032, 0.368026], 'p_i': 80, 'u_i': 4.9020},
        {'id': 4, 'e_m': 0.467952, 'e_o_k': [0.038052, 0.030442, 0.024353, 0.019483, 0.015586, 0.012469], 'p_i': 80, 'u_i': 1.1409},
        {'id': 5, 'e_m': 2.370549, 'e_o_k': [0.211555, 0.169244, 0.135395, 0.108316, 0.086653], 'p_i': 40, 'u_i': 1.3844},
        {'id': 6, 'e_m': 3.563156, 'e_o_k': [0.317988, 0.254390, 0.203512, 0.162810, 0.130248], 'p_i': 80, 'u_i': 3.8571},
        {'id': 7, 'e_m': 0.060309, 'e_o_k': [0.010051, 0.008041], 'p_i': 20, 'u_i': 3.6185},
    ]
    B_BUDGET = 71.759992
    return processors, tasks, B_BUDGET
