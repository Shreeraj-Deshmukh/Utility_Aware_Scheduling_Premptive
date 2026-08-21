"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 93.471995, "H": 80, "J": 21, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.1, "seed": 1019, "set": 19, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.10"}
"""

_SPEC = '{"B": 93.471995, "H": 80, "J": 21, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.1, "seed": 1019, "set": 19, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.529710, 'e_o_k': [0.725472, 0.580378, 0.464302, 0.371442], 'p_i': 10, 'u_i': 1.9017},
        {'id': 1, 'e_m': 1.119012, 'e_o_k': [0.870343, 0.696274], 'p_i': 20, 'u_i': 4.1004},
        {'id': 2, 'e_m': 0.375318, 'e_o_k': [0.177997, 0.142397, 0.113918, 0.091134], 'p_i': 40, 'u_i': 2.6358},
        {'id': 3, 'e_m': 2.653251, 'e_o_k': [1.522357, 1.217886, 0.974308], 'p_i': 80, 'u_i': 4.3577},
        {'id': 4, 'e_m': 0.027963, 'e_o_k': [0.013262, 0.010609, 0.008487, 0.006790], 'p_i': 40, 'u_i': 4.2383},
        {'id': 5, 'e_m': 0.045505, 'e_o_k': [0.018951, 0.015161, 0.012129, 0.009703, 0.007762], 'p_i': 80, 'u_i': 1.1754},
        {'id': 6, 'e_m': 9.092843, 'e_o_k': [7.072211, 5.657769], 'p_i': 80, 'u_i': 2.9766},
        {'id': 7, 'e_m': 1.344054, 'e_o_k': [0.510039, 0.408031, 0.326425, 0.261140, 0.208912, 0.167130], 'p_i': 40, 'u_i': 4.8798},
    ]
    B_BUDGET = 93.471995
    return processors, tasks, B_BUDGET
