"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520006, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520006, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.083687, 'e_o_k': [0.180615, 0.144492], 'p_i': 10, 'u_i': 1.0216},
        {'id': 1, 'e_m': 4.630332, 'e_o_k': [0.569303, 0.455442, 0.364354], 'p_i': 20, 'u_i': 4.0085},
        {'id': 2, 'e_m': 16.819008, 'e_o_k': [2.067911, 1.654329, 1.323463], 'p_i': 40, 'u_i': 1.9931},
        {'id': 3, 'e_m': 6.699098, 'e_o_k': [0.823660, 0.658928, 0.527142], 'p_i': 80, 'u_i': 2.4773},
        {'id': 4, 'e_m': 0.253259, 'e_o_k': [0.025738, 0.020590, 0.016472, 0.013178], 'p_i': 80, 'u_i': 3.1022},
        {'id': 5, 'e_m': 2.982121, 'e_o_k': [0.242496, 0.193997, 0.155198, 0.124158, 0.099326, 0.079461], 'p_i': 40, 'u_i': 1.9821},
        {'id': 6, 'e_m': 11.866832, 'e_o_k': [1.459037, 1.167229, 0.933784], 'p_i': 80, 'u_i': 1.2190},
        {'id': 7, 'e_m': 10.387727, 'e_o_k': [1.055663, 0.844531, 0.675625, 0.540500], 'p_i': 80, 'u_i': 2.8489},
    ]
    B_BUDGET = 143.520006
    return processors, tasks, B_BUDGET
