"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32001, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.32001, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.152761, 'e_o_k': [0.087649, 0.070120, 0.056096], 'p_i': 10, 'u_i': 2.4499},
        {'id': 1, 'e_m': 0.833685, 'e_o_k': [0.648422, 0.518737], 'p_i': 20, 'u_i': 1.6318},
        {'id': 2, 'e_m': 7.711193, 'e_o_k': [3.657070, 2.925656, 2.340525, 1.872420], 'p_i': 40, 'u_i': 3.2685},
        {'id': 3, 'e_m': 4.546245, 'e_o_k': [2.608501, 2.086801, 1.669441], 'p_i': 80, 'u_i': 2.9234},
        {'id': 4, 'e_m': 5.731149, 'e_o_k': [3.288364, 2.630691, 2.104553], 'p_i': 80, 'u_i': 3.7707},
        {'id': 5, 'e_m': 0.435849, 'e_o_k': [0.250077, 0.200062, 0.160050], 'p_i': 20, 'u_i': 1.9627},
    ]
    B_BUDGET = 88.320010
    return processors, tasks, B_BUDGET
