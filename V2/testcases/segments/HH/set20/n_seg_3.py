"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639997, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639997, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.143336, 'e_o_k': [1.229783, 0.983826, 0.787061], 'p_i': 10, 'u_i': 1.5090},
        {'id': 1, 'e_m': 1.413954, 'e_o_k': [0.811285, 0.649028, 0.519222], 'p_i': 20, 'u_i': 1.7367},
        {'id': 2, 'e_m': 3.402871, 'e_o_k': [1.952467, 1.561973, 1.249579], 'p_i': 40, 'u_i': 1.3712},
        {'id': 3, 'e_m': 12.001313, 'e_o_k': [6.885999, 5.508800, 4.407040], 'p_i': 80, 'u_i': 4.1249},
        {'id': 4, 'e_m': 0.888149, 'e_o_k': [0.509594, 0.407675, 0.326140], 'p_i': 40, 'u_i': 3.5067},
        {'id': 5, 'e_m': 2.314711, 'e_o_k': [1.328113, 1.062490, 0.849992], 'p_i': 40, 'u_i': 2.5623},
        {'id': 6, 'e_m': 10.156802, 'e_o_k': [5.827673, 4.662139, 3.729711], 'p_i': 80, 'u_i': 1.7025},
        {'id': 7, 'e_m': 0.728490, 'e_o_k': [0.417986, 0.334389, 0.267511], 'p_i': 10, 'u_i': 4.1731},
    ]
    B_BUDGET = 176.639997
    return processors, tasks, B_BUDGET
