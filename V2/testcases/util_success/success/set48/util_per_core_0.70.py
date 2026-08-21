"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.44, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.44, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.401020, 'e_o_k': [0.400170, 0.320136], 'p_i': 10, 'u_i': 2.6470},
        {'id': 1, 'e_m': 6.104581, 'e_o_k': [0.750563, 0.600451, 0.480360], 'p_i': 20, 'u_i': 4.9479},
        {'id': 2, 'e_m': 0.167938, 'e_o_k': [0.020648, 0.016518, 0.013215], 'p_i': 40, 'u_i': 2.1346},
        {'id': 3, 'e_m': 6.754175, 'e_o_k': [1.125696, 0.900557], 'p_i': 80, 'u_i': 1.3827},
        {'id': 4, 'e_m': 20.366020, 'e_o_k': [3.394337, 2.715469], 'p_i': 80, 'u_i': 3.9576},
        {'id': 5, 'e_m': 3.824194, 'e_o_k': [0.341283, 0.273027, 0.218421, 0.174737, 0.139790], 'p_i': 20, 'u_i': 4.9670},
        {'id': 6, 'e_m': 2.947267, 'e_o_k': [0.263024, 0.210419, 0.168335, 0.134668, 0.107734], 'p_i': 10, 'u_i': 4.5958},
        {'id': 7, 'e_m': 2.042535, 'e_o_k': [0.182282, 0.145826, 0.116661, 0.093329, 0.074663], 'p_i': 80, 'u_i': 1.9552},
    ]
    B_BUDGET = 167.440000
    return processors, tasks, B_BUDGET
