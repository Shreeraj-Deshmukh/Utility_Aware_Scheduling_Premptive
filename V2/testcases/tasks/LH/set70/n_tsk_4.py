"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.32001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.187791, 'e_o_k': [0.563316, 0.450652, 0.360522, 0.288418], 'p_i': 10, 'u_i': 4.7862},
        {'id': 1, 'e_m': 3.936347, 'e_o_k': [2.258560, 1.806848, 1.445478], 'p_i': 20, 'u_i': 1.7928},
        {'id': 2, 'e_m': 3.328741, 'e_o_k': [2.589021, 2.071216], 'p_i': 40, 'u_i': 1.8882},
        {'id': 3, 'e_m': 0.094804, 'e_o_k': [0.039483, 0.031586, 0.025269, 0.020215, 0.016172], 'p_i': 80, 'u_i': 2.0463},
    ]
    B_BUDGET = 88.320010
    return processors, tasks, B_BUDGET
