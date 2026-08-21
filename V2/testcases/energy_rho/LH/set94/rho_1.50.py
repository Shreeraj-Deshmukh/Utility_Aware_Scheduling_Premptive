"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 114.079996, "H": 80, "J": 21, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.5, "seed": 1094, "set": 94, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.50"}
"""

_SPEC = '{"B": 114.079996, "H": 80, "J": 21, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.5, "seed": 1094, "set": 94, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.333816, 'e_o_k': [0.158314, 0.126651, 0.101321, 0.081057], 'p_i': 10, 'u_i': 1.6879},
        {'id': 1, 'e_m': 0.511403, 'e_o_k': [0.242535, 0.194028, 0.155222, 0.124178], 'p_i': 20, 'u_i': 2.2588},
        {'id': 2, 'e_m': 2.476328, 'e_o_k': [1.926033, 1.540827], 'p_i': 40, 'u_i': 4.0829},
        {'id': 3, 'e_m': 3.763800, 'e_o_k': [2.159558, 1.727646, 1.382117], 'p_i': 80, 'u_i': 1.6866},
        {'id': 4, 'e_m': 0.262962, 'e_o_k': [0.150880, 0.120704, 0.096563], 'p_i': 40, 'u_i': 3.5950},
        {'id': 5, 'e_m': 7.850730, 'e_o_k': [6.106123, 4.884898], 'p_i': 80, 'u_i': 4.2025},
        {'id': 6, 'e_m': 3.101814, 'e_o_k': [2.412522, 1.930018], 'p_i': 40, 'u_i': 3.6883},
        {'id': 7, 'e_m': 3.987120, 'e_o_k': [3.101093, 2.480874], 'p_i': 80, 'u_i': 1.6967},
    ]
    B_BUDGET = 114.079996
    return processors, tasks, B_BUDGET
