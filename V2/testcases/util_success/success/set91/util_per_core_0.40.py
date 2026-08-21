"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679997, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679997, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.087664, 'e_o_k': [0.181277, 0.145022], 'p_i': 10, 'u_i': 2.8418},
        {'id': 1, 'e_m': 0.391931, 'e_o_k': [0.039830, 0.031864, 0.025491, 0.020393], 'p_i': 20, 'u_i': 1.5566},
        {'id': 2, 'e_m': 13.096144, 'e_o_k': [1.330909, 1.064727, 0.851782, 0.681425], 'p_i': 40, 'u_i': 3.2695},
        {'id': 3, 'e_m': 7.655110, 'e_o_k': [1.275852, 1.020681], 'p_i': 80, 'u_i': 3.8342},
        {'id': 4, 'e_m': 0.303823, 'e_o_k': [0.024706, 0.019765, 0.015812, 0.012649, 0.010120, 0.008096], 'p_i': 20, 'u_i': 4.3734},
        {'id': 5, 'e_m': 0.754717, 'e_o_k': [0.076699, 0.061359, 0.049087, 0.039270], 'p_i': 20, 'u_i': 3.3497},
        {'id': 6, 'e_m': 5.033151, 'e_o_k': [0.511499, 0.409199, 0.327359, 0.261888], 'p_i': 40, 'u_i': 4.2042},
        {'id': 7, 'e_m': 2.791552, 'e_o_k': [0.343224, 0.274579, 0.219663], 'p_i': 40, 'u_i': 1.0373},
    ]
    B_BUDGET = 95.679997
    return processors, tasks, B_BUDGET
