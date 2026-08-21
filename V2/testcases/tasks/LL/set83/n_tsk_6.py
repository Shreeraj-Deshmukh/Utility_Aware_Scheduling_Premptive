"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199987, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199987, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.056396, 'e_o_k': [0.293443, 0.234755], 'p_i': 10, 'u_i': 3.4799},
        {'id': 1, 'e_m': 0.992646, 'e_o_k': [0.147645, 0.118116, 0.094493, 0.075594, 0.060475], 'p_i': 20, 'u_i': 2.9893},
        {'id': 2, 'e_m': 0.801879, 'e_o_k': [0.119271, 0.095416, 0.076333, 0.061066, 0.048853], 'p_i': 40, 'u_i': 3.6030},
        {'id': 3, 'e_m': 9.625935, 'e_o_k': [2.673871, 2.139097], 'p_i': 80, 'u_i': 4.7122},
        {'id': 4, 'e_m': 6.603643, 'e_o_k': [1.834345, 1.467476], 'p_i': 80, 'u_i': 2.7870},
        {'id': 5, 'e_m': 0.872453, 'e_o_k': [0.178781, 0.143025, 0.114420], 'p_i': 40, 'u_i': 1.7506},
    ]
    B_BUDGET = 55.199987
    return processors, tasks, B_BUDGET
