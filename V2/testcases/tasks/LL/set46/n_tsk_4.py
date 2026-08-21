"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.909710, 'e_o_k': [0.154084, 0.123267, 0.098614, 0.078891], 'p_i': 10, 'u_i': 4.4662},
        {'id': 1, 'e_m': 0.625153, 'e_o_k': [0.128105, 0.102484, 0.081987], 'p_i': 20, 'u_i': 4.4739},
        {'id': 2, 'e_m': 10.123619, 'e_o_k': [2.812116, 2.249693], 'p_i': 40, 'u_i': 4.4595},
        {'id': 3, 'e_m': 1.974466, 'e_o_k': [0.404604, 0.323683, 0.258946], 'p_i': 80, 'u_i': 4.0510},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
