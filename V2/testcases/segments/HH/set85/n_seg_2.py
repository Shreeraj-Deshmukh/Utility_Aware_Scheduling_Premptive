"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.488440, 'e_o_k': [0.379898, 0.303918], 'p_i': 10, 'u_i': 1.2408},
        {'id': 1, 'e_m': 0.924655, 'e_o_k': [0.719176, 0.575341], 'p_i': 20, 'u_i': 2.7274},
        {'id': 2, 'e_m': 2.288327, 'e_o_k': [1.779810, 1.423848], 'p_i': 40, 'u_i': 3.7398},
        {'id': 3, 'e_m': 4.657210, 'e_o_k': [3.622275, 2.897820], 'p_i': 80, 'u_i': 1.4758},
        {'id': 4, 'e_m': 0.144768, 'e_o_k': [0.112597, 0.090078], 'p_i': 10, 'u_i': 4.3036},
        {'id': 5, 'e_m': 0.140954, 'e_o_k': [0.109631, 0.087705], 'p_i': 40, 'u_i': 3.9596},
        {'id': 6, 'e_m': 4.924673, 'e_o_k': [3.830301, 3.064241], 'p_i': 20, 'u_i': 3.9830},
        {'id': 7, 'e_m': 3.252657, 'e_o_k': [2.529844, 2.023875], 'p_i': 10, 'u_i': 3.3191},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
