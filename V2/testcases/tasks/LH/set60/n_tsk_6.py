"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.981043, 'e_o_k': [0.763034, 0.610427], 'p_i': 10, 'u_i': 2.4321},
        {'id': 1, 'e_m': 3.868647, 'e_o_k': [1.468066, 1.174453, 0.939562, 0.751650, 0.601320, 0.481056], 'p_i': 20, 'u_i': 1.0700},
        {'id': 2, 'e_m': 0.569018, 'e_o_k': [0.326486, 0.261188, 0.208951], 'p_i': 40, 'u_i': 3.1686},
        {'id': 3, 'e_m': 4.740604, 'e_o_k': [2.720019, 2.176015, 1.740812], 'p_i': 80, 'u_i': 1.4833},
        {'id': 4, 'e_m': 0.098523, 'e_o_k': [0.037387, 0.029910, 0.023928, 0.019142, 0.015314, 0.012251], 'p_i': 20, 'u_i': 1.9048},
        {'id': 5, 'e_m': 1.202166, 'e_o_k': [0.935018, 0.748015], 'p_i': 40, 'u_i': 4.4078},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET
