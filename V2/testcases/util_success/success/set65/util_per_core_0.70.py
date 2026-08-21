"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440002, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440002, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.223663, 'e_o_k': [0.022730, 0.018184, 0.014547, 0.011638], 'p_i': 10, 'u_i': 3.7146},
        {'id': 1, 'e_m': 8.117002, 'e_o_k': [0.997992, 0.798394, 0.638715], 'p_i': 20, 'u_i': 2.7971},
        {'id': 2, 'e_m': 1.401383, 'e_o_k': [0.172301, 0.137841, 0.110273], 'p_i': 40, 'u_i': 1.6396},
        {'id': 3, 'e_m': 16.516256, 'e_o_k': [2.030687, 1.624550, 1.299640], 'p_i': 80, 'u_i': 4.1445},
        {'id': 4, 'e_m': 6.095476, 'e_o_k': [0.619459, 0.495567, 0.396454, 0.317163], 'p_i': 20, 'u_i': 4.6205},
        {'id': 5, 'e_m': 25.416364, 'e_o_k': [2.066774, 1.653419, 1.322736, 1.058188, 0.846551, 0.677241], 'p_i': 80, 'u_i': 1.3665},
        {'id': 6, 'e_m': 0.128372, 'e_o_k': [0.013046, 0.010437, 0.008349, 0.006680], 'p_i': 20, 'u_i': 3.3652},
        {'id': 7, 'e_m': 2.027977, 'e_o_k': [0.180983, 0.144787, 0.115829, 0.092663, 0.074131], 'p_i': 20, 'u_i': 2.1692},
    ]
    B_BUDGET = 167.440002
    return processors, tasks, B_BUDGET
