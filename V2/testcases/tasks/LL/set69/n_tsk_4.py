"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.066996, 'e_o_k': [0.009080, 0.007264, 0.005811, 0.004649, 0.003719, 0.002975], 'p_i': 10, 'u_i': 3.0227},
        {'id': 1, 'e_m': 1.196503, 'e_o_k': [0.332362, 0.265890], 'p_i': 20, 'u_i': 1.4869},
        {'id': 2, 'e_m': 1.568472, 'e_o_k': [0.321408, 0.257127, 0.205701], 'p_i': 40, 'u_i': 4.8069},
        {'id': 3, 'e_m': 23.541076, 'e_o_k': [3.501469, 2.801175, 2.240940, 1.792752, 1.434202], 'p_i': 80, 'u_i': 1.7670},
    ]
    B_BUDGET = 55.200002
    return processors, tasks, B_BUDGET
