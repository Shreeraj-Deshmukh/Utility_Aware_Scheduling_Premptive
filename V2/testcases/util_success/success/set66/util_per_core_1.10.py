"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120009, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120009, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.628381, 'e_o_k': [0.569063, 0.455251, 0.364200], 'p_i': 10, 'u_i': 4.6145},
        {'id': 1, 'e_m': 5.460537, 'e_o_k': [0.910090, 0.728072], 'p_i': 20, 'u_i': 1.3416},
        {'id': 2, 'e_m': 14.076248, 'e_o_k': [1.256210, 1.004968, 0.803974, 0.643179, 0.514543], 'p_i': 40, 'u_i': 3.7595},
        {'id': 3, 'e_m': 3.581504, 'e_o_k': [0.319625, 0.255700, 0.204560, 0.163648, 0.130918], 'p_i': 80, 'u_i': 4.3540},
        {'id': 4, 'e_m': 15.133013, 'e_o_k': [1.230566, 0.984453, 0.787562, 0.630050, 0.504040, 0.403232], 'p_i': 40, 'u_i': 3.6734},
        {'id': 5, 'e_m': 12.987757, 'e_o_k': [1.596855, 1.277484, 1.021987], 'p_i': 80, 'u_i': 4.6535},
        {'id': 6, 'e_m': 9.270451, 'e_o_k': [0.753842, 0.603074, 0.482459, 0.385967, 0.308774, 0.247019], 'p_i': 80, 'u_i': 4.4620},
        {'id': 7, 'e_m': 4.109072, 'e_o_k': [0.417589, 0.334071, 0.267257, 0.213805], 'p_i': 10, 'u_i': 4.1539},
    ]
    B_BUDGET = 263.120009
    return processors, tasks, B_BUDGET
