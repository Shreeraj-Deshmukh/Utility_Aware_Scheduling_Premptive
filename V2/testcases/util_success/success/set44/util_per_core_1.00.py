"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199985, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199985, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.545545, 'e_o_k': [0.558879, 0.447103, 0.357682], 'p_i': 10, 'u_i': 2.4225},
        {'id': 1, 'e_m': 0.380824, 'e_o_k': [0.030967, 0.024774, 0.019819, 0.015855, 0.012684, 0.010147], 'p_i': 20, 'u_i': 3.0832},
        {'id': 2, 'e_m': 2.703784, 'e_o_k': [0.241294, 0.193035, 0.154428, 0.123543, 0.098834], 'p_i': 40, 'u_i': 3.4868},
        {'id': 3, 'e_m': 10.624873, 'e_o_k': [1.770812, 1.416650], 'p_i': 80, 'u_i': 3.8765},
        {'id': 4, 'e_m': 19.795205, 'e_o_k': [1.766588, 1.413270, 1.130616, 0.904493, 0.723594], 'p_i': 40, 'u_i': 3.4288},
        {'id': 5, 'e_m': 8.236744, 'e_o_k': [1.012714, 0.810172, 0.648137], 'p_i': 20, 'u_i': 3.2994},
        {'id': 6, 'e_m': 3.046678, 'e_o_k': [0.309622, 0.247697, 0.198158, 0.158526], 'p_i': 20, 'u_i': 1.7707},
        {'id': 7, 'e_m': 10.677900, 'e_o_k': [1.085152, 0.868122, 0.694498, 0.555598], 'p_i': 40, 'u_i': 4.2984},
    ]
    B_BUDGET = 239.199985
    return processors, tasks, B_BUDGET
