"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279991, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279991, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.786556, 'e_o_k': [0.145277, 0.116221, 0.092977, 0.074382, 0.059505, 0.047604], 'p_i': 10, 'u_i': 1.8568},
        {'id': 1, 'e_m': 8.258946, 'e_o_k': [1.015444, 0.812355, 0.649884], 'p_i': 20, 'u_i': 1.8128},
        {'id': 2, 'e_m': 4.319632, 'e_o_k': [0.719939, 0.575951], 'p_i': 40, 'u_i': 1.5689},
        {'id': 3, 'e_m': 6.449661, 'e_o_k': [0.655453, 0.524363, 0.419490, 0.335592], 'p_i': 80, 'u_i': 4.8976},
        {'id': 4, 'e_m': 1.714110, 'e_o_k': [0.139386, 0.111509, 0.089207, 0.071366, 0.057092, 0.045674], 'p_i': 40, 'u_i': 2.5447},
        {'id': 5, 'e_m': 18.376002, 'e_o_k': [3.062667, 2.450134], 'p_i': 40, 'u_i': 1.6969},
        {'id': 6, 'e_m': 5.229839, 'e_o_k': [0.531488, 0.425190, 0.340152, 0.272122], 'p_i': 80, 'u_i': 4.6966},
        {'id': 7, 'e_m': 36.172778, 'e_o_k': [3.228175, 2.582540, 2.066032, 1.652826, 1.322261], 'p_i': 80, 'u_i': 4.2096},
    ]
    B_BUDGET = 215.279991
    return processors, tasks, B_BUDGET
