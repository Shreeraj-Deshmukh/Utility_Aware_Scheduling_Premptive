"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.143336, 'e_o_k': [0.595371, 0.476297], 'p_i': 10, 'u_i': 1.5090},
        {'id': 1, 'e_m': 1.413954, 'e_o_k': [0.392765, 0.314212], 'p_i': 20, 'u_i': 1.7367},
        {'id': 2, 'e_m': 3.402871, 'e_o_k': [0.945242, 0.756193], 'p_i': 40, 'u_i': 1.3712},
        {'id': 3, 'e_m': 12.001313, 'e_o_k': [3.333698, 2.666959], 'p_i': 80, 'u_i': 4.1249},
        {'id': 4, 'e_m': 0.888149, 'e_o_k': [0.246708, 0.197367], 'p_i': 40, 'u_i': 3.5067},
        {'id': 5, 'e_m': 2.314711, 'e_o_k': [0.642975, 0.514380], 'p_i': 40, 'u_i': 2.5623},
        {'id': 6, 'e_m': 10.156802, 'e_o_k': [2.821334, 2.257067], 'p_i': 80, 'u_i': 1.7025},
        {'id': 7, 'e_m': 0.728490, 'e_o_k': [0.202358, 0.161887], 'p_i': 10, 'u_i': 4.1731},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
