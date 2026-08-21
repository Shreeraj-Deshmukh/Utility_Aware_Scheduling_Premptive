"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600009, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600009, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.072128, 'e_o_k': [0.008868, 0.007095, 0.005676], 'p_i': 10, 'u_i': 3.1857},
        {'id': 1, 'e_m': 1.062609, 'e_o_k': [0.177102, 0.141681], 'p_i': 20, 'u_i': 3.0673},
        {'id': 2, 'e_m': 0.928691, 'e_o_k': [0.082879, 0.066304, 0.053043, 0.042434, 0.033947], 'p_i': 40, 'u_i': 1.1608},
        {'id': 3, 'e_m': 8.997619, 'e_o_k': [1.106265, 0.885012, 0.708009], 'p_i': 80, 'u_i': 3.0557},
        {'id': 4, 'e_m': 13.551392, 'e_o_k': [1.209370, 0.967496, 0.773997, 0.619197, 0.495358], 'p_i': 80, 'u_i': 1.7105},
        {'id': 5, 'e_m': 37.928395, 'e_o_k': [4.663327, 3.730662, 2.984529], 'p_i': 80, 'u_i': 2.7562},
        {'id': 6, 'e_m': 1.584358, 'e_o_k': [0.161012, 0.128810, 0.103048, 0.082438], 'p_i': 20, 'u_i': 4.1777},
        {'id': 7, 'e_m': 6.500320, 'e_o_k': [1.083387, 0.866709], 'p_i': 80, 'u_i': 1.3396},
    ]
    B_BUDGET = 119.600009
    return processors, tasks, B_BUDGET
