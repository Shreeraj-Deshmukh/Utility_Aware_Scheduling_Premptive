"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.293027, 'e_o_k': [0.049632, 0.039706, 0.031764, 0.025412], 'p_i': 10, 'u_i': 1.2737},
        {'id': 1, 'e_m': 0.748915, 'e_o_k': [0.111393, 0.089114, 0.071291, 0.057033, 0.045626], 'p_i': 20, 'u_i': 1.7815},
        {'id': 2, 'e_m': 1.607964, 'e_o_k': [0.272352, 0.217881, 0.174305, 0.139444], 'p_i': 40, 'u_i': 4.6156},
        {'id': 3, 'e_m': 23.444197, 'e_o_k': [3.970901, 3.176720, 2.541376, 2.033101], 'p_i': 80, 'u_i': 1.3815},
    ]
    B_BUDGET = 55.200003
    return processors, tasks, B_BUDGET
