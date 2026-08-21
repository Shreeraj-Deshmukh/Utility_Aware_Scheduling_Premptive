"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32002, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.32002, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.822029, 'e_o_k': [0.471656, 0.377325, 0.301860], 'p_i': 10, 'u_i': 2.9699},
        {'id': 1, 'e_m': 0.158606, 'e_o_k': [0.091004, 0.072803, 0.058242], 'p_i': 20, 'u_i': 1.6736},
        {'id': 2, 'e_m': 0.584707, 'e_o_k': [0.335488, 0.268390, 0.214712], 'p_i': 40, 'u_i': 2.6796},
        {'id': 3, 'e_m': 6.151953, 'e_o_k': [3.529809, 2.823847, 2.259078], 'p_i': 80, 'u_i': 2.5270},
        {'id': 4, 'e_m': 1.208847, 'e_o_k': [0.693601, 0.554881, 0.443905], 'p_i': 20, 'u_i': 1.9244},
        {'id': 5, 'e_m': 0.880892, 'e_o_k': [0.505430, 0.404344, 0.323475], 'p_i': 10, 'u_i': 4.2011},
        {'id': 6, 'e_m': 0.518381, 'e_o_k': [0.297432, 0.237945, 0.190356], 'p_i': 40, 'u_i': 3.3831},
        {'id': 7, 'e_m': 1.137173, 'e_o_k': [0.652477, 0.521981, 0.417585], 'p_i': 20, 'u_i': 4.9669},
    ]
    B_BUDGET = 88.320020
    return processors, tasks, B_BUDGET
