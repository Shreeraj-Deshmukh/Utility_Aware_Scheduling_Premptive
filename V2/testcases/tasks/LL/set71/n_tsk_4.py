"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.072980, 'e_o_k': [0.575828, 0.460662], 'p_i': 10, 'u_i': 3.4158},
        {'id': 1, 'e_m': 0.396463, 'e_o_k': [0.110129, 0.088103], 'p_i': 20, 'u_i': 2.7668},
        {'id': 2, 'e_m': 1.417028, 'e_o_k': [0.290375, 0.232300, 0.185840], 'p_i': 40, 'u_i': 2.4237},
        {'id': 3, 'e_m': 10.996250, 'e_o_k': [1.490298, 1.192238, 0.953790, 0.763032, 0.610426, 0.488341], 'p_i': 80, 'u_i': 3.6832},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
