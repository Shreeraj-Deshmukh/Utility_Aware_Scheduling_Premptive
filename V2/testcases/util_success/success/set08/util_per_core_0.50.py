"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599999, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599999, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.267517, 'e_o_k': [0.032891, 0.026313, 0.021051], 'p_i': 10, 'u_i': 3.1459},
        {'id': 1, 'e_m': 0.433869, 'e_o_k': [0.053345, 0.042676, 0.034141], 'p_i': 20, 'u_i': 1.5731},
        {'id': 2, 'e_m': 3.796804, 'e_o_k': [0.632801, 0.506241], 'p_i': 40, 'u_i': 4.9538},
        {'id': 3, 'e_m': 28.828465, 'e_o_k': [2.572745, 2.058196, 1.646557, 1.317245, 1.053796], 'p_i': 80, 'u_i': 2.3994},
        {'id': 4, 'e_m': 5.931379, 'e_o_k': [0.988563, 0.790851], 'p_i': 40, 'u_i': 1.5904},
        {'id': 5, 'e_m': 12.435011, 'e_o_k': [1.528895, 1.223116, 0.978493], 'p_i': 40, 'u_i': 2.4893},
        {'id': 6, 'e_m': 0.155177, 'e_o_k': [0.019079, 0.015263, 0.012211], 'p_i': 20, 'u_i': 4.7173},
        {'id': 7, 'e_m': 2.348821, 'e_o_k': [0.391470, 0.313176], 'p_i': 80, 'u_i': 2.7558},
    ]
    B_BUDGET = 119.599999
    return processors, tasks, B_BUDGET
