"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.567565, 'e_o_k': [0.435435, 0.348348], 'p_i': 10, 'u_i': 1.2013},
        {'id': 1, 'e_m': 0.270439, 'e_o_k': [0.055418, 0.044334, 0.035467], 'p_i': 20, 'u_i': 4.4940},
        {'id': 2, 'e_m': 16.617201, 'e_o_k': [2.252093, 1.801674, 1.441339, 1.153071, 0.922457, 0.737966], 'p_i': 40, 'u_i': 4.9438},
        {'id': 3, 'e_m': 17.143319, 'e_o_k': [2.323396, 1.858717, 1.486974, 1.189579, 0.951663, 0.761330], 'p_i': 80, 'u_i': 2.3791},
    ]
    B_BUDGET = 110.399995
    return processors, tasks, B_BUDGET
