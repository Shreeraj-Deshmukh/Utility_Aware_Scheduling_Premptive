"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.613895, 'e_o_k': [2.033030, 1.626424], 'p_i': 10, 'u_i': 2.6714},
        {'id': 1, 'e_m': 0.628503, 'e_o_k': [0.298070, 0.238456, 0.190765, 0.152612], 'p_i': 20, 'u_i': 1.4256},
        {'id': 2, 'e_m': 3.259886, 'e_o_k': [2.535467, 2.028374], 'p_i': 40, 'u_i': 3.1325},
        {'id': 3, 'e_m': 2.055056, 'e_o_k': [1.598377, 1.278702], 'p_i': 80, 'u_i': 4.7073},
    ]
    B_BUDGET = 88.320006
    return processors, tasks, B_BUDGET
