"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.375582, 'e_o_k': [0.402368, 0.321895, 0.257516, 0.206013], 'p_i': 10, 'u_i': 4.7862},
        {'id': 1, 'e_m': 7.872693, 'e_o_k': [1.613257, 1.290605, 1.032484], 'p_i': 20, 'u_i': 1.7928},
        {'id': 2, 'e_m': 6.657481, 'e_o_k': [1.849300, 1.479440], 'p_i': 40, 'u_i': 1.8882},
        {'id': 3, 'e_m': 0.189608, 'e_o_k': [0.028202, 0.022562, 0.018049, 0.014439, 0.011552], 'p_i': 80, 'u_i': 2.0463},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET
