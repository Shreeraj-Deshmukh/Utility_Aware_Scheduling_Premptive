"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760023, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760023, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.842775, 'e_o_k': [0.140463, 0.112370], 'p_i': 10, 'u_i': 2.2300},
        {'id': 1, 'e_m': 2.248817, 'e_o_k': [0.228538, 0.182831, 0.146265, 0.117012], 'p_i': 20, 'u_i': 1.1980},
        {'id': 2, 'e_m': 9.427790, 'e_o_k': [0.958109, 0.766487, 0.613190, 0.490552], 'p_i': 40, 'u_i': 3.9540},
        {'id': 3, 'e_m': 0.238119, 'e_o_k': [0.039686, 0.031749], 'p_i': 80, 'u_i': 1.1604},
        {'id': 4, 'e_m': 2.068973, 'e_o_k': [0.210261, 0.168209, 0.134567, 0.107654], 'p_i': 40, 'u_i': 4.9556},
        {'id': 5, 'e_m': 2.198182, 'e_o_k': [0.366364, 0.293091], 'p_i': 20, 'u_i': 1.3741},
        {'id': 6, 'e_m': 0.023527, 'e_o_k': [0.002100, 0.001680, 0.001344, 0.001075, 0.000860], 'p_i': 10, 'u_i': 4.6107},
        {'id': 7, 'e_m': 0.049946, 'e_o_k': [0.004457, 0.003566, 0.002853, 0.002282, 0.001826], 'p_i': 80, 'u_i': 2.5105},
    ]
    B_BUDGET = 71.760023
    return processors, tasks, B_BUDGET
