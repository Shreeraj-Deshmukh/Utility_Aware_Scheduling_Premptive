"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.073055, 'e_o_k': [1.189458, 0.951566, 0.761253], 'p_i': 10, 'u_i': 2.4204},
        {'id': 1, 'e_m': 0.267192, 'e_o_k': [0.101393, 0.081115, 0.064892, 0.051913, 0.041531, 0.033225], 'p_i': 20, 'u_i': 4.6440},
        {'id': 2, 'e_m': 1.486671, 'e_o_k': [0.564159, 0.451327, 0.361062, 0.288849, 0.231079, 0.184864], 'p_i': 40, 'u_i': 4.0628},
        {'id': 3, 'e_m': 11.373449, 'e_o_k': [4.736682, 3.789345, 3.031476, 2.425181, 1.940145], 'p_i': 80, 'u_i': 1.2692},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
