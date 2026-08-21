"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.6, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.6, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.824276, 'e_o_k': [0.388646, 0.310917, 0.248733, 0.198987], 'p_i': 10, 'u_i': 1.9017},
        {'id': 1, 'e_m': 2.797530, 'e_o_k': [0.466255, 0.373004], 'p_i': 20, 'u_i': 4.1004},
        {'id': 2, 'e_m': 0.938296, 'e_o_k': [0.095355, 0.076284, 0.061027, 0.048822], 'p_i': 40, 'u_i': 2.6358},
        {'id': 3, 'e_m': 6.633127, 'e_o_k': [0.815548, 0.652439, 0.521951], 'p_i': 80, 'u_i': 4.3577},
        {'id': 4, 'e_m': 0.069907, 'e_o_k': [0.007104, 0.005684, 0.004547, 0.003637], 'p_i': 40, 'u_i': 4.2383},
        {'id': 5, 'e_m': 0.113761, 'e_o_k': [0.010152, 0.008122, 0.006498, 0.005198, 0.004158], 'p_i': 80, 'u_i': 1.1754},
        {'id': 6, 'e_m': 22.732107, 'e_o_k': [3.788685, 3.030948], 'p_i': 80, 'u_i': 2.9766},
        {'id': 7, 'e_m': 3.360136, 'e_o_k': [0.273235, 0.218588, 0.174870, 0.139896, 0.111917, 0.089534], 'p_i': 40, 'u_i': 4.8798},
    ]
    B_BUDGET = 119.600000
    return processors, tasks, B_BUDGET
