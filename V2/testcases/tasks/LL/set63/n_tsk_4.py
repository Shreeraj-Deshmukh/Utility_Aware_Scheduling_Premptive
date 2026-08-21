"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200015, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200015, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.664276, 'e_o_k': [0.247542, 0.198034, 0.158427, 0.126742, 0.101393], 'p_i': 10, 'u_i': 4.0082},
        {'id': 1, 'e_m': 0.037732, 'e_o_k': [0.005114, 0.004091, 0.003273, 0.002618, 0.002095, 0.001676], 'p_i': 20, 'u_i': 3.2625},
        {'id': 2, 'e_m': 4.249107, 'e_o_k': [0.870719, 0.696575, 0.557260], 'p_i': 40, 'u_i': 3.4071},
        {'id': 3, 'e_m': 10.036655, 'e_o_k': [1.492839, 1.194271, 0.955417, 0.764334, 0.611467], 'p_i': 80, 'u_i': 2.2919},
    ]
    B_BUDGET = 55.200015
    return processors, tasks, B_BUDGET
