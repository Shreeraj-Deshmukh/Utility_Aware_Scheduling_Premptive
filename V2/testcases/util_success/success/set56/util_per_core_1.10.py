"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119994, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119994, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.380156, 'e_o_k': [0.415593, 0.332474, 0.265980], 'p_i': 10, 'u_i': 3.5619},
        {'id': 1, 'e_m': 8.246762, 'e_o_k': [0.735968, 0.588774, 0.471019, 0.376815, 0.301452], 'p_i': 20, 'u_i': 1.8406},
        {'id': 2, 'e_m': 2.373806, 'e_o_k': [0.241240, 0.192992, 0.154394, 0.123515], 'p_i': 40, 'u_i': 2.4312},
        {'id': 3, 'e_m': 14.272768, 'e_o_k': [2.378795, 1.903036], 'p_i': 80, 'u_i': 4.6220},
        {'id': 4, 'e_m': 14.671758, 'e_o_k': [1.309355, 1.047484, 0.837987, 0.670390, 0.536312], 'p_i': 40, 'u_i': 4.8031},
        {'id': 5, 'e_m': 16.773061, 'e_o_k': [1.363930, 1.091144, 0.872915, 0.698332, 0.558666, 0.446932], 'p_i': 40, 'u_i': 1.8198},
        {'id': 6, 'e_m': 3.412442, 'e_o_k': [0.568740, 0.454992], 'p_i': 80, 'u_i': 3.6343},
        {'id': 7, 'e_m': 7.662309, 'e_o_k': [0.623074, 0.498459, 0.398767, 0.319014, 0.255211, 0.204169], 'p_i': 20, 'u_i': 1.0815},
    ]
    B_BUDGET = 263.119994
    return processors, tasks, B_BUDGET
