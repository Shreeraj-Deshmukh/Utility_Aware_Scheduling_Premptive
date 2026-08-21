"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279989, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279989, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.960636, 'e_o_k': [0.174973, 0.139979, 0.111983, 0.089586, 0.071669], 'p_i': 10, 'u_i': 1.4156},
        {'id': 1, 'e_m': 5.406068, 'e_o_k': [0.901011, 0.720809], 'p_i': 20, 'u_i': 4.7114},
        {'id': 2, 'e_m': 14.293909, 'e_o_k': [1.275634, 1.020508, 0.816406, 0.653125, 0.522500], 'p_i': 40, 'u_i': 3.0006},
        {'id': 3, 'e_m': 20.467164, 'e_o_k': [2.516455, 2.013164, 1.610531], 'p_i': 80, 'u_i': 1.2816},
        {'id': 4, 'e_m': 2.630853, 'e_o_k': [0.267363, 0.213890, 0.171112, 0.136890], 'p_i': 40, 'u_i': 2.2759},
        {'id': 5, 'e_m': 7.829713, 'e_o_k': [0.636686, 0.509349, 0.407479, 0.325983, 0.260787, 0.208629], 'p_i': 20, 'u_i': 1.7983},
        {'id': 6, 'e_m': 0.119345, 'e_o_k': [0.019891, 0.015913], 'p_i': 10, 'u_i': 2.1310},
        {'id': 7, 'e_m': 5.025084, 'e_o_k': [0.408623, 0.326899, 0.261519, 0.209215, 0.167372, 0.133898], 'p_i': 20, 'u_i': 2.4443},
    ]
    B_BUDGET = 215.279989
    return processors, tasks, B_BUDGET
