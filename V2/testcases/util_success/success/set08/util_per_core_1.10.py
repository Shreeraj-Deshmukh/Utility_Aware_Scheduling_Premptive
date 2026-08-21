"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119998, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119998, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.441306, 'e_o_k': [0.248100, 0.198480, 0.158784, 0.127027], 'p_i': 10, 'u_i': 1.1912},
        {'id': 1, 'e_m': 4.878262, 'e_o_k': [0.396684, 0.317347, 0.253878, 0.203102, 0.162482, 0.129985], 'p_i': 20, 'u_i': 1.9657},
        {'id': 2, 'e_m': 13.250790, 'e_o_k': [1.629196, 1.303356, 1.042685], 'p_i': 40, 'u_i': 2.1965},
        {'id': 3, 'e_m': 2.857433, 'e_o_k': [0.351324, 0.281059, 0.224847], 'p_i': 80, 'u_i': 2.9990},
        {'id': 4, 'e_m': 25.782876, 'e_o_k': [2.620211, 2.096169, 1.676935, 1.341548], 'p_i': 80, 'u_i': 2.8058},
        {'id': 5, 'e_m': 13.237774, 'e_o_k': [1.181382, 0.945105, 0.756084, 0.604867, 0.483894], 'p_i': 40, 'u_i': 2.9621},
        {'id': 6, 'e_m': 12.066126, 'e_o_k': [1.483540, 1.186832, 0.949466], 'p_i': 40, 'u_i': 3.1505},
        {'id': 7, 'e_m': 31.206820, 'e_o_k': [5.201137, 4.160909], 'p_i': 80, 'u_i': 4.5579},
    ]
    B_BUDGET = 263.119998
    return processors, tasks, B_BUDGET
