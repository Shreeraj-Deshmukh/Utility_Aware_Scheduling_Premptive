"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.244203, 'e_o_k': [0.713887, 0.571109, 0.456888], 'p_i': 10, 'u_i': 2.0434},
        {'id': 1, 'e_m': 3.938746, 'e_o_k': [1.494667, 1.195733, 0.956587, 0.765269, 0.612216, 0.489772], 'p_i': 20, 'u_i': 3.8464},
        {'id': 2, 'e_m': 14.279143, 'e_o_k': [5.418618, 4.334895, 3.467916, 2.774333, 2.219466, 1.775573], 'p_i': 40, 'u_i': 4.9550},
        {'id': 3, 'e_m': 9.733109, 'e_o_k': [4.053532, 3.242825, 2.594260, 2.075408, 1.660327], 'p_i': 80, 'u_i': 4.5167},
    ]
    B_BUDGET = 176.640006
    return processors, tasks, B_BUDGET
