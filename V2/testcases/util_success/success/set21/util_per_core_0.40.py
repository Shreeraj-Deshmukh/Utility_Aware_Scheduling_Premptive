"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680008, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680008, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.691442, 'e_o_k': [0.085013, 0.068011, 0.054409], 'p_i': 10, 'u_i': 2.6945},
        {'id': 1, 'e_m': 3.651177, 'e_o_k': [0.296902, 0.237521, 0.190017, 0.152014, 0.121611, 0.097289], 'p_i': 20, 'u_i': 1.0830},
        {'id': 2, 'e_m': 5.369710, 'e_o_k': [0.894952, 0.715961], 'p_i': 40, 'u_i': 1.9156},
        {'id': 3, 'e_m': 9.653701, 'e_o_k': [0.785007, 0.628006, 0.502404, 0.401924, 0.321539, 0.257231], 'p_i': 80, 'u_i': 2.8864},
        {'id': 4, 'e_m': 0.756812, 'e_o_k': [0.067540, 0.054032, 0.043226, 0.034581, 0.027665], 'p_i': 10, 'u_i': 1.3892},
        {'id': 5, 'e_m': 0.749641, 'e_o_k': [0.076183, 0.060946, 0.048757, 0.039006], 'p_i': 10, 'u_i': 2.4866},
        {'id': 6, 'e_m': 6.748626, 'e_o_k': [0.602269, 0.481815, 0.385452, 0.308362, 0.246689], 'p_i': 80, 'u_i': 4.5153},
        {'id': 7, 'e_m': 2.335192, 'e_o_k': [0.208400, 0.166720, 0.133376, 0.106701, 0.085361], 'p_i': 40, 'u_i': 1.1207},
    ]
    B_BUDGET = 95.680008
    return processors, tasks, B_BUDGET
