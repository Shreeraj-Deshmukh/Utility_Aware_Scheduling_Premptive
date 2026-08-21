"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639991, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639991, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.978192, 'e_o_k': [0.371202, 0.296962, 0.237569, 0.190056, 0.152044, 0.121636], 'p_i': 10, 'u_i': 1.1924},
        {'id': 1, 'e_m': 2.729673, 'e_o_k': [1.566206, 1.252965, 1.002372], 'p_i': 20, 'u_i': 4.9854},
        {'id': 2, 'e_m': 8.948325, 'e_o_k': [6.959808, 5.567846], 'p_i': 40, 'u_i': 2.6844},
        {'id': 3, 'e_m': 17.481868, 'e_o_k': [6.633981, 5.307185, 4.245748, 3.396599, 2.717279, 2.173823], 'p_i': 80, 'u_i': 3.2251},
        {'id': 4, 'e_m': 0.637135, 'e_o_k': [0.365569, 0.292455, 0.233964], 'p_i': 10, 'u_i': 4.0273},
        {'id': 5, 'e_m': 4.780173, 'e_o_k': [2.742722, 2.194178, 1.755342], 'p_i': 80, 'u_i': 2.2476},
    ]
    B_BUDGET = 176.639991
    return processors, tasks, B_BUDGET
