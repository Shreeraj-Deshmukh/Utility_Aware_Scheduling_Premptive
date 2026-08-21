"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119985, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119985, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.349510, 'e_o_k': [0.288874, 0.231099, 0.184879], 'p_i': 10, 'u_i': 4.1073},
        {'id': 1, 'e_m': 7.146415, 'e_o_k': [0.726262, 0.581009, 0.464808, 0.371846], 'p_i': 20, 'u_i': 3.7559},
        {'id': 2, 'e_m': 14.894685, 'e_o_k': [1.513687, 1.210950, 0.968760, 0.775008], 'p_i': 40, 'u_i': 4.2943},
        {'id': 3, 'e_m': 19.563398, 'e_o_k': [3.260566, 2.608453], 'p_i': 80, 'u_i': 1.0411},
        {'id': 4, 'e_m': 1.430565, 'e_o_k': [0.175889, 0.140711, 0.112569], 'p_i': 40, 'u_i': 4.5861},
        {'id': 5, 'e_m': 15.959685, 'e_o_k': [1.424294, 1.139435, 0.911548, 0.729238, 0.583391], 'p_i': 40, 'u_i': 4.2047},
        {'id': 6, 'e_m': 6.184281, 'e_o_k': [0.760362, 0.608290, 0.486632], 'p_i': 20, 'u_i': 1.7569},
        {'id': 7, 'e_m': 4.936966, 'e_o_k': [0.501724, 0.401379, 0.321104, 0.256883], 'p_i': 20, 'u_i': 1.4071},
    ]
    B_BUDGET = 263.119985
    return processors, tasks, B_BUDGET
