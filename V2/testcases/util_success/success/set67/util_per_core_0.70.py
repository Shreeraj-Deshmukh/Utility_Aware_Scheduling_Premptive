"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439979, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439979, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.850047, 'e_o_k': [0.165104, 0.132083, 0.105667, 0.084533, 0.067627], 'p_i': 10, 'u_i': 1.8232},
        {'id': 1, 'e_m': 2.937028, 'e_o_k': [0.262110, 0.209688, 0.167750, 0.134200, 0.107360], 'p_i': 20, 'u_i': 4.2323},
        {'id': 2, 'e_m': 9.340801, 'e_o_k': [0.833603, 0.666882, 0.533506, 0.426805, 0.341444], 'p_i': 40, 'u_i': 3.7021},
        {'id': 3, 'e_m': 7.815273, 'e_o_k': [0.960894, 0.768715, 0.614972], 'p_i': 80, 'u_i': 1.4717},
        {'id': 4, 'e_m': 2.088409, 'e_o_k': [0.256772, 0.205417, 0.164334], 'p_i': 10, 'u_i': 2.9634},
        {'id': 5, 'e_m': 8.749061, 'e_o_k': [0.780794, 0.624635, 0.499708, 0.399767, 0.319813], 'p_i': 80, 'u_i': 1.6416},
        {'id': 6, 'e_m': 3.513100, 'e_o_k': [0.313520, 0.250816, 0.200653, 0.160522, 0.128418], 'p_i': 20, 'u_i': 4.1520},
        {'id': 7, 'e_m': 2.430737, 'e_o_k': [0.247026, 0.197621, 0.158097, 0.126477], 'p_i': 10, 'u_i': 2.8128},
    ]
    B_BUDGET = 167.439979
    return processors, tasks, B_BUDGET
