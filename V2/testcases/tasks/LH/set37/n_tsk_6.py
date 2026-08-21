"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320008, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320008, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.561109, 'e_o_k': [0.895718, 0.716574, 0.573260], 'p_i': 10, 'u_i': 4.5515},
        {'id': 1, 'e_m': 0.460144, 'e_o_k': [0.357890, 0.286312], 'p_i': 20, 'u_i': 3.0521},
        {'id': 2, 'e_m': 1.133580, 'e_o_k': [0.537606, 0.430085, 0.344068, 0.275254], 'p_i': 40, 'u_i': 1.1668},
        {'id': 3, 'e_m': 12.114088, 'e_o_k': [9.422068, 7.537655], 'p_i': 80, 'u_i': 2.3448},
        {'id': 4, 'e_m': 1.064930, 'e_o_k': [0.443509, 0.354808, 0.283846, 0.227077, 0.181661], 'p_i': 40, 'u_i': 3.9461},
        {'id': 5, 'e_m': 0.289862, 'e_o_k': [0.137468, 0.109975, 0.087980, 0.070384], 'p_i': 20, 'u_i': 2.2173},
    ]
    B_BUDGET = 88.320008
    return processors, tasks, B_BUDGET
