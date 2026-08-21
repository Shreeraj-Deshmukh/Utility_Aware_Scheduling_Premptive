"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 38.639995, "H": 80, "J": 30, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.1, "seed": 1006, "set": 6, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.10"}
"""

_SPEC = '{"B": 38.639995, "H": 80, "J": 30, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.1, "seed": 1006, "set": 6, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.561850, 'e_o_k': [0.156070, 0.124856], 'p_i': 10, 'u_i': 2.2300},
        {'id': 1, 'e_m': 1.499211, 'e_o_k': [0.253931, 0.203145, 0.162516, 0.130013], 'p_i': 20, 'u_i': 1.1980},
        {'id': 2, 'e_m': 6.285193, 'e_o_k': [1.064565, 0.851652, 0.681322, 0.545057], 'p_i': 40, 'u_i': 3.9540},
        {'id': 3, 'e_m': 0.158746, 'e_o_k': [0.044096, 0.035277], 'p_i': 80, 'u_i': 1.1604},
        {'id': 4, 'e_m': 1.379315, 'e_o_k': [0.233624, 0.186899, 0.149519, 0.119615], 'p_i': 40, 'u_i': 4.9556},
        {'id': 5, 'e_m': 1.465455, 'e_o_k': [0.407071, 0.325657], 'p_i': 20, 'u_i': 1.3741},
        {'id': 6, 'e_m': 0.015684, 'e_o_k': [0.002333, 0.001866, 0.001493, 0.001194, 0.000956], 'p_i': 10, 'u_i': 4.6107},
        {'id': 7, 'e_m': 0.033297, 'e_o_k': [0.004953, 0.003962, 0.003170, 0.002536, 0.002029], 'p_i': 80, 'u_i': 2.5105},
    ]
    B_BUDGET = 38.639995
    return processors, tasks, B_BUDGET
