"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64001, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.64001, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.625813, 'e_o_k': [0.677100, 0.541680, 0.433344, 0.346675, 0.277340], 'p_i': 10, 'u_i': 4.4263},
        {'id': 1, 'e_m': 9.707566, 'e_o_k': [5.569915, 4.455932, 3.564745], 'p_i': 20, 'u_i': 1.7162},
        {'id': 2, 'e_m': 0.282585, 'e_o_k': [0.219788, 0.175830], 'p_i': 40, 'u_i': 1.4626},
        {'id': 3, 'e_m': 2.321296, 'e_o_k': [1.805453, 1.444362], 'p_i': 80, 'u_i': 2.2690},
        {'id': 4, 'e_m': 0.529719, 'e_o_k': [0.303937, 0.243150, 0.194520], 'p_i': 10, 'u_i': 1.2408},
        {'id': 5, 'e_m': 5.039015, 'e_o_k': [3.919234, 3.135387], 'p_i': 80, 'u_i': 2.2030},
    ]
    B_BUDGET = 176.640010
    return processors, tasks, B_BUDGET
