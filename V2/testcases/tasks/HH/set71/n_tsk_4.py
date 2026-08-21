"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.145960, 'e_o_k': [3.224636, 2.579709], 'p_i': 10, 'u_i': 3.4158},
        {'id': 1, 'e_m': 0.792926, 'e_o_k': [0.616721, 0.493376], 'p_i': 20, 'u_i': 2.7668},
        {'id': 2, 'e_m': 2.834056, 'e_o_k': [1.626098, 1.300878, 1.040703], 'p_i': 40, 'u_i': 2.4237},
        {'id': 3, 'e_m': 21.992501, 'e_o_k': [8.345667, 6.676533, 5.341227, 4.272981, 3.418385, 2.734708], 'p_i': 80, 'u_i': 3.6832},
    ]
    B_BUDGET = 176.640005
    return processors, tasks, B_BUDGET
