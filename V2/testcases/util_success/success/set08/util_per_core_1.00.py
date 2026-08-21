"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199995, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199995, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.945830, 'e_o_k': [0.362192, 0.289754, 0.231803], 'p_i': 10, 'u_i': 2.4893},
        {'id': 1, 'e_m': 7.562670, 'e_o_k': [0.929836, 0.743869, 0.595095], 'p_i': 20, 'u_i': 4.7173},
        {'id': 2, 'e_m': 16.921331, 'e_o_k': [2.820222, 2.256177], 'p_i': 40, 'u_i': 2.7558},
        {'id': 3, 'e_m': 39.858183, 'e_o_k': [3.557073, 2.845658, 2.276526, 1.821221, 1.456977], 'p_i': 80, 'u_i': 2.1995},
        {'id': 4, 'e_m': 7.742473, 'e_o_k': [0.951943, 0.761555, 0.609244], 'p_i': 40, 'u_i': 2.7585},
        {'id': 5, 'e_m': 1.441120, 'e_o_k': [0.128610, 0.102888, 0.082311, 0.065848, 0.052679], 'p_i': 10, 'u_i': 4.0797},
        {'id': 6, 'e_m': 0.526278, 'e_o_k': [0.053484, 0.042787, 0.034229, 0.027384], 'p_i': 10, 'u_i': 3.6908},
        {'id': 7, 'e_m': 0.314426, 'e_o_k': [0.031954, 0.025563, 0.020450, 0.016360], 'p_i': 20, 'u_i': 3.3068},
    ]
    B_BUDGET = 239.199995
    return processors, tasks, B_BUDGET
