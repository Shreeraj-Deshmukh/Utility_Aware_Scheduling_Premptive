"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119993, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119993, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.138225, 'e_o_k': [0.689704, 0.551763], 'p_i': 10, 'u_i': 2.5753},
        {'id': 1, 'e_m': 5.951187, 'e_o_k': [0.731703, 0.585363, 0.468290], 'p_i': 20, 'u_i': 3.8279},
        {'id': 2, 'e_m': 15.093985, 'e_o_k': [1.533942, 1.227153, 0.981723, 0.785378], 'p_i': 40, 'u_i': 4.1778},
        {'id': 3, 'e_m': 0.898761, 'e_o_k': [0.073084, 0.058467, 0.046774, 0.037419, 0.029935, 0.023948], 'p_i': 80, 'u_i': 4.0918},
        {'id': 4, 'e_m': 4.626017, 'e_o_k': [0.568773, 0.455018, 0.364014], 'p_i': 80, 'u_i': 1.0208},
        {'id': 5, 'e_m': 8.132145, 'e_o_k': [0.725739, 0.580591, 0.464473, 0.371578, 0.297263], 'p_i': 20, 'u_i': 3.6355},
        {'id': 6, 'e_m': 9.777421, 'e_o_k': [1.629570, 1.303656], 'p_i': 40, 'u_i': 2.2263},
        {'id': 7, 'e_m': 7.823320, 'e_o_k': [0.795053, 0.636042, 0.508834, 0.407067], 'p_i': 20, 'u_i': 2.4741},
    ]
    B_BUDGET = 263.119993
    return processors, tasks, B_BUDGET
