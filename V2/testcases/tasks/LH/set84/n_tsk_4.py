"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.543082, 'e_o_k': [0.226176, 0.180941, 0.144753, 0.115802, 0.092642], 'p_i': 10, 'u_i': 4.6924},
        {'id': 1, 'e_m': 0.967555, 'e_o_k': [0.367166, 0.293733, 0.234986, 0.187989, 0.150391, 0.120313], 'p_i': 20, 'u_i': 3.7468},
        {'id': 2, 'e_m': 6.912441, 'e_o_k': [5.376343, 4.301075], 'p_i': 40, 'u_i': 3.5829},
        {'id': 3, 'e_m': 9.960244, 'e_o_k': [3.779692, 3.023753, 2.419003, 1.935202, 1.548162, 1.238529], 'p_i': 80, 'u_i': 3.3883},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET
