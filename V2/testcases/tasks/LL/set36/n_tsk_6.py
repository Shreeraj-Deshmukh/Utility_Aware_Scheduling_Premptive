"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.643703, 'e_o_k': [0.131906, 0.105525, 0.084420], 'p_i': 10, 'u_i': 1.0054},
        {'id': 1, 'e_m': 0.506012, 'e_o_k': [0.085707, 0.068565, 0.054852, 0.043882], 'p_i': 20, 'u_i': 3.4815},
        {'id': 2, 'e_m': 0.577286, 'e_o_k': [0.160357, 0.128286], 'p_i': 40, 'u_i': 3.3828},
        {'id': 3, 'e_m': 3.591706, 'e_o_k': [0.608351, 0.486681, 0.389345, 0.311476], 'p_i': 80, 'u_i': 4.2011},
        {'id': 4, 'e_m': 9.654735, 'e_o_k': [1.635287, 1.308230, 1.046584, 0.837267], 'p_i': 40, 'u_i': 4.7650},
        {'id': 5, 'e_m': 0.770579, 'e_o_k': [0.157906, 0.126324, 0.101060], 'p_i': 80, 'u_i': 4.1252},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET
