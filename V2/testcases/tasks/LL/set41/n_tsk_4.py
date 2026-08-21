"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.20001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.20001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.950399, 'e_o_k': [0.264000, 0.211200], 'p_i': 10, 'u_i': 1.8275},
        {'id': 1, 'e_m': 1.993422, 'e_o_k': [0.553728, 0.442983], 'p_i': 20, 'u_i': 3.9821},
        {'id': 2, 'e_m': 8.136855, 'e_o_k': [1.102770, 0.882216, 0.705773, 0.564618, 0.451695, 0.361356], 'p_i': 40, 'u_i': 4.4924},
        {'id': 3, 'e_m': 0.149413, 'e_o_k': [0.030617, 0.024494, 0.019595], 'p_i': 80, 'u_i': 4.2054},
    ]
    B_BUDGET = 55.200010
    return processors, tasks, B_BUDGET
