"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.40001, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.40001, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.201488, 'e_o_k': [0.055969, 0.044775], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 1.441830, 'e_o_k': [0.400508, 0.320407], 'p_i': 20, 'u_i': 1.1969},
        {'id': 2, 'e_m': 8.661890, 'e_o_k': [2.406081, 1.924865], 'p_i': 40, 'u_i': 4.6056},
        {'id': 3, 'e_m': 8.902172, 'e_o_k': [2.472826, 1.978261], 'p_i': 80, 'u_i': 2.0280},
        {'id': 4, 'e_m': 5.993625, 'e_o_k': [1.664896, 1.331917], 'p_i': 40, 'u_i': 3.8591},
        {'id': 5, 'e_m': 4.342413, 'e_o_k': [1.206226, 0.964981], 'p_i': 80, 'u_i': 4.1547},
        {'id': 6, 'e_m': 1.301354, 'e_o_k': [0.361487, 0.289190], 'p_i': 10, 'u_i': 4.9057},
        {'id': 7, 'e_m': 3.654332, 'e_o_k': [1.015092, 0.812074], 'p_i': 80, 'u_i': 4.2009},
    ]
    B_BUDGET = 110.400010
    return processors, tasks, B_BUDGET
