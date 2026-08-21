"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.222670, 'e_o_k': [0.579857, 0.463885, 0.371108, 0.296887], 'p_i': 10, 'u_i': 4.4576},
        {'id': 1, 'e_m': 0.002934, 'e_o_k': [0.002282, 0.001826], 'p_i': 20, 'u_i': 1.2102},
        {'id': 2, 'e_m': 17.452391, 'e_o_k': [10.013667, 8.010933, 6.408747], 'p_i': 40, 'u_i': 3.7306},
        {'id': 3, 'e_m': 5.457841, 'e_o_k': [3.131548, 2.505239, 2.004191], 'p_i': 80, 'u_i': 4.1325},
        {'id': 4, 'e_m': 1.018899, 'e_o_k': [0.483217, 0.386574, 0.309259, 0.247407], 'p_i': 20, 'u_i': 2.4718},
        {'id': 5, 'e_m': 4.884345, 'e_o_k': [1.853501, 1.482801, 1.186241, 0.948992, 0.759194, 0.607355], 'p_i': 40, 'u_i': 1.1369},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET
