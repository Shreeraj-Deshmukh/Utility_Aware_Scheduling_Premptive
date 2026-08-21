"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.76001, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.76001, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.898756, 'e_o_k': [0.110503, 0.088402, 0.070722], 'p_i': 10, 'u_i': 3.9348},
        {'id': 1, 'e_m': 6.278489, 'e_o_k': [1.046415, 0.837132], 'p_i': 20, 'u_i': 2.2078},
        {'id': 2, 'e_m': 0.220875, 'e_o_k': [0.022447, 0.017957, 0.014366, 0.011493], 'p_i': 40, 'u_i': 1.5646},
        {'id': 3, 'e_m': 1.611672, 'e_o_k': [0.268612, 0.214890], 'p_i': 80, 'u_i': 4.4075},
        {'id': 4, 'e_m': 0.313909, 'e_o_k': [0.052318, 0.041855], 'p_i': 10, 'u_i': 2.2030},
        {'id': 5, 'e_m': 0.212949, 'e_o_k': [0.026182, 0.020946, 0.016757], 'p_i': 80, 'u_i': 2.4770},
        {'id': 6, 'e_m': 0.470545, 'e_o_k': [0.038263, 0.030611, 0.024488, 0.019591, 0.015673, 0.012538], 'p_i': 80, 'u_i': 1.9604},
        {'id': 7, 'e_m': 2.611953, 'e_o_k': [0.265442, 0.212354, 0.169883, 0.135906], 'p_i': 20, 'u_i': 2.4961},
    ]
    B_BUDGET = 71.760010
    return processors, tasks, B_BUDGET
