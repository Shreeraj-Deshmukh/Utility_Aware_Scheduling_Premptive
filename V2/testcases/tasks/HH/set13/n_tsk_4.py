"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.260305, 'e_o_k': [0.149355, 0.119484, 0.095587], 'p_i': 10, 'u_i': 3.2721},
        {'id': 1, 'e_m': 1.935309, 'e_o_k': [1.505240, 1.204192], 'p_i': 20, 'u_i': 2.5377},
        {'id': 2, 'e_m': 8.445409, 'e_o_k': [6.568651, 5.254921], 'p_i': 40, 'u_i': 2.5387},
        {'id': 3, 'e_m': 37.285509, 'e_o_k': [17.682829, 14.146264, 11.317011, 9.053609], 'p_i': 80, 'u_i': 1.0056},
    ]
    B_BUDGET = 176.639995
    return processors, tasks, B_BUDGET
