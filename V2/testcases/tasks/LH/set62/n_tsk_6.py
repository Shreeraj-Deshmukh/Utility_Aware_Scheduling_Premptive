"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32001, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.32001, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.399738, 'e_o_k': [1.088685, 0.870948], 'p_i': 10, 'u_i': 4.3165},
        {'id': 1, 'e_m': 1.192176, 'e_o_k': [0.927248, 0.741798], 'p_i': 20, 'u_i': 4.1600},
        {'id': 2, 'e_m': 0.850246, 'e_o_k': [0.354101, 0.283281, 0.226624, 0.181300, 0.145040], 'p_i': 40, 'u_i': 2.4258},
        {'id': 3, 'e_m': 1.297044, 'e_o_k': [0.615129, 0.492104, 0.393683, 0.314946], 'p_i': 80, 'u_i': 2.6711},
        {'id': 4, 'e_m': 12.521523, 'e_o_k': [4.751640, 3.801312, 3.041050, 2.432840, 1.946272, 1.557018], 'p_i': 80, 'u_i': 3.0914},
        {'id': 5, 'e_m': 0.064292, 'e_o_k': [0.030491, 0.024393, 0.019514, 0.015611], 'p_i': 10, 'u_i': 2.6989},
    ]
    B_BUDGET = 88.320010
    return processors, tasks, B_BUDGET
