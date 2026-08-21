"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760002, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760002, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.714830, 'e_o_k': [0.174271, 0.139417, 0.111534, 0.089227], 'p_i': 10, 'u_i': 1.7025},
        {'id': 1, 'e_m': 1.082430, 'e_o_k': [0.096600, 0.077280, 0.061824, 0.049459, 0.039567], 'p_i': 20, 'u_i': 2.0058},
        {'id': 2, 'e_m': 0.841823, 'e_o_k': [0.140304, 0.112243], 'p_i': 40, 'u_i': 3.5722},
        {'id': 3, 'e_m': 14.860707, 'e_o_k': [1.510234, 1.208188, 0.966550, 0.773240], 'p_i': 80, 'u_i': 1.2384},
        {'id': 4, 'e_m': 1.387350, 'e_o_k': [0.231225, 0.184980], 'p_i': 40, 'u_i': 4.5379},
        {'id': 5, 'e_m': 1.967073, 'e_o_k': [0.327845, 0.262276], 'p_i': 20, 'u_i': 1.9982},
        {'id': 6, 'e_m': 0.229139, 'e_o_k': [0.038190, 0.030552], 'p_i': 20, 'u_i': 2.1252},
        {'id': 7, 'e_m': 1.847739, 'e_o_k': [0.187778, 0.150223, 0.120178, 0.096143], 'p_i': 80, 'u_i': 4.2384},
    ]
    B_BUDGET = 71.760002
    return processors, tasks, B_BUDGET
