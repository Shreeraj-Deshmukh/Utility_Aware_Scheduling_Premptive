"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399992, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399992, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.964311, 'e_o_k': [0.143430, 0.114744, 0.091795, 0.073436, 0.058749], 'p_i': 10, 'u_i': 3.2309},
        {'id': 1, 'e_m': 8.642127, 'e_o_k': [1.285419, 1.028335, 0.822668, 0.658134, 0.526507], 'p_i': 20, 'u_i': 2.9440},
        {'id': 2, 'e_m': 0.480580, 'e_o_k': [0.098479, 0.078784, 0.063027], 'p_i': 40, 'u_i': 1.5741},
        {'id': 3, 'e_m': 4.458164, 'e_o_k': [0.604205, 0.483364, 0.386691, 0.309353, 0.247482, 0.197986], 'p_i': 80, 'u_i': 1.4817},
        {'id': 4, 'e_m': 4.126083, 'e_o_k': [1.146134, 0.916907], 'p_i': 40, 'u_i': 3.4660},
        {'id': 5, 'e_m': 2.011380, 'e_o_k': [0.272598, 0.218078, 0.174463, 0.139570, 0.111656, 0.089325], 'p_i': 20, 'u_i': 3.9304},
    ]
    B_BUDGET = 110.399992
    return processors, tasks, B_BUDGET
