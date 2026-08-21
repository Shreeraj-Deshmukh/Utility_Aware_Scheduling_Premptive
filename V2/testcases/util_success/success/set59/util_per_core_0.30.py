"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760008, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760008, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.190260, 'e_o_k': [0.178105, 0.142484, 0.113987, 0.091190, 0.072952, 0.058361], 'p_i': 10, 'u_i': 3.0949},
        {'id': 1, 'e_m': 0.625810, 'e_o_k': [0.076944, 0.061555, 0.049244], 'p_i': 20, 'u_i': 1.9752},
        {'id': 2, 'e_m': 3.476080, 'e_o_k': [0.310217, 0.248173, 0.198539, 0.158831, 0.127065], 'p_i': 40, 'u_i': 3.9662},
        {'id': 3, 'e_m': 0.475957, 'e_o_k': [0.058519, 0.046815, 0.037452], 'p_i': 80, 'u_i': 1.9890},
        {'id': 4, 'e_m': 2.592889, 'e_o_k': [0.231398, 0.185118, 0.148095, 0.118476, 0.094781], 'p_i': 40, 'u_i': 3.3639},
        {'id': 5, 'e_m': 0.315832, 'e_o_k': [0.032097, 0.025677, 0.020542, 0.016434], 'p_i': 10, 'u_i': 4.7869},
        {'id': 6, 'e_m': 0.310506, 'e_o_k': [0.031555, 0.025244, 0.020196, 0.016156], 'p_i': 10, 'u_i': 2.7944},
        {'id': 7, 'e_m': 1.293760, 'e_o_k': [0.215627, 0.172501], 'p_i': 10, 'u_i': 4.7769},
    ]
    B_BUDGET = 71.760008
    return processors, tasks, B_BUDGET
