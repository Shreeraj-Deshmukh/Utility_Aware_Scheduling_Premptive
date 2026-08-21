"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319984, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319984, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.162586, 'e_o_k': [0.441175, 0.352940, 0.282352, 0.225882, 0.180705, 0.144564], 'p_i': 10, 'u_i': 2.0153},
        {'id': 1, 'e_m': 4.654398, 'e_o_k': [1.938409, 1.550727, 1.240582, 0.992466, 0.793972], 'p_i': 20, 'u_i': 4.1190},
        {'id': 2, 'e_m': 0.750044, 'e_o_k': [0.430353, 0.344282, 0.275426], 'p_i': 40, 'u_i': 4.7975},
        {'id': 3, 'e_m': 2.581637, 'e_o_k': [0.979674, 0.783739, 0.626991, 0.501593, 0.401274, 0.321020], 'p_i': 80, 'u_i': 4.0424},
    ]
    B_BUDGET = 88.319984
    return processors, tasks, B_BUDGET
