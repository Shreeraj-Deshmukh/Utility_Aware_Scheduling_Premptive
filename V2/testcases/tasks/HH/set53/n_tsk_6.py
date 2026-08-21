"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.63999, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.63999, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.441716, 'e_o_k': [0.167621, 0.134097, 0.107278, 0.085822, 0.068658, 0.054926], 'p_i': 10, 'u_i': 2.3061},
        {'id': 1, 'e_m': 3.450901, 'e_o_k': [2.684034, 2.147227], 'p_i': 20, 'u_i': 3.0150},
        {'id': 2, 'e_m': 2.918010, 'e_o_k': [1.215259, 0.972207, 0.777766, 0.622212, 0.497770], 'p_i': 40, 'u_i': 1.0989},
        {'id': 3, 'e_m': 16.308239, 'e_o_k': [9.357186, 7.485749, 5.988599], 'p_i': 80, 'u_i': 1.3802},
        {'id': 4, 'e_m': 3.302699, 'e_o_k': [1.375469, 1.100376, 0.880300, 0.704240, 0.563392], 'p_i': 40, 'u_i': 2.4137},
        {'id': 5, 'e_m': 17.913011, 'e_o_k': [13.932342, 11.145873], 'p_i': 80, 'u_i': 1.6729},
    ]
    B_BUDGET = 176.639990
    return processors, tasks, B_BUDGET
