"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.31999, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.31999, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.503086, 'e_o_k': [0.712846, 0.570277, 0.456221, 0.364977], 'p_i': 10, 'u_i': 1.9112},
        {'id': 1, 'e_m': 0.915545, 'e_o_k': [0.381295, 0.305036, 0.244029, 0.195223, 0.156179], 'p_i': 20, 'u_i': 4.0850},
        {'id': 2, 'e_m': 0.749753, 'e_o_k': [0.355574, 0.284459, 0.227567, 0.182054], 'p_i': 40, 'u_i': 1.7025},
        {'id': 3, 'e_m': 11.481254, 'e_o_k': [4.781579, 3.825263, 3.060211, 2.448168, 1.958535], 'p_i': 80, 'u_i': 2.0058},
        {'id': 4, 'e_m': 0.208788, 'e_o_k': [0.162391, 0.129913], 'p_i': 10, 'u_i': 3.5722},
        {'id': 5, 'e_m': 1.662061, 'e_o_k': [0.788241, 0.630592, 0.504474, 0.403579], 'p_i': 80, 'u_i': 1.2384},
    ]
    B_BUDGET = 88.319990
    return processors, tasks, B_BUDGET
