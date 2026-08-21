"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.399738, 'e_o_k': [0.388816, 0.311053], 'p_i': 10, 'u_i': 4.3165},
        {'id': 1, 'e_m': 1.192176, 'e_o_k': [0.331160, 0.264928], 'p_i': 20, 'u_i': 4.1600},
        {'id': 2, 'e_m': 0.850246, 'e_o_k': [0.126465, 0.101172, 0.080937, 0.064750, 0.051800], 'p_i': 40, 'u_i': 2.4258},
        {'id': 3, 'e_m': 1.297044, 'e_o_k': [0.219689, 0.175751, 0.140601, 0.112481], 'p_i': 80, 'u_i': 2.6711},
        {'id': 4, 'e_m': 12.521523, 'e_o_k': [1.697014, 1.357612, 1.086089, 0.868871, 0.695097, 0.556078], 'p_i': 80, 'u_i': 3.0914},
        {'id': 5, 'e_m': 0.064292, 'e_o_k': [0.010890, 0.008712, 0.006969, 0.005575], 'p_i': 10, 'u_i': 2.6989},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
