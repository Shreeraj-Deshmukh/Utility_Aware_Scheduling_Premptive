"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.087664, 'e_o_k': [0.761365, 0.761365], 'p_i': 10, 'u_i': 2.8418},
        {'id': 1, 'e_m': 0.391931, 'e_o_k': [0.137176, 0.137176, 0.137176, 0.137176], 'p_i': 20, 'u_i': 1.5566},
        {'id': 2, 'e_m': 13.096144, 'e_o_k': [4.583650, 4.583650, 4.583650, 4.583650], 'p_i': 40, 'u_i': 3.2695},
        {'id': 3, 'e_m': 7.655110, 'e_o_k': [5.358577, 5.358577], 'p_i': 80, 'u_i': 3.8342},
        {'id': 4, 'e_m': 0.303823, 'e_o_k': [0.070892, 0.070892, 0.070892, 0.070892, 0.070892, 0.070892], 'p_i': 20, 'u_i': 4.3734},
        {'id': 5, 'e_m': 0.754717, 'e_o_k': [0.264151, 0.264151, 0.264151, 0.264151], 'p_i': 20, 'u_i': 3.3497},
        {'id': 6, 'e_m': 5.033151, 'e_o_k': [1.761603, 1.761603, 1.761603, 1.761603], 'p_i': 40, 'u_i': 4.2042},
        {'id': 7, 'e_m': 2.791552, 'e_o_k': [1.302724, 1.302724, 1.302724], 'p_i': 40, 'u_i': 1.0373},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
