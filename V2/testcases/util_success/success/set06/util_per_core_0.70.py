"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440002, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440002, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.255781, 'e_o_k': [0.209297, 0.167437], 'p_i': 10, 'u_i': 2.0470},
        {'id': 1, 'e_m': 1.124521, 'e_o_k': [0.114281, 0.091424, 0.073140, 0.058512], 'p_i': 20, 'u_i': 4.9556},
        {'id': 2, 'e_m': 10.201217, 'e_o_k': [1.700203, 1.360162], 'p_i': 40, 'u_i': 1.3741},
        {'id': 3, 'e_m': 29.010312, 'e_o_k': [2.588974, 2.071179, 1.656943, 1.325554, 1.060444], 'p_i': 80, 'u_i': 4.6107},
        {'id': 4, 'e_m': 14.100001, 'e_o_k': [1.258329, 1.006664, 0.805331, 0.644265, 0.515412], 'p_i': 40, 'u_i': 2.5105},
        {'id': 5, 'e_m': 0.163504, 'e_o_k': [0.016616, 0.013293, 0.010634, 0.008508], 'p_i': 10, 'u_i': 2.2972},
        {'id': 6, 'e_m': 6.417722, 'e_o_k': [1.069620, 0.855696], 'p_i': 40, 'u_i': 3.0996},
        {'id': 7, 'e_m': 0.712430, 'e_o_k': [0.063580, 0.050864, 0.040691, 0.032553, 0.026042], 'p_i': 10, 'u_i': 4.5299},
    ]
    B_BUDGET = 167.440002
    return processors, tasks, B_BUDGET
