"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120003, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120003, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.030264, 'e_o_k': [0.181187, 0.144950, 0.115960, 0.092768, 0.074214], 'p_i': 10, 'u_i': 1.3844},
        {'id': 1, 'e_m': 7.999647, 'e_o_k': [0.713914, 0.571131, 0.456905, 0.365524, 0.292419], 'p_i': 20, 'u_i': 3.8571},
        {'id': 2, 'e_m': 10.434278, 'e_o_k': [1.739046, 1.391237], 'p_i': 40, 'u_i': 3.6185},
        {'id': 3, 'e_m': 1.411188, 'e_o_k': [0.143413, 0.114731, 0.091785, 0.073428], 'p_i': 80, 'u_i': 1.1495},
        {'id': 4, 'e_m': 5.720227, 'e_o_k': [0.581324, 0.465059, 0.372047, 0.297638], 'p_i': 20, 'u_i': 2.9121},
        {'id': 5, 'e_m': 2.936794, 'e_o_k': [0.262089, 0.209671, 0.167737, 0.134190, 0.107352], 'p_i': 10, 'u_i': 1.1301},
        {'id': 6, 'e_m': 6.720123, 'e_o_k': [1.120020, 0.896016], 'p_i': 20, 'u_i': 4.2884},
        {'id': 7, 'e_m': 4.027976, 'e_o_k': [0.359470, 0.287576, 0.230060, 0.184048, 0.147239], 'p_i': 10, 'u_i': 4.6426},
    ]
    B_BUDGET = 263.120003
    return processors, tasks, B_BUDGET
