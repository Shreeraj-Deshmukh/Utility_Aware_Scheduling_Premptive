"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.950399, 'e_o_k': [0.739199, 0.591359], 'p_i': 10, 'u_i': 1.8275},
        {'id': 1, 'e_m': 1.993422, 'e_o_k': [1.550439, 1.240351], 'p_i': 20, 'u_i': 3.9821},
        {'id': 2, 'e_m': 8.136855, 'e_o_k': [3.087756, 2.470205, 1.976164, 1.580931, 1.264745, 1.011796], 'p_i': 40, 'u_i': 4.4924},
        {'id': 3, 'e_m': 0.149413, 'e_o_k': [0.085729, 0.068583, 0.054866], 'p_i': 80, 'u_i': 4.2054},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
