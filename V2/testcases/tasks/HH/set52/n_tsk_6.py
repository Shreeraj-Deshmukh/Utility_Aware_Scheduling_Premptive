"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639998, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639998, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.101224, 'e_o_k': [0.042156, 0.033725, 0.026980, 0.021584, 0.017267], 'p_i': 10, 'u_i': 1.6984},
        {'id': 1, 'e_m': 1.684546, 'e_o_k': [0.798904, 0.639123, 0.511298, 0.409039], 'p_i': 20, 'u_i': 3.4597},
        {'id': 2, 'e_m': 14.212239, 'e_o_k': [6.740222, 5.392177, 4.313742, 3.450994], 'p_i': 40, 'u_i': 4.7133},
        {'id': 3, 'e_m': 18.089584, 'e_o_k': [6.864596, 5.491677, 4.393342, 3.514673, 2.811739, 2.249391], 'p_i': 80, 'u_i': 2.1441},
        {'id': 4, 'e_m': 2.706115, 'e_o_k': [1.127011, 0.901609, 0.721287, 0.577030, 0.461624], 'p_i': 40, 'u_i': 1.5180},
        {'id': 5, 'e_m': 0.565717, 'e_o_k': [0.268294, 0.214635, 0.171708, 0.137367], 'p_i': 10, 'u_i': 2.4726},
    ]
    B_BUDGET = 176.639998
    return processors, tasks, B_BUDGET
