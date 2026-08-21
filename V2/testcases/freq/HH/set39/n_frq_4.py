"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640007, "H": 80, "J": 35, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "freq", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640007, "H": 80, "J": 35, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "freq", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.435325, 'e_o_k': [0.338586, 0.270869], 'p_i': 10, 'u_i': 1.4412},
        {'id': 1, 'e_m': 3.692417, 'e_o_k': [1.751146, 1.400917, 1.120733, 0.896587], 'p_i': 20, 'u_i': 3.7136},
        {'id': 2, 'e_m': 1.661795, 'e_o_k': [0.630614, 0.504492, 0.403593, 0.322875, 0.258300, 0.206640], 'p_i': 40, 'u_i': 3.0715},
        {'id': 3, 'e_m': 21.880045, 'e_o_k': [8.302992, 6.642394, 5.313915, 4.251132, 3.400906, 2.720724], 'p_i': 80, 'u_i': 2.1053},
        {'id': 4, 'e_m': 0.175787, 'e_o_k': [0.136723, 0.109378], 'p_i': 20, 'u_i': 3.9261},
        {'id': 5, 'e_m': 0.532000, 'e_o_k': [0.413778, 0.331022], 'p_i': 20, 'u_i': 2.2961},
        {'id': 6, 'e_m': 0.171451, 'e_o_k': [0.071404, 0.057123, 0.045699, 0.036559, 0.029247], 'p_i': 10, 'u_i': 1.3761},
        {'id': 7, 'e_m': 4.085336, 'e_o_k': [2.344045, 1.875236, 1.500189], 'p_i': 20, 'u_i': 2.1930},
    ]
    B_BUDGET = 176.640007
    return processors, tasks, B_BUDGET
