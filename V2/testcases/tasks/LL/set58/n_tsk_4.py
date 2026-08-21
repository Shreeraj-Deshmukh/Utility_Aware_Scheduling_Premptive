"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.317572, 'e_o_k': [0.178568, 0.142854, 0.114283, 0.091427, 0.073141, 0.058513], 'p_i': 10, 'u_i': 3.8653},
        {'id': 1, 'e_m': 3.445268, 'e_o_k': [0.705997, 0.564798, 0.451838], 'p_i': 20, 'u_i': 1.8068},
        {'id': 2, 'e_m': 0.525499, 'e_o_k': [0.145972, 0.116778], 'p_i': 40, 'u_i': 1.4573},
        {'id': 3, 'e_m': 6.627353, 'e_o_k': [0.985744, 0.788595, 0.630876, 0.504701, 0.403761], 'p_i': 80, 'u_i': 1.2598},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET
