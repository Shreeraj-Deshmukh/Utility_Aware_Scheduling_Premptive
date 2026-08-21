"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.083997, 'e_o_k': [0.017212, 0.013770, 0.011016], 'p_i': 10, 'u_i': 2.9413},
        {'id': 1, 'e_m': 1.581251, 'e_o_k': [0.324027, 0.259221, 0.207377], 'p_i': 20, 'u_i': 2.0448},
        {'id': 2, 'e_m': 10.971554, 'e_o_k': [1.631895, 1.305516, 1.044413, 0.835530, 0.668424], 'p_i': 40, 'u_i': 1.6984},
        {'id': 3, 'e_m': 3.059915, 'e_o_k': [0.518278, 0.414623, 0.331698, 0.265358], 'p_i': 80, 'u_i': 3.4597},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
