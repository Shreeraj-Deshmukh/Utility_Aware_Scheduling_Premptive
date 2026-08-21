"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279999, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279999, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.347421, 'e_o_k': [0.165667, 0.132533, 0.106027], 'p_i': 10, 'u_i': 3.5794},
        {'id': 1, 'e_m': 4.569482, 'e_o_k': [0.464378, 0.371503, 0.297202, 0.237762], 'p_i': 20, 'u_i': 4.0478},
        {'id': 2, 'e_m': 9.638203, 'e_o_k': [0.783747, 0.626997, 0.501598, 0.401278, 0.321023, 0.256818], 'p_i': 40, 'u_i': 1.4500},
        {'id': 3, 'e_m': 30.049972, 'e_o_k': [3.694669, 2.955735, 2.364588], 'p_i': 80, 'u_i': 4.5142},
        {'id': 4, 'e_m': 0.765371, 'e_o_k': [0.068304, 0.054643, 0.043715, 0.034972, 0.027977], 'p_i': 10, 'u_i': 2.2039},
        {'id': 5, 'e_m': 1.929669, 'e_o_k': [0.172210, 0.137768, 0.110214, 0.088171, 0.070537], 'p_i': 10, 'u_i': 3.2272},
        {'id': 6, 'e_m': 39.564762, 'e_o_k': [6.594127, 5.275302], 'p_i': 80, 'u_i': 1.1781},
        {'id': 7, 'e_m': 2.245621, 'e_o_k': [0.228214, 0.182571, 0.146057, 0.116845], 'p_i': 40, 'u_i': 4.3119},
    ]
    B_BUDGET = 215.279999
    return processors, tasks, B_BUDGET
