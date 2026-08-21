"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639998, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639998, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.087664, 'e_o_k': [0.624069, 0.499256, 0.399404], 'p_i': 10, 'u_i': 2.8418},
        {'id': 1, 'e_m': 0.391931, 'e_o_k': [0.224879, 0.179903, 0.143922], 'p_i': 20, 'u_i': 1.5566},
        {'id': 2, 'e_m': 13.096144, 'e_o_k': [7.514181, 6.011345, 4.809076], 'p_i': 40, 'u_i': 3.2695},
        {'id': 3, 'e_m': 7.655110, 'e_o_k': [4.392276, 3.513821, 2.811057], 'p_i': 80, 'u_i': 3.8342},
        {'id': 4, 'e_m': 0.303823, 'e_o_k': [0.174325, 0.139460, 0.111568], 'p_i': 20, 'u_i': 4.2274},
        {'id': 5, 'e_m': 0.754717, 'e_o_k': [0.433034, 0.346427, 0.277142], 'p_i': 20, 'u_i': 3.9205},
        {'id': 6, 'e_m': 5.033151, 'e_o_k': [2.887874, 2.310299, 1.848239], 'p_i': 40, 'u_i': 1.6340},
        {'id': 7, 'e_m': 2.791552, 'e_o_k': [1.601710, 1.281368, 1.025094], 'p_i': 40, 'u_i': 3.9145},
    ]
    B_BUDGET = 176.639998
    return processors, tasks, B_BUDGET
