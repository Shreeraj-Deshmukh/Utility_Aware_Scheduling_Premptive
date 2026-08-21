"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200002, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200002, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.199367, 'e_o_k': [0.374765, 0.299812, 0.239850, 0.191880, 0.153504], 'p_i': 10, 'u_i': 3.8323},
        {'id': 1, 'e_m': 4.698884, 'e_o_k': [0.783147, 0.626518], 'p_i': 20, 'u_i': 2.6619},
        {'id': 2, 'e_m': 3.123375, 'e_o_k': [0.384022, 0.307217, 0.245774], 'p_i': 40, 'u_i': 4.8838},
        {'id': 3, 'e_m': 34.059121, 'e_o_k': [2.769575, 2.215660, 1.772528, 1.418022, 1.134418, 0.907534], 'p_i': 80, 'u_i': 1.1242},
        {'id': 4, 'e_m': 37.321478, 'e_o_k': [3.330689, 2.664551, 2.131641, 1.705313, 1.364250], 'p_i': 80, 'u_i': 3.3705},
        {'id': 5, 'e_m': 3.466664, 'e_o_k': [0.352303, 0.281843, 0.225474, 0.180379], 'p_i': 40, 'u_i': 2.3409},
        {'id': 6, 'e_m': 6.742827, 'e_o_k': [1.123805, 0.899044], 'p_i': 80, 'u_i': 3.0130},
        {'id': 7, 'e_m': 2.038253, 'e_o_k': [0.181900, 0.145520, 0.116416, 0.093133, 0.074506], 'p_i': 10, 'u_i': 4.5858},
    ]
    B_BUDGET = 239.200002
    return processors, tasks, B_BUDGET
