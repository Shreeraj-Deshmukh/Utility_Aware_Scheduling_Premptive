"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359999, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359999, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.359494, 'e_o_k': [0.299812, 0.239850, 0.191880, 0.153504, 0.122803], 'p_i': 10, 'u_i': 3.8323},
        {'id': 1, 'e_m': 3.759107, 'e_o_k': [0.626518, 0.501214], 'p_i': 20, 'u_i': 2.6619},
        {'id': 2, 'e_m': 2.498700, 'e_o_k': [0.307217, 0.245774, 0.196619], 'p_i': 40, 'u_i': 4.8838},
        {'id': 3, 'e_m': 27.247296, 'e_o_k': [2.215660, 1.772528, 1.418022, 1.134418, 0.907534, 0.726027], 'p_i': 80, 'u_i': 1.1242},
        {'id': 4, 'e_m': 29.857182, 'e_o_k': [2.664551, 2.131641, 1.705313, 1.364250, 1.091400], 'p_i': 80, 'u_i': 3.3705},
        {'id': 5, 'e_m': 2.773331, 'e_o_k': [0.281843, 0.225474, 0.180379, 0.144303], 'p_i': 40, 'u_i': 2.3409},
        {'id': 6, 'e_m': 5.394262, 'e_o_k': [0.899044, 0.719235], 'p_i': 80, 'u_i': 3.0130},
        {'id': 7, 'e_m': 1.630602, 'e_o_k': [0.145520, 0.116416, 0.093133, 0.074506, 0.059605], 'p_i': 10, 'u_i': 4.5858},
    ]
    B_BUDGET = 191.359999
    return processors, tasks, B_BUDGET
