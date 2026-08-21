"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119997, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119997, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.355510, 'e_o_k': [0.442633, 0.354106, 0.283285, 0.226628], 'p_i': 10, 'u_i': 1.9313},
        {'id': 1, 'e_m': 8.003015, 'e_o_k': [1.333836, 1.067069], 'p_i': 20, 'u_i': 4.0147},
        {'id': 2, 'e_m': 18.763887, 'e_o_k': [1.525817, 1.220654, 0.976523, 0.781218, 0.624975, 0.499980], 'p_i': 40, 'u_i': 3.8759},
        {'id': 3, 'e_m': 8.304095, 'e_o_k': [1.020995, 0.816796, 0.653437], 'p_i': 80, 'u_i': 4.3076},
        {'id': 4, 'e_m': 10.770130, 'e_o_k': [0.875791, 0.700633, 0.560506, 0.448405, 0.358724, 0.286979], 'p_i': 80, 'u_i': 1.9116},
        {'id': 5, 'e_m': 7.442781, 'e_o_k': [0.915096, 0.732077, 0.585661], 'p_i': 40, 'u_i': 2.7475},
        {'id': 6, 'e_m': 22.636061, 'e_o_k': [2.020115, 1.616092, 1.292874, 1.034299, 0.827439], 'p_i': 80, 'u_i': 2.9584},
        {'id': 7, 'e_m': 3.755060, 'e_o_k': [0.381612, 0.305289, 0.244232, 0.195385], 'p_i': 20, 'u_i': 3.8181},
    ]
    B_BUDGET = 263.119997
    return processors, tasks, B_BUDGET
