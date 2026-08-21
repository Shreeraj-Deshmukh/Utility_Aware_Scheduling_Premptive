"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.172080, 'e_o_k': [0.911618, 0.729294], 'p_i': 10, 'u_i': 3.4053},
        {'id': 1, 'e_m': 2.847079, 'e_o_k': [1.350241, 1.080192, 0.864154, 0.691323], 'p_i': 20, 'u_i': 3.7246},
        {'id': 2, 'e_m': 2.581376, 'e_o_k': [1.224230, 0.979384, 0.783507, 0.626806], 'p_i': 40, 'u_i': 3.7938},
        {'id': 3, 'e_m': 1.215373, 'e_o_k': [0.461207, 0.368966, 0.295173, 0.236138, 0.188910, 0.151128], 'p_i': 80, 'u_i': 1.4474},
        {'id': 4, 'e_m': 1.244808, 'e_o_k': [0.518423, 0.414739, 0.331791, 0.265433, 0.212346], 'p_i': 10, 'u_i': 3.1824},
        {'id': 5, 'e_m': 26.898454, 'e_o_k': [10.207367, 8.165894, 6.532715, 5.226172, 4.180938, 3.344750], 'p_i': 80, 'u_i': 3.3367},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
