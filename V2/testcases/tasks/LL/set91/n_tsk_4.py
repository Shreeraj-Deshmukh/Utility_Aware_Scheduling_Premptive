"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200012, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200012, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.155705, 'e_o_k': [0.195749, 0.156600, 0.125280, 0.100224], 'p_i': 10, 'u_i': 4.8210},
        {'id': 1, 'e_m': 0.470230, 'e_o_k': [0.130620, 0.104496], 'p_i': 20, 'u_i': 2.4270},
        {'id': 2, 'e_m': 10.067610, 'e_o_k': [1.364441, 1.091553, 0.873242, 0.698594, 0.558875, 0.447100], 'p_i': 40, 'u_i': 3.3094},
        {'id': 3, 'e_m': 0.738221, 'e_o_k': [0.151275, 0.121020, 0.096816], 'p_i': 80, 'u_i': 3.8452},
    ]
    B_BUDGET = 55.200012
    return processors, tasks, B_BUDGET
