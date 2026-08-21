"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.63998, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.63998, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.456621, 'e_o_k': [0.835766, 0.668613, 0.534890], 'p_i': 10, 'u_i': 4.9967},
        {'id': 1, 'e_m': 6.472983, 'e_o_k': [3.714006, 2.971205, 2.376964], 'p_i': 20, 'u_i': 3.1686},
        {'id': 2, 'e_m': 1.070031, 'e_o_k': [0.613952, 0.491162, 0.392929], 'p_i': 40, 'u_i': 1.4833},
        {'id': 3, 'e_m': 9.500976, 'e_o_k': [5.451380, 4.361104, 3.488883], 'p_i': 80, 'u_i': 4.1202},
        {'id': 4, 'e_m': 0.365435, 'e_o_k': [0.209676, 0.167741, 0.134193], 'p_i': 40, 'u_i': 4.7898},
        {'id': 5, 'e_m': 0.184044, 'e_o_k': [0.105599, 0.084479, 0.067583], 'p_i': 10, 'u_i': 3.8151},
        {'id': 6, 'e_m': 5.282667, 'e_o_k': [3.031038, 2.424831, 1.939865], 'p_i': 40, 'u_i': 2.4922},
        {'id': 7, 'e_m': 0.255688, 'e_o_k': [0.146706, 0.117365, 0.093892], 'p_i': 10, 'u_i': 1.4417},
    ]
    B_BUDGET = 176.639980
    return processors, tasks, B_BUDGET
