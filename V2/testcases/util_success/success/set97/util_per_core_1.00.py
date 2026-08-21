"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200015, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200015, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.623240, 'e_o_k': [0.131997, 0.105597, 0.084478, 0.067582, 0.054066, 0.043253], 'p_i': 10, 'u_i': 4.0993},
        {'id': 1, 'e_m': 1.598277, 'e_o_k': [0.266379, 0.213104], 'p_i': 20, 'u_i': 2.5958},
        {'id': 2, 'e_m': 19.137125, 'e_o_k': [2.352925, 1.882340, 1.505872], 'p_i': 40, 'u_i': 1.3643},
        {'id': 3, 'e_m': 17.198898, 'e_o_k': [1.398557, 1.118846, 0.895077, 0.716061, 0.572849, 0.458279], 'p_i': 80, 'u_i': 1.6218},
        {'id': 4, 'e_m': 7.743920, 'e_o_k': [0.786984, 0.629587, 0.503670, 0.402936], 'p_i': 20, 'u_i': 1.2955},
        {'id': 5, 'e_m': 2.050792, 'e_o_k': [0.208414, 0.166731, 0.133385, 0.106708], 'p_i': 10, 'u_i': 2.7520},
        {'id': 6, 'e_m': 15.149704, 'e_o_k': [1.352008, 1.081607, 0.865285, 0.692228, 0.553783], 'p_i': 40, 'u_i': 2.0302},
        {'id': 7, 'e_m': 0.933300, 'e_o_k': [0.114750, 0.091800, 0.073440], 'p_i': 10, 'u_i': 2.5969},
    ]
    B_BUDGET = 239.200015
    return processors, tasks, B_BUDGET
