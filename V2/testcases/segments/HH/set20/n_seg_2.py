"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64001, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.64001, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.143336, 'e_o_k': [1.667039, 1.333631], 'p_i': 10, 'u_i': 1.5090},
        {'id': 1, 'e_m': 1.413954, 'e_o_k': [1.099742, 0.879794], 'p_i': 20, 'u_i': 1.7367},
        {'id': 2, 'e_m': 3.402871, 'e_o_k': [2.646677, 2.117342], 'p_i': 40, 'u_i': 1.3712},
        {'id': 3, 'e_m': 12.001313, 'e_o_k': [9.334355, 7.467484], 'p_i': 80, 'u_i': 4.1249},
        {'id': 4, 'e_m': 0.888149, 'e_o_k': [0.690783, 0.552626], 'p_i': 40, 'u_i': 3.5067},
        {'id': 5, 'e_m': 2.314711, 'e_o_k': [1.800331, 1.440264], 'p_i': 40, 'u_i': 2.5623},
        {'id': 6, 'e_m': 10.156802, 'e_o_k': [7.899735, 6.319788], 'p_i': 80, 'u_i': 1.7025},
        {'id': 7, 'e_m': 0.728490, 'e_o_k': [0.566604, 0.453283], 'p_i': 10, 'u_i': 4.1731},
    ]
    B_BUDGET = 176.640010
    return processors, tasks, B_BUDGET
