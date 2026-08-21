"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.981043, 'e_o_k': [0.272512, 0.218010], 'p_i': 10, 'u_i': 2.4321},
        {'id': 1, 'e_m': 3.868647, 'e_o_k': [0.524309, 0.419447, 0.335558, 0.268446, 0.214757, 0.171806], 'p_i': 20, 'u_i': 1.0700},
        {'id': 2, 'e_m': 0.569018, 'e_o_k': [0.116602, 0.093282, 0.074625], 'p_i': 40, 'u_i': 3.1686},
        {'id': 3, 'e_m': 4.740604, 'e_o_k': [0.971435, 0.777148, 0.621719], 'p_i': 80, 'u_i': 1.4833},
        {'id': 4, 'e_m': 0.098523, 'e_o_k': [0.013353, 0.010682, 0.008546, 0.006837, 0.005469, 0.004375], 'p_i': 20, 'u_i': 1.9048},
        {'id': 5, 'e_m': 1.202166, 'e_o_k': [0.333935, 0.267148], 'p_i': 40, 'u_i': 4.4078},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
