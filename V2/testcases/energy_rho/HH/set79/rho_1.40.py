"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 217.856004, "H": 80, "J": 20, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.4, "seed": 1079, "set": 79, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.40"}
"""

_SPEC = '{"B": 217.856004, "H": 80, "J": 20, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.4, "seed": 1079, "set": 79, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.680163, 'e_o_k': [0.283267, 0.226613, 0.181291, 0.145032, 0.116026], 'p_i': 10, 'u_i': 4.9110},
        {'id': 1, 'e_m': 1.689853, 'e_o_k': [0.641262, 0.513010, 0.410408, 0.328326, 0.262661, 0.210129], 'p_i': 20, 'u_i': 1.5555},
        {'id': 2, 'e_m': 0.519615, 'e_o_k': [0.298140, 0.238512, 0.190810], 'p_i': 40, 'u_i': 1.9189},
        {'id': 3, 'e_m': 18.094462, 'e_o_k': [14.073470, 11.258776], 'p_i': 80, 'u_i': 3.1608},
        {'id': 4, 'e_m': 5.009794, 'e_o_k': [3.896506, 3.117205], 'p_i': 80, 'u_i': 1.3239},
        {'id': 5, 'e_m': 1.955931, 'e_o_k': [0.927610, 0.742088, 0.593670, 0.474936], 'p_i': 80, 'u_i': 4.3282},
        {'id': 6, 'e_m': 10.750512, 'e_o_k': [8.361509, 6.689208], 'p_i': 40, 'u_i': 3.0285},
        {'id': 7, 'e_m': 4.198837, 'e_o_k': [1.991318, 1.593055, 1.274444, 1.019555], 'p_i': 80, 'u_i': 4.7214},
    ]
    B_BUDGET = 217.856004
    return processors, tasks, B_BUDGET
