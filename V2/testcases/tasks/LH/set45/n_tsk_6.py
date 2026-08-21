"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.066460, 'e_o_k': [0.027678, 0.022143, 0.017714, 0.014171, 0.011337], 'p_i': 10, 'u_i': 4.9998},
        {'id': 1, 'e_m': 0.732917, 'e_o_k': [0.570047, 0.456037], 'p_i': 20, 'u_i': 2.8601},
        {'id': 2, 'e_m': 0.018045, 'e_o_k': [0.008558, 0.006846, 0.005477, 0.004382], 'p_i': 40, 'u_i': 4.7969},
        {'id': 3, 'e_m': 2.107623, 'e_o_k': [0.877758, 0.702207, 0.561765, 0.449412, 0.359530], 'p_i': 80, 'u_i': 4.3760},
        {'id': 4, 'e_m': 7.862420, 'e_o_k': [4.511225, 3.608980, 2.887184], 'p_i': 80, 'u_i': 3.1042},
        {'id': 5, 'e_m': 18.530521, 'e_o_k': [7.031922, 5.625538, 4.500430, 3.600344, 2.880275, 2.304220], 'p_i': 80, 'u_i': 1.7042},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET
