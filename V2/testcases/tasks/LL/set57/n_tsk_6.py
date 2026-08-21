"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.140327, 'e_o_k': [0.038980, 0.031184], 'p_i': 10, 'u_i': 2.3979},
        {'id': 1, 'e_m': 1.045262, 'e_o_k': [0.290351, 0.232280], 'p_i': 20, 'u_i': 4.6396},
        {'id': 2, 'e_m': 6.086089, 'e_o_k': [0.905237, 0.724190, 0.579352, 0.463481, 0.370785], 'p_i': 40, 'u_i': 4.1139},
        {'id': 3, 'e_m': 5.835122, 'e_o_k': [0.790821, 0.632657, 0.506126, 0.404900, 0.323920, 0.259136], 'p_i': 80, 'u_i': 3.3967},
        {'id': 4, 'e_m': 6.759010, 'e_o_k': [1.877503, 1.502002], 'p_i': 80, 'u_i': 1.9449},
        {'id': 5, 'e_m': 0.965011, 'e_o_k': [0.268059, 0.214447], 'p_i': 40, 'u_i': 4.6056},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
