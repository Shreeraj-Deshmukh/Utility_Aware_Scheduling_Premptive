"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.754933, 'e_o_k': [0.358030, 0.286424, 0.229140, 0.183312], 'p_i': 10, 'u_i': 3.2224},
        {'id': 1, 'e_m': 2.776976, 'e_o_k': [2.159871, 1.727896], 'p_i': 20, 'u_i': 2.5978},
        {'id': 2, 'e_m': 0.073202, 'e_o_k': [0.042001, 0.033601, 0.026881], 'p_i': 40, 'u_i': 4.5124},
        {'id': 3, 'e_m': 14.706228, 'e_o_k': [6.974498, 5.579599, 4.463679, 3.570943], 'p_i': 80, 'u_i': 4.6729},
    ]
    B_BUDGET = 88.320001
    return processors, tasks, B_BUDGET
