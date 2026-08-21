"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.171449, 'e_o_k': [1.029820, 0.823856, 0.659085, 0.527268], 'p_i': 10, 'u_i': 1.8534},
        {'id': 1, 'e_m': 3.039270, 'e_o_k': [1.441388, 1.153111, 0.922489, 0.737991], 'p_i': 20, 'u_i': 3.8693},
        {'id': 2, 'e_m': 3.765803, 'e_o_k': [2.928958, 2.343166], 'p_i': 40, 'u_i': 4.5509},
        {'id': 3, 'e_m': 26.939719, 'e_o_k': [20.953115, 16.762492], 'p_i': 80, 'u_i': 1.7636},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET
