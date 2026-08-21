"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120006, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120006, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.675903, 'e_o_k': [0.054962, 0.043970, 0.035176, 0.028141, 0.022513, 0.018010], 'p_i': 10, 'u_i': 4.4319},
        {'id': 1, 'e_m': 7.032415, 'e_o_k': [0.627595, 0.502076, 0.401661, 0.321329, 0.257063], 'p_i': 20, 'u_i': 3.5005},
        {'id': 2, 'e_m': 4.077416, 'e_o_k': [0.414372, 0.331497, 0.265198, 0.212158], 'p_i': 40, 'u_i': 3.6064},
        {'id': 3, 'e_m': 36.512173, 'e_o_k': [3.258464, 2.606771, 2.085417, 1.668333, 1.334667], 'p_i': 80, 'u_i': 2.1318},
        {'id': 4, 'e_m': 14.852649, 'e_o_k': [1.207768, 0.966215, 0.772972, 0.618377, 0.494702, 0.395761], 'p_i': 40, 'u_i': 2.3435},
        {'id': 5, 'e_m': 0.211981, 'e_o_k': [0.018918, 0.015134, 0.012107, 0.009686, 0.007749], 'p_i': 10, 'u_i': 4.1320},
        {'id': 6, 'e_m': 33.603414, 'e_o_k': [5.600569, 4.480455], 'p_i': 80, 'u_i': 4.9104},
        {'id': 7, 'e_m': 4.098944, 'e_o_k': [0.683157, 0.546526], 'p_i': 10, 'u_i': 1.8351},
    ]
    B_BUDGET = 263.120006
    return processors, tasks, B_BUDGET
