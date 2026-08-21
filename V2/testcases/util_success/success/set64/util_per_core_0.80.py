"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359998, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359998, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.886697, 'e_o_k': [0.257618, 0.206095, 0.164876, 0.131900, 0.105520], 'p_i': 10, 'u_i': 4.7302},
        {'id': 1, 'e_m': 9.984555, 'e_o_k': [1.664092, 1.331274], 'p_i': 20, 'u_i': 1.8342},
        {'id': 2, 'e_m': 3.546002, 'e_o_k': [0.435984, 0.348787, 0.279030], 'p_i': 40, 'u_i': 2.1428},
        {'id': 3, 'e_m': 9.641844, 'e_o_k': [0.979862, 0.783890, 0.627112, 0.501689], 'p_i': 80, 'u_i': 3.7337},
        {'id': 4, 'e_m': 11.793448, 'e_o_k': [1.052485, 0.841988, 0.673591, 0.538872, 0.431098], 'p_i': 40, 'u_i': 3.4112},
        {'id': 5, 'e_m': 18.387549, 'e_o_k': [3.064591, 2.451673], 'p_i': 80, 'u_i': 2.7179},
        {'id': 6, 'e_m': 0.019037, 'e_o_k': [0.001935, 0.001548, 0.001238, 0.000991], 'p_i': 40, 'u_i': 2.6898},
        {'id': 7, 'e_m': 1.555459, 'e_o_k': [0.191245, 0.152996, 0.122397], 'p_i': 20, 'u_i': 4.5690},
    ]
    B_BUDGET = 191.359998
    return processors, tasks, B_BUDGET
