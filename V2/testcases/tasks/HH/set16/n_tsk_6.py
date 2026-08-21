"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639983, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639983, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.461036, 'e_o_k': [0.608475, 0.486780, 0.389424, 0.311539, 0.249232], 'p_i': 10, 'u_i': 1.1399},
        {'id': 1, 'e_m': 2.740078, 'e_o_k': [1.039799, 0.831839, 0.665471, 0.532377, 0.425902, 0.340721], 'p_i': 20, 'u_i': 4.6324},
        {'id': 2, 'e_m': 6.123017, 'e_o_k': [2.550043, 2.040034, 1.632027, 1.305622, 1.044498], 'p_i': 40, 'u_i': 3.3557},
        {'id': 3, 'e_m': 7.319613, 'e_o_k': [3.048387, 2.438710, 1.950968, 1.560774, 1.248619], 'p_i': 80, 'u_i': 3.4396},
        {'id': 4, 'e_m': 0.971590, 'e_o_k': [0.368697, 0.294957, 0.235966, 0.188773, 0.151018, 0.120815], 'p_i': 10, 'u_i': 2.9972},
        {'id': 5, 'e_m': 7.006514, 'e_o_k': [5.449511, 4.359609], 'p_i': 40, 'u_i': 3.3467},
    ]
    B_BUDGET = 176.639983
    return processors, tasks, B_BUDGET
