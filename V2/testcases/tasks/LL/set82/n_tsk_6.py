"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.19999, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.19999, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.130582, 'e_o_k': [0.314051, 0.251241], 'p_i': 10, 'u_i': 4.0095},
        {'id': 1, 'e_m': 0.240545, 'e_o_k': [0.035778, 0.028623, 0.022898, 0.018319, 0.014655], 'p_i': 20, 'u_i': 4.5444},
        {'id': 2, 'e_m': 2.057526, 'e_o_k': [0.571535, 0.457228], 'p_i': 40, 'u_i': 4.8070},
        {'id': 3, 'e_m': 2.770051, 'e_o_k': [0.412014, 0.329611, 0.263689, 0.210951, 0.168761], 'p_i': 80, 'u_i': 3.8434},
        {'id': 4, 'e_m': 5.452928, 'e_o_k': [1.514702, 1.211762], 'p_i': 40, 'u_i': 3.7460},
        {'id': 5, 'e_m': 0.525275, 'e_o_k': [0.088969, 0.071175, 0.056940, 0.045552], 'p_i': 10, 'u_i': 2.3844},
    ]
    B_BUDGET = 55.199990
    return processors, tasks, B_BUDGET
