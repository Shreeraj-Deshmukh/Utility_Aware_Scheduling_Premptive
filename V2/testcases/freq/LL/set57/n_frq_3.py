"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200017, "H": 80, "J": 27, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "freq", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200017, "H": 80, "J": 27, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "freq", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.7, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.7, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.100744, 'e_o_k': [0.014985, 0.011988, 0.009590, 0.007672, 0.006138], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 0.720915, 'e_o_k': [0.097704, 0.078163, 0.062531, 0.050024, 0.040020, 0.032016], 'p_i': 20, 'u_i': 3.3967},
        {'id': 2, 'e_m': 4.330945, 'e_o_k': [1.203040, 0.962432], 'p_i': 40, 'u_i': 1.9449},
        {'id': 3, 'e_m': 4.451086, 'e_o_k': [1.236413, 0.989130], 'p_i': 80, 'u_i': 4.6056},
        {'id': 4, 'e_m': 2.996813, 'e_o_k': [0.832448, 0.665958], 'p_i': 40, 'u_i': 2.0280},
        {'id': 5, 'e_m': 2.171206, 'e_o_k': [0.294259, 0.235407, 0.188326, 0.150661, 0.120528, 0.096423], 'p_i': 80, 'u_i': 1.2717},
        {'id': 6, 'e_m': 0.650677, 'e_o_k': [0.180744, 0.144595], 'p_i': 10, 'u_i': 1.1584},
        {'id': 7, 'e_m': 1.827166, 'e_o_k': [0.374419, 0.299535, 0.239628], 'p_i': 80, 'u_i': 3.8897},
    ]
    B_BUDGET = 55.200017
    return processors, tasks, B_BUDGET
