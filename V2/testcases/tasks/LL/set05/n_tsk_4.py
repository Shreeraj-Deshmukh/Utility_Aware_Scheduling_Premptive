"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200016, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200016, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.861356, 'e_o_k': [0.116738, 0.093390, 0.074712, 0.059770, 0.047816, 0.038253], 'p_i': 10, 'u_i': 3.5509},
        {'id': 1, 'e_m': 0.314912, 'e_o_k': [0.053339, 0.042671, 0.034137, 0.027309], 'p_i': 20, 'u_i': 2.4298},
        {'id': 2, 'e_m': 5.515709, 'e_o_k': [1.130268, 0.904215, 0.723372], 'p_i': 40, 'u_i': 2.9531},
        {'id': 3, 'e_m': 12.818090, 'e_o_k': [1.737207, 1.389766, 1.111813, 0.889450, 0.711560, 0.569248], 'p_i': 80, 'u_i': 4.5727},
    ]
    B_BUDGET = 55.200016
    return processors, tasks, B_BUDGET
