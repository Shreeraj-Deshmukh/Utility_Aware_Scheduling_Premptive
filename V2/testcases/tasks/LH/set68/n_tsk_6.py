"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319991, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319991, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.635917, 'e_o_k': [0.301586, 0.241269, 0.193015, 0.154412], 'p_i': 10, 'u_i': 4.9351},
        {'id': 1, 'e_m': 2.189877, 'e_o_k': [0.912014, 0.729612, 0.583689, 0.466951, 0.373561], 'p_i': 20, 'u_i': 4.9277},
        {'id': 2, 'e_m': 1.848218, 'e_o_k': [0.876526, 0.701221, 0.560977, 0.448781], 'p_i': 40, 'u_i': 1.3099},
        {'id': 3, 'e_m': 5.611671, 'e_o_k': [2.661362, 2.129089, 1.703271, 1.362617], 'p_i': 80, 'u_i': 1.1502},
        {'id': 4, 'e_m': 0.302424, 'e_o_k': [0.173522, 0.138818, 0.111054], 'p_i': 10, 'u_i': 2.1747},
        {'id': 5, 'e_m': 1.606415, 'e_o_k': [1.249434, 0.999547], 'p_i': 20, 'u_i': 4.4262},
    ]
    B_BUDGET = 88.319991
    return processors, tasks, B_BUDGET
