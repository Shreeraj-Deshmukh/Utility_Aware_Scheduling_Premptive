"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.111464, 'e_o_k': [0.462795, 0.370236, 0.296189, 0.236951, 0.189561], 'p_i': 10, 'u_i': 2.5478},
        {'id': 1, 'e_m': 1.077629, 'e_o_k': [0.182525, 0.146020, 0.116816, 0.093453], 'p_i': 20, 'u_i': 1.9017},
        {'id': 2, 'e_m': 12.270583, 'e_o_k': [3.408495, 2.726796], 'p_i': 40, 'u_i': 4.1004},
        {'id': 3, 'e_m': 10.256603, 'e_o_k': [1.737229, 1.389784, 1.111827, 0.889461], 'p_i': 80, 'u_i': 2.6358},
    ]
    B_BUDGET = 110.399991
    return processors, tasks, B_BUDGET
