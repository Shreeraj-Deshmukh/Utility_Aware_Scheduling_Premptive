"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.730518, 'e_o_k': [0.108656, 0.086925, 0.069540, 0.055632, 0.044506], 'p_i': 10, 'u_i': 1.1399},
        {'id': 1, 'e_m': 1.370039, 'e_o_k': [0.185678, 0.148543, 0.118834, 0.095067, 0.076054, 0.060843], 'p_i': 20, 'u_i': 4.6324},
        {'id': 2, 'e_m': 3.061509, 'e_o_k': [0.455365, 0.364292, 0.291433, 0.233147, 0.186517], 'p_i': 40, 'u_i': 3.3557},
        {'id': 3, 'e_m': 3.659807, 'e_o_k': [0.544355, 0.435484, 0.348387, 0.278710, 0.222968], 'p_i': 80, 'u_i': 3.4396},
        {'id': 4, 'e_m': 0.485795, 'e_o_k': [0.065839, 0.052671, 0.042137, 0.033709, 0.026968, 0.021574], 'p_i': 10, 'u_i': 2.9972},
        {'id': 5, 'e_m': 3.503257, 'e_o_k': [0.973127, 0.778502], 'p_i': 40, 'u_i': 3.3467},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
