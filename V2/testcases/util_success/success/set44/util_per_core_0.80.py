"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359992, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359992, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.636436, 'e_o_k': [0.447103, 0.357682, 0.286146], 'p_i': 10, 'u_i': 2.4225},
        {'id': 1, 'e_m': 0.304660, 'e_o_k': [0.024774, 0.019819, 0.015855, 0.012684, 0.010147, 0.008118], 'p_i': 20, 'u_i': 3.0832},
        {'id': 2, 'e_m': 2.163027, 'e_o_k': [0.193035, 0.154428, 0.123543, 0.098834, 0.079067], 'p_i': 40, 'u_i': 3.4868},
        {'id': 3, 'e_m': 8.499899, 'e_o_k': [1.416650, 1.133320], 'p_i': 80, 'u_i': 3.8765},
        {'id': 4, 'e_m': 15.836164, 'e_o_k': [1.413270, 1.130616, 0.904493, 0.723594, 0.578875], 'p_i': 40, 'u_i': 3.4288},
        {'id': 5, 'e_m': 6.589395, 'e_o_k': [0.810172, 0.648137, 0.518510], 'p_i': 20, 'u_i': 3.2994},
        {'id': 6, 'e_m': 2.437343, 'e_o_k': [0.247697, 0.198158, 0.158526, 0.126821], 'p_i': 20, 'u_i': 1.7707},
        {'id': 7, 'e_m': 8.542320, 'e_o_k': [0.868122, 0.694498, 0.555598, 0.444478], 'p_i': 40, 'u_i': 4.2984},
    ]
    B_BUDGET = 191.359992
    return processors, tasks, B_BUDGET
