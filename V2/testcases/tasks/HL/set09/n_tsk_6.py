"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399993, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399993, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.321452, 'e_o_k': [0.475707, 0.380566, 0.304453], 'p_i': 10, 'u_i': 2.0997},
        {'id': 1, 'e_m': 1.867881, 'e_o_k': [0.518856, 0.415085], 'p_i': 20, 'u_i': 1.8132},
        {'id': 2, 'e_m': 10.883768, 'e_o_k': [1.475053, 1.180042, 0.944034, 0.755227, 0.604182, 0.483345], 'p_i': 40, 'u_i': 1.3118},
        {'id': 3, 'e_m': 4.486259, 'e_o_k': [0.667280, 0.533824, 0.427059, 0.341648, 0.273318], 'p_i': 80, 'u_i': 1.6432},
        {'id': 4, 'e_m': 0.235105, 'e_o_k': [0.065307, 0.052246], 'p_i': 20, 'u_i': 3.2827},
        {'id': 5, 'e_m': 2.690661, 'e_o_k': [0.400205, 0.320164, 0.256131, 0.204905, 0.163924], 'p_i': 20, 'u_i': 1.0597},
    ]
    B_BUDGET = 110.399993
    return processors, tasks, B_BUDGET
