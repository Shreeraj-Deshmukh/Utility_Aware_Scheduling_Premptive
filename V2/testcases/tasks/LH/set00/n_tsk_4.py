"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319986, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319986, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.322098, 'e_o_k': [0.152757, 0.122205, 0.097764, 0.078211], 'p_i': 10, 'u_i': 1.2518},
        {'id': 1, 'e_m': 1.335603, 'e_o_k': [0.766329, 0.613063, 0.490451], 'p_i': 20, 'u_i': 3.1387},
        {'id': 2, 'e_m': 10.846720, 'e_o_k': [4.517316, 3.613853, 2.891082, 2.312866, 1.850292], 'p_i': 40, 'u_i': 1.5213},
        {'id': 3, 'e_m': 2.387361, 'e_o_k': [1.369797, 1.095838, 0.876670], 'p_i': 80, 'u_i': 2.4569},
    ]
    B_BUDGET = 88.319986
    return processors, tasks, B_BUDGET
