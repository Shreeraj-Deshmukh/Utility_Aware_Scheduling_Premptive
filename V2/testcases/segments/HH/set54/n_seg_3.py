"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639997, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639997, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.060089, 'e_o_k': [1.182018, 0.945614, 0.756492], 'p_i': 10, 'u_i': 3.7892},
        {'id': 1, 'e_m': 0.339026, 'e_o_k': [0.194523, 0.155618, 0.124495], 'p_i': 20, 'u_i': 2.5683},
        {'id': 2, 'e_m': 15.847193, 'e_o_k': [9.092652, 7.274121, 5.819297], 'p_i': 40, 'u_i': 1.2577},
        {'id': 3, 'e_m': 1.762893, 'e_o_k': [1.011496, 0.809197, 0.647357], 'p_i': 80, 'u_i': 3.4086},
        {'id': 4, 'e_m': 0.784991, 'e_o_k': [0.450404, 0.360324, 0.288259], 'p_i': 40, 'u_i': 3.2935},
        {'id': 5, 'e_m': 0.814426, 'e_o_k': [0.467294, 0.373835, 0.299068], 'p_i': 10, 'u_i': 4.9988},
        {'id': 6, 'e_m': 0.165452, 'e_o_k': [0.094932, 0.075945, 0.060756], 'p_i': 20, 'u_i': 2.8879},
        {'id': 7, 'e_m': 0.989677, 'e_o_k': [0.567847, 0.454278, 0.363422], 'p_i': 20, 'u_i': 4.7528},
    ]
    B_BUDGET = 176.639997
    return processors, tasks, B_BUDGET
