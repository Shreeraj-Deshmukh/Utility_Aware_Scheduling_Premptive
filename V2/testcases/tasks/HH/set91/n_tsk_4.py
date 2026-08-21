"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.818069, 'e_o_k': [1.336483, 1.069186, 0.855349, 0.684279], 'p_i': 10, 'u_i': 3.6437},
        {'id': 1, 'e_m': 0.935497, 'e_o_k': [0.355000, 0.284000, 0.227200, 0.181760, 0.145408, 0.116327], 'p_i': 20, 'u_i': 3.7824},
        {'id': 2, 'e_m': 5.605572, 'e_o_k': [3.216312, 2.573049, 2.058439], 'p_i': 40, 'u_i': 3.8452},
        {'id': 3, 'e_m': 26.502316, 'e_o_k': [10.057041, 8.045633, 6.436507, 5.149205, 4.119364, 3.295491], 'p_i': 80, 'u_i': 1.8919},
    ]
    B_BUDGET = 176.639997
    return processors, tasks, B_BUDGET
