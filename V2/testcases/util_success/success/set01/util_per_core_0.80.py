"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.36, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.36, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.050795, 'e_o_k': [0.675132, 0.540106], 'p_i': 10, 'u_i': 1.5964},
        {'id': 1, 'e_m': 0.581126, 'e_o_k': [0.096854, 0.077484], 'p_i': 20, 'u_i': 3.4312},
        {'id': 2, 'e_m': 11.185480, 'e_o_k': [1.864247, 1.491397], 'p_i': 40, 'u_i': 2.7324},
        {'id': 3, 'e_m': 8.686355, 'e_o_k': [0.882760, 0.706208, 0.564966, 0.451973], 'p_i': 80, 'u_i': 1.8023},
        {'id': 4, 'e_m': 17.971612, 'e_o_k': [2.209624, 1.767700, 1.414160], 'p_i': 40, 'u_i': 3.1548},
        {'id': 5, 'e_m': 3.336381, 'e_o_k': [0.410211, 0.328169, 0.262535], 'p_i': 40, 'u_i': 3.2967},
        {'id': 6, 'e_m': 2.978500, 'e_o_k': [0.496417, 0.397133], 'p_i': 20, 'u_i': 2.4813},
        {'id': 7, 'e_m': 7.681836, 'e_o_k': [0.944488, 0.755590, 0.604472], 'p_i': 80, 'u_i': 4.3288},
    ]
    B_BUDGET = 191.360000
    return processors, tasks, B_BUDGET
