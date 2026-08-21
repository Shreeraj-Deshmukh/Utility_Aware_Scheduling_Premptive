"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.571521, 'e_o_k': [0.216880, 0.173504, 0.138803, 0.111042, 0.088834, 0.071067], 'p_i': 10, 'u_i': 2.5404},
        {'id': 1, 'e_m': 1.425904, 'e_o_k': [0.818142, 0.654513, 0.523611], 'p_i': 20, 'u_i': 1.0986},
        {'id': 2, 'e_m': 1.552851, 'e_o_k': [1.207773, 0.966218], 'p_i': 40, 'u_i': 3.7025},
        {'id': 3, 'e_m': 9.264581, 'e_o_k': [7.205785, 5.764628], 'p_i': 80, 'u_i': 4.4926},
        {'id': 4, 'e_m': 0.961546, 'e_o_k': [0.551707, 0.441365, 0.353092], 'p_i': 80, 'u_i': 3.2922},
        {'id': 5, 'e_m': 4.196193, 'e_o_k': [3.263705, 2.610964], 'p_i': 40, 'u_i': 3.7450},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
