"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.622101, 'e_o_k': [0.356943, 0.285555, 0.228444], 'p_i': 10, 'u_i': 2.0434},
        {'id': 1, 'e_m': 1.969373, 'e_o_k': [0.747333, 0.597867, 0.478293, 0.382635, 0.306108, 0.244886], 'p_i': 20, 'u_i': 3.8464},
        {'id': 2, 'e_m': 7.139571, 'e_o_k': [2.709309, 2.167447, 1.733958, 1.387166, 1.109733, 0.887786], 'p_i': 40, 'u_i': 4.9550},
        {'id': 3, 'e_m': 4.866555, 'e_o_k': [2.026766, 1.621413, 1.297130, 1.037704, 0.830163], 'p_i': 80, 'u_i': 4.5167},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET
