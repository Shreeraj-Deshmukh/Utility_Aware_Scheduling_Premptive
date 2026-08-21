"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639991, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639991, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.325064, 'e_o_k': [0.502833, 0.402266, 0.321813, 0.257450, 0.205960, 0.164768], 'p_i': 10, 'u_i': 3.4980},
        {'id': 1, 'e_m': 3.938877, 'e_o_k': [3.063571, 2.450857], 'p_i': 20, 'u_i': 2.1751},
        {'id': 2, 'e_m': 1.537214, 'e_o_k': [0.640201, 0.512161, 0.409729, 0.327783, 0.262226], 'p_i': 40, 'u_i': 4.1688},
        {'id': 3, 'e_m': 5.703460, 'e_o_k': [3.272477, 2.617982, 2.094385], 'p_i': 80, 'u_i': 2.2140},
        {'id': 4, 'e_m': 1.856926, 'e_o_k': [1.065449, 0.852359, 0.681888], 'p_i': 10, 'u_i': 3.2266},
        {'id': 5, 'e_m': 1.751335, 'e_o_k': [0.664593, 0.531674, 0.425339, 0.340272, 0.272217, 0.217774], 'p_i': 10, 'u_i': 3.3398},
    ]
    B_BUDGET = 176.639991
    return processors, tasks, B_BUDGET
