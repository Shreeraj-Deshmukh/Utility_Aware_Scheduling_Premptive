"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199995, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199995, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.762023, 'e_o_k': [0.627004, 0.501603], 'p_i': 10, 'u_i': 2.5753},
        {'id': 1, 'e_m': 5.410170, 'e_o_k': [0.665185, 0.532148, 0.425718], 'p_i': 20, 'u_i': 3.8279},
        {'id': 2, 'e_m': 13.721805, 'e_o_k': [1.394492, 1.115594, 0.892475, 0.713980], 'p_i': 40, 'u_i': 4.1778},
        {'id': 3, 'e_m': 0.817055, 'e_o_k': [0.066440, 0.053152, 0.042522, 0.034017, 0.027214, 0.021771], 'p_i': 80, 'u_i': 4.0918},
        {'id': 4, 'e_m': 4.205470, 'e_o_k': [0.517066, 0.413653, 0.330922], 'p_i': 80, 'u_i': 1.0208},
        {'id': 5, 'e_m': 7.392859, 'e_o_k': [0.659763, 0.527810, 0.422248, 0.337798, 0.270239], 'p_i': 20, 'u_i': 3.6355},
        {'id': 6, 'e_m': 8.888564, 'e_o_k': [1.481427, 1.185142], 'p_i': 40, 'u_i': 2.2263},
        {'id': 7, 'e_m': 7.112109, 'e_o_k': [0.722775, 0.578220, 0.462576, 0.370061], 'p_i': 20, 'u_i': 2.4741},
    ]
    B_BUDGET = 239.199995
    return processors, tasks, B_BUDGET
