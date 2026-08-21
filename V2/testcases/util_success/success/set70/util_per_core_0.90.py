"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279967, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279967, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.661125, 'e_o_k': [0.148244, 0.118595, 0.094876, 0.075901, 0.060721], 'p_i': 10, 'u_i': 1.3844},
        {'id': 1, 'e_m': 6.545165, 'e_o_k': [0.584112, 0.467289, 0.373831, 0.299065, 0.239252], 'p_i': 20, 'u_i': 3.8571},
        {'id': 2, 'e_m': 8.537137, 'e_o_k': [1.422856, 1.138285], 'p_i': 40, 'u_i': 3.6185},
        {'id': 3, 'e_m': 1.154609, 'e_o_k': [0.117338, 0.093871, 0.075096, 0.060077], 'p_i': 80, 'u_i': 1.1495},
        {'id': 4, 'e_m': 4.680186, 'e_o_k': [0.475629, 0.380503, 0.304402, 0.243522], 'p_i': 20, 'u_i': 2.9121},
        {'id': 5, 'e_m': 2.402832, 'e_o_k': [0.214436, 0.171549, 0.137239, 0.109791, 0.087833], 'p_i': 10, 'u_i': 1.1301},
        {'id': 6, 'e_m': 5.498282, 'e_o_k': [0.916380, 0.733104], 'p_i': 20, 'u_i': 4.2884},
        {'id': 7, 'e_m': 3.295616, 'e_o_k': [0.294111, 0.235289, 0.188231, 0.150585, 0.120468], 'p_i': 10, 'u_i': 4.6426},
    ]
    B_BUDGET = 215.279967
    return processors, tasks, B_BUDGET
