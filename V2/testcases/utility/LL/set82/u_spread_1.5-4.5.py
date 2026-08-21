"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200005, "H": 80, "J": 32, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 55.200005, "H": 80, "J": 32, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.844903, 'e_o_k': [0.125670, 0.100536, 0.080429, 0.064343, 0.051474], 'p_i': 10, 'u_i': 3.6325},
        {'id': 1, 'e_m': 0.177585, 'e_o_k': [0.049329, 0.039463], 'p_i': 20, 'u_i': 3.5595},
        {'id': 2, 'e_m': 1.433543, 'e_o_k': [0.242809, 0.194247, 0.155398, 0.124318], 'p_i': 40, 'u_i': 2.5383},
        {'id': 3, 'e_m': 1.748862, 'e_o_k': [0.485795, 0.388636], 'p_i': 80, 'u_i': 3.4797},
        {'id': 4, 'e_m': 6.915032, 'e_o_k': [0.937179, 0.749743, 0.599795, 0.479836, 0.383869, 0.307095], 'p_i': 80, 'u_i': 2.2567},
        {'id': 5, 'e_m': 1.550765, 'e_o_k': [0.262663, 0.210131, 0.168105, 0.134484], 'p_i': 20, 'u_i': 3.9730},
        {'id': 6, 'e_m': 0.111141, 'e_o_k': [0.030872, 0.024698], 'p_i': 10, 'u_i': 3.4410},
        {'id': 7, 'e_m': 1.476817, 'e_o_k': [0.200150, 0.160120, 0.128096, 0.102477, 0.081981, 0.065585], 'p_i': 20, 'u_i': 3.7788},
    ]
    B_BUDGET = 55.200005
    return processors, tasks, B_BUDGET
