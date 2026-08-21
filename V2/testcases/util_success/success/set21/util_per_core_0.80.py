"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359998, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359998, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.382884, 'e_o_k': [0.170027, 0.136021, 0.108817], 'p_i': 10, 'u_i': 2.6945},
        {'id': 1, 'e_m': 7.302355, 'e_o_k': [0.593803, 0.475043, 0.380034, 0.304027, 0.243222, 0.194577], 'p_i': 20, 'u_i': 1.0830},
        {'id': 2, 'e_m': 10.739419, 'e_o_k': [1.789903, 1.431923], 'p_i': 40, 'u_i': 1.9156},
        {'id': 3, 'e_m': 19.307401, 'e_o_k': [1.570014, 1.256011, 1.004809, 0.803847, 0.643078, 0.514462], 'p_i': 80, 'u_i': 2.8864},
        {'id': 4, 'e_m': 1.513625, 'e_o_k': [0.135081, 0.108065, 0.086452, 0.069161, 0.055329], 'p_i': 10, 'u_i': 1.3892},
        {'id': 5, 'e_m': 1.499281, 'e_o_k': [0.152366, 0.121893, 0.097514, 0.078011], 'p_i': 10, 'u_i': 2.4866},
        {'id': 6, 'e_m': 13.497252, 'e_o_k': [1.204538, 0.963631, 0.770904, 0.616724, 0.493379], 'p_i': 80, 'u_i': 4.5153},
        {'id': 7, 'e_m': 4.670384, 'e_o_k': [0.416800, 0.333440, 0.266752, 0.213402, 0.170721], 'p_i': 40, 'u_i': 1.1207},
    ]
    B_BUDGET = 191.359998
    return processors, tasks, B_BUDGET
