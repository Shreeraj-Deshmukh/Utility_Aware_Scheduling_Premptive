"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119993, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119993, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.113404, 'e_o_k': [0.009222, 0.007377, 0.005902, 0.004721, 0.003777, 0.003022], 'p_i': 10, 'u_i': 2.6826},
        {'id': 1, 'e_m': 8.466492, 'e_o_k': [1.411082, 1.128866], 'p_i': 20, 'u_i': 3.7355},
        {'id': 2, 'e_m': 17.986496, 'e_o_k': [1.605173, 1.284138, 1.027311, 0.821848, 0.657479], 'p_i': 40, 'u_i': 1.4955},
        {'id': 3, 'e_m': 8.236430, 'e_o_k': [1.372738, 1.098191], 'p_i': 80, 'u_i': 2.6687},
        {'id': 4, 'e_m': 10.231965, 'e_o_k': [1.258029, 1.006423, 0.805138], 'p_i': 80, 'u_i': 2.2975},
        {'id': 5, 'e_m': 38.572894, 'e_o_k': [3.920010, 3.136008, 2.508806, 2.007045], 'p_i': 80, 'u_i': 1.1081},
        {'id': 6, 'e_m': 37.367312, 'e_o_k': [3.797491, 3.037993, 2.430394, 1.944315], 'p_i': 80, 'u_i': 4.2565},
        {'id': 7, 'e_m': 5.422601, 'e_o_k': [0.903767, 0.723013], 'p_i': 40, 'u_i': 2.5120},
    ]
    B_BUDGET = 263.119993
    return processors, tasks, B_BUDGET
