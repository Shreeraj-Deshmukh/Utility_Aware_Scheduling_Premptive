"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.343272, 'e_o_k': [0.196959, 0.157568, 0.126054], 'p_i': 10, 'u_i': 3.5588},
        {'id': 1, 'e_m': 0.791370, 'e_o_k': [0.454064, 0.363252, 0.290601], 'p_i': 20, 'u_i': 1.0875},
        {'id': 2, 'e_m': 2.553569, 'e_o_k': [1.465162, 1.172130, 0.937704], 'p_i': 40, 'u_i': 2.9446},
        {'id': 3, 'e_m': 0.112895, 'e_o_k': [0.064776, 0.051820, 0.041456], 'p_i': 80, 'u_i': 2.5289},
        {'id': 4, 'e_m': 5.014202, 'e_o_k': [2.877001, 2.301601, 1.841281], 'p_i': 40, 'u_i': 2.8941},
        {'id': 5, 'e_m': 2.695419, 'e_o_k': [1.546552, 1.237241, 0.989793], 'p_i': 40, 'u_i': 3.9189},
        {'id': 6, 'e_m': 0.133194, 'e_o_k': [0.076423, 0.061138, 0.048910], 'p_i': 10, 'u_i': 2.1344},
        {'id': 7, 'e_m': 2.191761, 'e_o_k': [1.257568, 1.006054, 0.804844], 'p_i': 40, 'u_i': 2.5225},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET
