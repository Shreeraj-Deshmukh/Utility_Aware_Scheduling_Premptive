"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599999, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599999, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.359580, 'e_o_k': [0.226597, 0.181277], 'p_i': 10, 'u_i': 2.8418},
        {'id': 1, 'e_m': 0.489914, 'e_o_k': [0.049788, 0.039830, 0.031864, 0.025491], 'p_i': 20, 'u_i': 1.5566},
        {'id': 2, 'e_m': 16.370180, 'e_o_k': [1.663636, 1.330909, 1.064727, 0.851782], 'p_i': 40, 'u_i': 3.2695},
        {'id': 3, 'e_m': 9.568888, 'e_o_k': [1.594815, 1.275852], 'p_i': 80, 'u_i': 3.8342},
        {'id': 4, 'e_m': 0.379779, 'e_o_k': [0.030882, 0.024706, 0.019765, 0.015812, 0.012649, 0.010120], 'p_i': 20, 'u_i': 4.3734},
        {'id': 5, 'e_m': 0.943396, 'e_o_k': [0.095874, 0.076699, 0.061359, 0.049087], 'p_i': 20, 'u_i': 3.3497},
        {'id': 6, 'e_m': 6.291439, 'e_o_k': [0.639374, 0.511499, 0.409199, 0.327359], 'p_i': 40, 'u_i': 4.2042},
        {'id': 7, 'e_m': 3.489440, 'e_o_k': [0.429029, 0.343224, 0.274579], 'p_i': 40, 'u_i': 1.0373},
    ]
    B_BUDGET = 119.599999
    return processors, tasks, B_BUDGET
