"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.012700, 'e_o_k': [0.581057, 0.464846, 0.371877], 'p_i': 10, 'u_i': 4.3936},
        {'id': 1, 'e_m': 6.068499, 'e_o_k': [3.481926, 2.785541, 2.228432], 'p_i': 20, 'u_i': 2.8467},
        {'id': 2, 'e_m': 8.216760, 'e_o_k': [3.896837, 3.117470, 2.493976, 1.995181], 'p_i': 40, 'u_i': 2.7697},
        {'id': 3, 'e_m': 15.190882, 'e_o_k': [5.764603, 4.611683, 3.689346, 2.951477, 2.361181, 1.888945], 'p_i': 80, 'u_i': 2.4720},
    ]
    B_BUDGET = 176.639997
    return processors, tasks, B_BUDGET
