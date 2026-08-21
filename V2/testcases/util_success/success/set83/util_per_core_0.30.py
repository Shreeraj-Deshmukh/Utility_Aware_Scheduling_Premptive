"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760003, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760003, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.180276, 'e_o_k': [0.105332, 0.084265, 0.067412, 0.053930, 0.043144], 'p_i': 10, 'u_i': 3.6650},
        {'id': 1, 'e_m': 1.116528, 'e_o_k': [0.090792, 0.072634, 0.058107, 0.046486, 0.037189, 0.029751], 'p_i': 20, 'u_i': 1.3163},
        {'id': 2, 'e_m': 0.852067, 'e_o_k': [0.086592, 0.069274, 0.055419, 0.044335], 'p_i': 40, 'u_i': 1.2768},
        {'id': 3, 'e_m': 10.314855, 'e_o_k': [1.268220, 1.014576, 0.811661], 'p_i': 80, 'u_i': 1.7506},
        {'id': 4, 'e_m': 4.486784, 'e_o_k': [0.551654, 0.441323, 0.353058], 'p_i': 40, 'u_i': 4.5685},
        {'id': 5, 'e_m': 0.505509, 'e_o_k': [0.045113, 0.036091, 0.028872, 0.023098, 0.018478], 'p_i': 10, 'u_i': 2.7344},
        {'id': 6, 'e_m': 0.665875, 'e_o_k': [0.110979, 0.088783], 'p_i': 40, 'u_i': 1.1398},
        {'id': 7, 'e_m': 7.723305, 'e_o_k': [0.689253, 0.551402, 0.441122, 0.352897, 0.282318], 'p_i': 80, 'u_i': 4.8954},
    ]
    B_BUDGET = 71.760003
    return processors, tasks, B_BUDGET
