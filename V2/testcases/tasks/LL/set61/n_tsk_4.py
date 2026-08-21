"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.754933, 'e_o_k': [0.127868, 0.102294, 0.081836, 0.065468], 'p_i': 10, 'u_i': 3.2224},
        {'id': 1, 'e_m': 2.776976, 'e_o_k': [0.771382, 0.617106], 'p_i': 20, 'u_i': 2.5978},
        {'id': 2, 'e_m': 0.073202, 'e_o_k': [0.015000, 0.012000, 0.009600], 'p_i': 40, 'u_i': 4.5124},
        {'id': 3, 'e_m': 14.706228, 'e_o_k': [2.490892, 1.992714, 1.594171, 1.275337], 'p_i': 80, 'u_i': 4.6729},
    ]
    B_BUDGET = 55.199993
    return processors, tasks, B_BUDGET
