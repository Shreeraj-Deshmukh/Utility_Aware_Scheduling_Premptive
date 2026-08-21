"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519999, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519999, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.652987, 'e_o_k': [0.108831, 0.087065], 'p_i': 10, 'u_i': 1.4412},
        {'id': 1, 'e_m': 5.538625, 'e_o_k': [0.562868, 0.450295, 0.360236, 0.288189], 'p_i': 20, 'u_i': 3.7136},
        {'id': 2, 'e_m': 2.492693, 'e_o_k': [0.202697, 0.162158, 0.129726, 0.103781, 0.083025, 0.066420], 'p_i': 40, 'u_i': 3.0715},
        {'id': 3, 'e_m': 32.820067, 'e_o_k': [2.668819, 2.135055, 1.708044, 1.366435, 1.093148, 0.874519], 'p_i': 80, 'u_i': 2.1053},
        {'id': 4, 'e_m': 0.263680, 'e_o_k': [0.043947, 0.035157], 'p_i': 20, 'u_i': 3.9261},
        {'id': 5, 'e_m': 0.798000, 'e_o_k': [0.133000, 0.106400], 'p_i': 20, 'u_i': 2.2961},
        {'id': 6, 'e_m': 0.257177, 'e_o_k': [0.022951, 0.018361, 0.014689, 0.011751, 0.009401], 'p_i': 10, 'u_i': 1.3761},
        {'id': 7, 'e_m': 6.128004, 'e_o_k': [0.753443, 0.602754, 0.482204], 'p_i': 20, 'u_i': 2.1930},
    ]
    B_BUDGET = 143.519999
    return processors, tasks, B_BUDGET
