"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 114.079998, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.1, "seed": 1073, "set": 73, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.10"}
"""

_SPEC = '{"B": 114.079998, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.1, "seed": 1073, "set": 73, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.198341, 'e_o_k': [0.245562, 0.196449, 0.157159], 'p_i': 10, 'u_i': 3.9348},
        {'id': 1, 'e_m': 8.371318, 'e_o_k': [2.325366, 1.860293], 'p_i': 20, 'u_i': 2.2078},
        {'id': 2, 'e_m': 0.294500, 'e_o_k': [0.049881, 0.039905, 0.031924, 0.025539], 'p_i': 40, 'u_i': 1.5646},
        {'id': 3, 'e_m': 2.148895, 'e_o_k': [0.596915, 0.477532], 'p_i': 80, 'u_i': 4.4075},
        {'id': 4, 'e_m': 0.418546, 'e_o_k': [0.116263, 0.093010], 'p_i': 10, 'u_i': 2.2030},
        {'id': 5, 'e_m': 0.283932, 'e_o_k': [0.058183, 0.046546, 0.037237], 'p_i': 80, 'u_i': 2.4770},
        {'id': 6, 'e_m': 0.627393, 'e_o_k': [0.085029, 0.068023, 0.054419, 0.043535, 0.034828, 0.027862], 'p_i': 80, 'u_i': 1.9604},
        {'id': 7, 'e_m': 3.482604, 'e_o_k': [0.589872, 0.471898, 0.377518, 0.302014], 'p_i': 20, 'u_i': 2.4961},
    ]
    B_BUDGET = 114.079998
    return processors, tasks, B_BUDGET
