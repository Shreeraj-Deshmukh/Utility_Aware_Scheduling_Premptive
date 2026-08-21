"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639994, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639994, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.660725, 'e_o_k': [1.526645, 1.221316, 0.977053], 'p_i': 10, 'u_i': 2.7301},
        {'id': 1, 'e_m': 0.191668, 'e_o_k': [0.090900, 0.072720, 0.058176, 0.046541], 'p_i': 20, 'u_i': 2.9329},
        {'id': 2, 'e_m': 6.038206, 'e_o_k': [2.863648, 2.290918, 1.832735, 1.466188], 'p_i': 40, 'u_i': 4.3550},
        {'id': 3, 'e_m': 2.896544, 'e_o_k': [1.206319, 0.965055, 0.772044, 0.617635, 0.494108], 'p_i': 80, 'u_i': 2.2741},
        {'id': 4, 'e_m': 1.536590, 'e_o_k': [0.881650, 0.705320, 0.564256], 'p_i': 10, 'u_i': 2.5808},
        {'id': 5, 'e_m': 7.340925, 'e_o_k': [3.057263, 2.445810, 1.956648, 1.565319, 1.252255], 'p_i': 40, 'u_i': 4.5356},
    ]
    B_BUDGET = 176.639994
    return processors, tasks, B_BUDGET
