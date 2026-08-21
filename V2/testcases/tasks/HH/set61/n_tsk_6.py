"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640018, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640018, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.943519, 'e_o_k': [0.447468, 0.357975, 0.286380, 0.229104], 'p_i': 10, 'u_i': 2.3827},
        {'id': 1, 'e_m': 3.438081, 'e_o_k': [1.431852, 1.145482, 0.916385, 0.733108, 0.586487], 'p_i': 20, 'u_i': 2.9856},
        {'id': 2, 'e_m': 0.070381, 'e_o_k': [0.026708, 0.021366, 0.017093, 0.013674, 0.010940, 0.008752], 'p_i': 40, 'u_i': 4.8236},
        {'id': 3, 'e_m': 17.556587, 'e_o_k': [8.326295, 6.661036, 5.328829, 4.263063], 'p_i': 80, 'u_i': 2.2531},
        {'id': 4, 'e_m': 22.420817, 'e_o_k': [9.337561, 7.470049, 5.976039, 4.780831, 3.824665], 'p_i': 80, 'u_i': 4.0598},
        {'id': 5, 'e_m': 0.645340, 'e_o_k': [0.306056, 0.244845, 0.195876, 0.156700], 'p_i': 20, 'u_i': 4.5014},
    ]
    B_BUDGET = 176.640018
    return processors, tasks, B_BUDGET
