"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.231133, 'e_o_k': [0.039149, 0.031319, 0.025055, 0.020044], 'p_i': 10, 'u_i': 4.2108},
        {'id': 1, 'e_m': 1.903134, 'e_o_k': [0.389986, 0.311989, 0.249591], 'p_i': 20, 'u_i': 3.3354},
        {'id': 2, 'e_m': 9.454475, 'e_o_k': [1.601368, 1.281094, 1.024875, 0.819900], 'p_i': 40, 'u_i': 1.0371},
        {'id': 3, 'e_m': 3.629449, 'e_o_k': [0.539840, 0.431872, 0.345497, 0.276398, 0.221118], 'p_i': 80, 'u_i': 1.4152},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
