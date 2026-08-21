"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.622101, 'e_o_k': [0.127480, 0.101984, 0.081587], 'p_i': 10, 'u_i': 2.0434},
        {'id': 1, 'e_m': 1.969373, 'e_o_k': [0.266905, 0.213524, 0.170819, 0.136655, 0.109324, 0.087459], 'p_i': 20, 'u_i': 3.8464},
        {'id': 2, 'e_m': 7.139571, 'e_o_k': [0.967610, 0.774088, 0.619271, 0.495417, 0.396333, 0.317067], 'p_i': 40, 'u_i': 4.9550},
        {'id': 3, 'e_m': 4.866555, 'e_o_k': [0.723845, 0.579076, 0.463261, 0.370609, 0.296487], 'p_i': 80, 'u_i': 4.5167},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
