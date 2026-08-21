"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.071668, 'e_o_k': [0.297686, 0.238148], 'p_i': 10, 'u_i': 1.5090},
        {'id': 1, 'e_m': 0.706977, 'e_o_k': [0.196383, 0.157106], 'p_i': 20, 'u_i': 1.7367},
        {'id': 2, 'e_m': 1.701435, 'e_o_k': [0.472621, 0.378097], 'p_i': 40, 'u_i': 1.3712},
        {'id': 3, 'e_m': 6.000657, 'e_o_k': [1.666849, 1.333479], 'p_i': 80, 'u_i': 4.1249},
        {'id': 4, 'e_m': 0.444075, 'e_o_k': [0.123354, 0.098683], 'p_i': 40, 'u_i': 3.5067},
        {'id': 5, 'e_m': 1.157355, 'e_o_k': [0.321488, 0.257190], 'p_i': 40, 'u_i': 2.5623},
        {'id': 6, 'e_m': 5.078401, 'e_o_k': [1.410667, 1.128534], 'p_i': 80, 'u_i': 1.7025},
        {'id': 7, 'e_m': 0.364245, 'e_o_k': [0.101179, 0.080943], 'p_i': 10, 'u_i': 4.1731},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
