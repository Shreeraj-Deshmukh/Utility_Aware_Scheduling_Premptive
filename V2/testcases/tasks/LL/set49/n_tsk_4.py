"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.002169, 'e_o_k': [0.000602, 0.000482], 'p_i': 10, 'u_i': 1.9531},
        {'id': 1, 'e_m': 1.447483, 'e_o_k': [0.245170, 0.196136, 0.156909, 0.125527], 'p_i': 20, 'u_i': 4.6020},
        {'id': 2, 'e_m': 1.057846, 'e_o_k': [0.179174, 0.143340, 0.114672, 0.091737], 'p_i': 40, 'u_i': 3.3171},
        {'id': 3, 'e_m': 24.077029, 'e_o_k': [6.688064, 5.350451], 'p_i': 80, 'u_i': 1.0597},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
