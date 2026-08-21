"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 46.000005, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.5, "seed": 1066, "set": 66, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.50"}
"""

_SPEC = '{"B": 46.000005, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.5, "seed": 1066, "set": 66, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.067141, 'e_o_k': [0.011372, 0.009098, 0.007278, 0.005823], 'p_i': 10, 'u_i': 3.0491},
        {'id': 1, 'e_m': 0.797553, 'e_o_k': [0.118627, 0.094902, 0.075921, 0.060737, 0.048590], 'p_i': 20, 'u_i': 3.9469},
        {'id': 2, 'e_m': 2.043499, 'e_o_k': [0.418750, 0.335000, 0.268000], 'p_i': 40, 'u_i': 1.2331},
        {'id': 3, 'e_m': 5.056120, 'e_o_k': [1.036090, 0.828872, 0.663098], 'p_i': 80, 'u_i': 3.8857},
        {'id': 4, 'e_m': 0.957980, 'e_o_k': [0.266105, 0.212884], 'p_i': 20, 'u_i': 4.4773},
        {'id': 5, 'e_m': 0.502682, 'e_o_k': [0.139634, 0.111707], 'p_i': 10, 'u_i': 2.4546},
        {'id': 6, 'e_m': 0.546749, 'e_o_k': [0.092607, 0.074085, 0.059268, 0.047415], 'p_i': 80, 'u_i': 1.1544},
        {'id': 7, 'e_m': 10.729419, 'e_o_k': [2.198651, 1.758921, 1.407137], 'p_i': 80, 'u_i': 4.0204},
    ]
    B_BUDGET = 46.000005
    return processors, tasks, B_BUDGET
