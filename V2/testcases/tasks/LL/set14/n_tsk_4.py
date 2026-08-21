"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.792640, 'e_o_k': [0.117896, 0.094317, 0.075454, 0.060363, 0.048290], 'p_i': 10, 'u_i': 3.7039},
        {'id': 1, 'e_m': 3.276966, 'e_o_k': [0.444120, 0.355296, 0.284237, 0.227389, 0.181912, 0.145529], 'p_i': 20, 'u_i': 3.4878},
        {'id': 2, 'e_m': 6.056555, 'e_o_k': [0.900844, 0.720675, 0.576540, 0.461232, 0.368986], 'p_i': 40, 'u_i': 4.7761},
        {'id': 3, 'e_m': 0.437906, 'e_o_k': [0.065134, 0.052107, 0.041685, 0.033348, 0.026679], 'p_i': 80, 'u_i': 2.0030},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
