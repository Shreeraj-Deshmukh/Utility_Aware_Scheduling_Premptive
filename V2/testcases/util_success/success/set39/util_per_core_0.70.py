"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440023, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440023, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.761819, 'e_o_k': [0.126970, 0.101576], 'p_i': 10, 'u_i': 1.4412},
        {'id': 1, 'e_m': 6.461729, 'e_o_k': [0.656680, 0.525344, 0.420275, 0.336220], 'p_i': 20, 'u_i': 3.7136},
        {'id': 2, 'e_m': 2.908142, 'e_o_k': [0.236480, 0.189184, 0.151347, 0.121078, 0.096862, 0.077490], 'p_i': 40, 'u_i': 3.0715},
        {'id': 3, 'e_m': 38.290078, 'e_o_k': [3.113622, 2.490898, 1.992718, 1.594174, 1.275340, 1.020272], 'p_i': 80, 'u_i': 2.1053},
        {'id': 4, 'e_m': 0.307627, 'e_o_k': [0.051271, 0.041017], 'p_i': 20, 'u_i': 3.9261},
        {'id': 5, 'e_m': 0.931000, 'e_o_k': [0.155167, 0.124133], 'p_i': 20, 'u_i': 2.2961},
        {'id': 6, 'e_m': 0.300040, 'e_o_k': [0.026777, 0.021421, 0.017137, 0.013710, 0.010968], 'p_i': 10, 'u_i': 1.3761},
        {'id': 7, 'e_m': 7.149337, 'e_o_k': [0.879017, 0.703214, 0.562571], 'p_i': 20, 'u_i': 2.1930},
    ]
    B_BUDGET = 167.440023
    return processors, tasks, B_BUDGET
