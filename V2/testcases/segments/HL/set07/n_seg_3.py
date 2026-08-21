"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400006, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400006, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.175817, 'e_o_k': [0.036028, 0.028822, 0.023058], 'p_i': 10, 'u_i': 3.9277},
        {'id': 1, 'e_m': 0.569763, 'e_o_k': [0.116755, 0.093404, 0.074723], 'p_i': 20, 'u_i': 1.1365},
        {'id': 2, 'e_m': 2.984963, 'e_o_k': [0.611673, 0.489338, 0.391471], 'p_i': 40, 'u_i': 1.9653},
        {'id': 3, 'e_m': 1.604801, 'e_o_k': [0.328853, 0.263082, 0.210466], 'p_i': 80, 'u_i': 1.4843},
        {'id': 4, 'e_m': 0.625370, 'e_o_k': [0.128150, 0.102520, 0.082016], 'p_i': 10, 'u_i': 4.5666},
        {'id': 5, 'e_m': 1.194963, 'e_o_k': [0.244869, 0.195896, 0.156716], 'p_i': 20, 'u_i': 2.1776},
        {'id': 6, 'e_m': 4.162884, 'e_o_k': [0.853050, 0.682440, 0.545952], 'p_i': 10, 'u_i': 3.5354},
        {'id': 7, 'e_m': 9.653801, 'e_o_k': [1.978238, 1.582590, 1.266072], 'p_i': 80, 'u_i': 3.2835},
    ]
    B_BUDGET = 110.400006
    return processors, tasks, B_BUDGET
