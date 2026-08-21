"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399977, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.399977, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.198341, 'e_o_k': [0.199723, 0.199723, 0.199723], 'p_i': 10, 'u_i': 3.9348},
        {'id': 1, 'e_m': 8.371318, 'e_o_k': [2.092830, 2.092830], 'p_i': 20, 'u_i': 2.2078},
        {'id': 2, 'e_m': 0.294500, 'e_o_k': [0.036812, 0.036812, 0.036812, 0.036812], 'p_i': 40, 'u_i': 1.5646},
        {'id': 3, 'e_m': 2.148895, 'e_o_k': [0.537224, 0.537224], 'p_i': 80, 'u_i': 4.4075},
        {'id': 4, 'e_m': 0.418546, 'e_o_k': [0.104636, 0.104636], 'p_i': 10, 'u_i': 2.2030},
        {'id': 5, 'e_m': 0.283932, 'e_o_k': [0.047322, 0.047322, 0.047322], 'p_i': 80, 'u_i': 2.4770},
        {'id': 6, 'e_m': 0.627393, 'e_o_k': [0.052283, 0.052283, 0.052283, 0.052283, 0.052283, 0.052283], 'p_i': 80, 'u_i': 1.9604},
        {'id': 7, 'e_m': 3.482604, 'e_o_k': [0.435325, 0.435325, 0.435325, 0.435325], 'p_i': 20, 'u_i': 2.4961},
    ]
    B_BUDGET = 110.399977
    return processors, tasks, B_BUDGET
