"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.260836, 'e_o_k': [0.980650, 0.784520], 'p_i': 10, 'u_i': 3.1727},
        {'id': 1, 'e_m': 5.166643, 'e_o_k': [4.018500, 3.214800], 'p_i': 20, 'u_i': 2.8789},
        {'id': 2, 'e_m': 0.082920, 'e_o_k': [0.047577, 0.038062, 0.030449], 'p_i': 40, 'u_i': 1.7162},
        {'id': 3, 'e_m': 1.080901, 'e_o_k': [0.840701, 0.672561], 'p_i': 80, 'u_i': 1.4626},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
