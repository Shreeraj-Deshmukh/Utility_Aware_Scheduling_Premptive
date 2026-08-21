"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199997, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199997, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.475493, 'e_o_k': [0.080537, 0.064430, 0.051544, 0.041235], 'p_i': 10, 'u_i': 1.4304},
        {'id': 1, 'e_m': 2.468602, 'e_o_k': [0.367177, 0.293741, 0.234993, 0.187994, 0.150396], 'p_i': 20, 'u_i': 2.0301},
        {'id': 2, 'e_m': 3.424018, 'e_o_k': [0.509284, 0.407427, 0.325942, 0.260753, 0.208603], 'p_i': 40, 'u_i': 4.4775},
        {'id': 3, 'e_m': 5.713174, 'e_o_k': [0.774294, 0.619435, 0.495548, 0.396438, 0.317151, 0.253721], 'p_i': 80, 'u_i': 1.0830},
        {'id': 4, 'e_m': 3.406818, 'e_o_k': [0.946338, 0.757071], 'p_i': 80, 'u_i': 1.9156},
        {'id': 5, 'e_m': 2.353620, 'e_o_k': [0.318981, 0.255185, 0.204148, 0.163318, 0.130655, 0.104524], 'p_i': 80, 'u_i': 2.8864},
    ]
    B_BUDGET = 55.199997
    return processors, tasks, B_BUDGET
