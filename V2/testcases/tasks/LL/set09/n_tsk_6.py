"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200006, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200006, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.160726, 'e_o_k': [0.237854, 0.190283, 0.152226], 'p_i': 10, 'u_i': 2.0997},
        {'id': 1, 'e_m': 0.933941, 'e_o_k': [0.259428, 0.207542], 'p_i': 20, 'u_i': 1.8132},
        {'id': 2, 'e_m': 5.441884, 'e_o_k': [0.737527, 0.590021, 0.472017, 0.377614, 0.302091, 0.241673], 'p_i': 40, 'u_i': 1.3118},
        {'id': 3, 'e_m': 2.243130, 'e_o_k': [0.333640, 0.266912, 0.213530, 0.170824, 0.136659], 'p_i': 80, 'u_i': 1.6432},
        {'id': 4, 'e_m': 0.117552, 'e_o_k': [0.032653, 0.026123], 'p_i': 20, 'u_i': 3.2827},
        {'id': 5, 'e_m': 1.345331, 'e_o_k': [0.200103, 0.160082, 0.128066, 0.102453, 0.081962], 'p_i': 20, 'u_i': 1.0597},
    ]
    B_BUDGET = 55.200006
    return processors, tasks, B_BUDGET
