"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639977, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639977, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.471954, 'e_o_k': [0.613022, 0.490418, 0.392334, 0.313867, 0.251094], 'p_i': 10, 'u_i': 1.2401},
        {'id': 1, 'e_m': 2.545723, 'e_o_k': [1.060213, 0.848170, 0.678536, 0.542829, 0.434263], 'p_i': 20, 'u_i': 2.2762},
        {'id': 2, 'e_m': 13.299632, 'e_o_k': [5.538876, 4.431100, 3.544880, 2.835904, 2.268723], 'p_i': 40, 'u_i': 1.0661},
        {'id': 3, 'e_m': 15.442209, 'e_o_k': [7.323541, 5.858833, 4.687066, 3.749653], 'p_i': 80, 'u_i': 2.9903},
    ]
    B_BUDGET = 176.639977
    return processors, tasks, B_BUDGET
