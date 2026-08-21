"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639995, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639995, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.175817, 'e_o_k': [0.100879, 0.080703, 0.064562], 'p_i': 10, 'u_i': 3.9277},
        {'id': 1, 'e_m': 0.569763, 'e_o_k': [0.326913, 0.261531, 0.209225], 'p_i': 20, 'u_i': 1.1365},
        {'id': 2, 'e_m': 2.984963, 'e_o_k': [1.712684, 1.370147, 1.096118], 'p_i': 40, 'u_i': 1.9653},
        {'id': 3, 'e_m': 1.604801, 'e_o_k': [0.920787, 0.736630, 0.589304], 'p_i': 80, 'u_i': 1.4843},
        {'id': 4, 'e_m': 0.625370, 'e_o_k': [0.358819, 0.287055, 0.229644], 'p_i': 10, 'u_i': 4.5666},
        {'id': 5, 'e_m': 1.194963, 'e_o_k': [0.685634, 0.548507, 0.438806], 'p_i': 20, 'u_i': 2.1776},
        {'id': 6, 'e_m': 4.162884, 'e_o_k': [2.388540, 1.910832, 1.528665], 'p_i': 10, 'u_i': 3.5354},
        {'id': 7, 'e_m': 9.653801, 'e_o_k': [5.539066, 4.431253, 3.545002], 'p_i': 80, 'u_i': 3.2835},
    ]
    B_BUDGET = 176.639995
    return processors, tasks, B_BUDGET
