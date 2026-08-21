"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120006, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120006, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.907217, 'e_o_k': [0.259449, 0.207560, 0.166048, 0.132838, 0.106270], 'p_i': 10, 'u_i': 1.8232},
        {'id': 1, 'e_m': 4.615330, 'e_o_k': [0.411887, 0.329509, 0.263608, 0.210886, 0.168709], 'p_i': 20, 'u_i': 4.2323},
        {'id': 2, 'e_m': 14.678401, 'e_o_k': [1.309948, 1.047958, 0.838367, 0.670693, 0.536555], 'p_i': 40, 'u_i': 3.7021},
        {'id': 3, 'e_m': 12.281144, 'e_o_k': [1.509977, 1.207981, 0.966385], 'p_i': 80, 'u_i': 1.4717},
        {'id': 4, 'e_m': 3.281786, 'e_o_k': [0.403498, 0.322799, 0.258239], 'p_i': 10, 'u_i': 2.9634},
        {'id': 5, 'e_m': 13.748524, 'e_o_k': [1.226963, 0.981570, 0.785256, 0.628205, 0.502564], 'p_i': 80, 'u_i': 1.6416},
        {'id': 6, 'e_m': 5.520586, 'e_o_k': [0.492675, 0.394140, 0.315312, 0.252250, 0.201800], 'p_i': 20, 'u_i': 4.1520},
        {'id': 7, 'e_m': 3.819730, 'e_o_k': [0.388184, 0.310547, 0.248438, 0.198750], 'p_i': 10, 'u_i': 2.8128},
    ]
    B_BUDGET = 263.120006
    return processors, tasks, B_BUDGET
