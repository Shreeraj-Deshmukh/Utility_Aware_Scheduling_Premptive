"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.152761, 'e_o_k': [0.031303, 0.025043, 0.020034], 'p_i': 10, 'u_i': 2.4499},
        {'id': 1, 'e_m': 0.833685, 'e_o_k': [0.231579, 0.185263], 'p_i': 20, 'u_i': 1.6318},
        {'id': 2, 'e_m': 7.711193, 'e_o_k': [1.306096, 1.044877, 0.835902, 0.668721], 'p_i': 40, 'u_i': 3.2685},
        {'id': 3, 'e_m': 4.546245, 'e_o_k': [0.931608, 0.745286, 0.596229], 'p_i': 80, 'u_i': 2.9234},
        {'id': 4, 'e_m': 5.731149, 'e_o_k': [1.174416, 0.939533, 0.751626], 'p_i': 80, 'u_i': 3.7707},
        {'id': 5, 'e_m': 0.435849, 'e_o_k': [0.089313, 0.071451, 0.057161], 'p_i': 20, 'u_i': 1.9627},
    ]
    B_BUDGET = 55.200002
    return processors, tasks, B_BUDGET
