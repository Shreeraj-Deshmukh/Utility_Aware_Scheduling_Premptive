"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679992, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679992, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.793526, 'e_o_k': [0.064527, 0.051621, 0.041297, 0.033038, 0.026430, 0.021144], 'p_i': 10, 'u_i': 2.9192},
        {'id': 1, 'e_m': 1.049928, 'e_o_k': [0.106700, 0.085360, 0.068288, 0.054630], 'p_i': 20, 'u_i': 2.0454},
        {'id': 2, 'e_m': 7.537585, 'e_o_k': [0.612931, 0.490345, 0.392276, 0.313821, 0.251057, 0.200845], 'p_i': 40, 'u_i': 2.8602},
        {'id': 3, 'e_m': 17.122126, 'e_o_k': [2.853688, 2.282950], 'p_i': 80, 'u_i': 2.9521},
        {'id': 4, 'e_m': 0.854071, 'e_o_k': [0.142345, 0.113876], 'p_i': 10, 'u_i': 3.5497},
        {'id': 5, 'e_m': 3.312634, 'e_o_k': [0.336650, 0.269320, 0.215456, 0.172365], 'p_i': 40, 'u_i': 2.7971},
        {'id': 6, 'e_m': 1.838787, 'e_o_k': [0.149524, 0.119619, 0.095695, 0.076556, 0.061245, 0.048996], 'p_i': 80, 'u_i': 4.6429},
        {'id': 7, 'e_m': 5.958164, 'e_o_k': [0.993027, 0.794422], 'p_i': 80, 'u_i': 1.6248},
    ]
    B_BUDGET = 95.679992
    return processors, tasks, B_BUDGET
