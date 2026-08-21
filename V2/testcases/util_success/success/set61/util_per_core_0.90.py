"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279993, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279993, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.411704, 'e_o_k': [0.215228, 0.172183, 0.137746, 0.110197, 0.088157], 'p_i': 10, 'u_i': 2.7853},
        {'id': 1, 'e_m': 0.440196, 'e_o_k': [0.073366, 0.058693], 'p_i': 20, 'u_i': 2.0311},
        {'id': 2, 'e_m': 8.034947, 'e_o_k': [0.987903, 0.790323, 0.632258], 'p_i': 40, 'u_i': 4.7803},
        {'id': 3, 'e_m': 15.374255, 'e_o_k': [2.562376, 2.049901], 'p_i': 80, 'u_i': 3.5491},
        {'id': 4, 'e_m': 1.476307, 'e_o_k': [0.150031, 0.120025, 0.096020, 0.076816], 'p_i': 40, 'u_i': 1.2323},
        {'id': 5, 'e_m': 4.873305, 'e_o_k': [0.434909, 0.347927, 0.278342, 0.222674, 0.178139], 'p_i': 10, 'u_i': 1.1183},
        {'id': 6, 'e_m': 3.346174, 'e_o_k': [0.340058, 0.272047, 0.217637, 0.174110], 'p_i': 10, 'u_i': 3.6917},
        {'id': 7, 'e_m': 22.792989, 'e_o_k': [1.853450, 1.482760, 1.186208, 0.948967, 0.759173, 0.607339], 'p_i': 80, 'u_i': 4.1944},
    ]
    B_BUDGET = 215.279993
    return processors, tasks, B_BUDGET
