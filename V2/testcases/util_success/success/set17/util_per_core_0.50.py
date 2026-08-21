"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599994, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599994, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.991907, 'e_o_k': [0.080659, 0.064527, 0.051621, 0.041297, 0.033038, 0.026430], 'p_i': 10, 'u_i': 2.9192},
        {'id': 1, 'e_m': 1.312411, 'e_o_k': [0.133375, 0.106700, 0.085360, 0.068288], 'p_i': 20, 'u_i': 2.0454},
        {'id': 2, 'e_m': 9.421981, 'e_o_k': [0.766164, 0.612931, 0.490345, 0.392276, 0.313821, 0.251057], 'p_i': 40, 'u_i': 2.8602},
        {'id': 3, 'e_m': 21.402657, 'e_o_k': [3.567109, 2.853688], 'p_i': 80, 'u_i': 2.9521},
        {'id': 4, 'e_m': 1.067589, 'e_o_k': [0.177931, 0.142345], 'p_i': 10, 'u_i': 3.5497},
        {'id': 5, 'e_m': 4.140792, 'e_o_k': [0.420812, 0.336650, 0.269320, 0.215456], 'p_i': 40, 'u_i': 2.7971},
        {'id': 6, 'e_m': 2.298483, 'e_o_k': [0.186905, 0.149524, 0.119619, 0.095695, 0.076556, 0.061245], 'p_i': 80, 'u_i': 4.6429},
        {'id': 7, 'e_m': 7.447705, 'e_o_k': [1.241284, 0.993027], 'p_i': 80, 'u_i': 1.6248},
    ]
    B_BUDGET = 119.599994
    return processors, tasks, B_BUDGET
