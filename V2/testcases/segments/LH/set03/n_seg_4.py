"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "segments", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "segments", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.379864, 'e_o_k': [0.180152, 0.144122, 0.115297, 0.092238], 'p_i': 10, 'u_i': 3.3255},
        {'id': 1, 'e_m': 1.133617, 'e_o_k': [0.537623, 0.430099, 0.344079, 0.275263], 'p_i': 20, 'u_i': 3.5739},
        {'id': 2, 'e_m': 0.770090, 'e_o_k': [0.365219, 0.292175, 0.233740, 0.186992], 'p_i': 40, 'u_i': 2.2786},
        {'id': 3, 'e_m': 4.175854, 'e_o_k': [1.980419, 1.584335, 1.267468, 1.013974], 'p_i': 80, 'u_i': 1.5604},
        {'id': 4, 'e_m': 4.336894, 'e_o_k': [2.056793, 1.645434, 1.316347, 1.053078], 'p_i': 80, 'u_i': 1.1253},
        {'id': 5, 'e_m': 12.059321, 'e_o_k': [5.719190, 4.575352, 3.660282, 2.928225], 'p_i': 80, 'u_i': 3.7966},
        {'id': 6, 'e_m': 0.192411, 'e_o_k': [0.091252, 0.073001, 0.058401, 0.046721], 'p_i': 10, 'u_i': 1.2428},
        {'id': 7, 'e_m': 0.387543, 'e_o_k': [0.183794, 0.147035, 0.117628, 0.094103], 'p_i': 40, 'u_i': 4.6455},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
