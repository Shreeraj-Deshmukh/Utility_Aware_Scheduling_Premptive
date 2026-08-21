"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.171934, 'e_o_k': [1.246191, 0.996953, 0.797562], 'p_i': 10, 'u_i': 1.7419},
        {'id': 1, 'e_m': 6.026758, 'e_o_k': [2.858219, 2.286575, 1.829260, 1.463408], 'p_i': 20, 'u_i': 1.0689},
        {'id': 2, 'e_m': 6.980869, 'e_o_k': [5.429565, 4.343652], 'p_i': 40, 'u_i': 2.1386},
        {'id': 3, 'e_m': 8.555761, 'e_o_k': [3.563204, 2.850563, 2.280450, 1.824360, 1.459488], 'p_i': 80, 'u_i': 3.8785},
    ]
    B_BUDGET = 176.639998
    return processors, tasks, B_BUDGET
