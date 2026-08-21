"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199994, "H": 80, "J": 24, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "utility", "util_per_core": 0.2, "value": "1.0-5.0"}
"""

_SPEC = '{"B": 55.199994, "H": 80, "J": 24, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "utility", "util_per_core": 0.2, "value": "1.0-5.0"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.823643, 'e_o_k': [0.111627, 0.089301, 0.071441, 0.057153, 0.045722, 0.036578], 'p_i': 10, 'u_i': 3.9772},
        {'id': 1, 'e_m': 0.017150, 'e_o_k': [0.002905, 0.002324, 0.001859, 0.001487], 'p_i': 20, 'u_i': 1.4627},
        {'id': 2, 'e_m': 1.462946, 'e_o_k': [0.406374, 0.325099], 'p_i': 40, 'u_i': 4.5040},
        {'id': 3, 'e_m': 0.827621, 'e_o_k': [0.169594, 0.135676, 0.108540], 'p_i': 80, 'u_i': 4.7123},
        {'id': 4, 'e_m': 0.489062, 'e_o_k': [0.072742, 0.058194, 0.046555, 0.037244, 0.029795], 'p_i': 20, 'u_i': 4.3702},
        {'id': 5, 'e_m': 0.934156, 'e_o_k': [0.158224, 0.126579, 0.101264, 0.081011], 'p_i': 40, 'u_i': 3.7678},
        {'id': 6, 'e_m': 7.716508, 'e_o_k': [1.306997, 1.045597, 0.836478, 0.669182], 'p_i': 80, 'u_i': 3.2312},
        {'id': 7, 'e_m': 5.023836, 'e_o_k': [1.029474, 0.823580, 0.658864], 'p_i': 40, 'u_i': 3.7207},
    ]
    B_BUDGET = 55.199994
    return processors, tasks, B_BUDGET
