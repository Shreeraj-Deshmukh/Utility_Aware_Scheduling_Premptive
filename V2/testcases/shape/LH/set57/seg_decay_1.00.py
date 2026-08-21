"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.31998, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.31998, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.100744, 'e_o_k': [0.028208, 0.028208, 0.028208, 0.028208, 0.028208], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 0.720915, 'e_o_k': [0.168213, 0.168213, 0.168213, 0.168213, 0.168213, 0.168213], 'p_i': 20, 'u_i': 3.3967},
        {'id': 2, 'e_m': 4.330945, 'e_o_k': [3.031662, 3.031662], 'p_i': 40, 'u_i': 1.9449},
        {'id': 3, 'e_m': 4.451086, 'e_o_k': [3.115760, 3.115760], 'p_i': 80, 'u_i': 4.6056},
        {'id': 4, 'e_m': 2.996813, 'e_o_k': [2.097769, 2.097769], 'p_i': 40, 'u_i': 2.0280},
        {'id': 5, 'e_m': 2.171206, 'e_o_k': [0.506615, 0.506615, 0.506615, 0.506615, 0.506615, 0.506615], 'p_i': 80, 'u_i': 1.2717},
        {'id': 6, 'e_m': 0.650677, 'e_o_k': [0.455474, 0.455474], 'p_i': 10, 'u_i': 1.1584},
        {'id': 7, 'e_m': 1.827166, 'e_o_k': [0.852677, 0.852677, 0.852677], 'p_i': 80, 'u_i': 3.8897},
    ]
    B_BUDGET = 88.319980
    return processors, tasks, B_BUDGET
