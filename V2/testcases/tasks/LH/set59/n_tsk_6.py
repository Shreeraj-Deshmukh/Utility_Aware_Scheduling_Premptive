"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.882119, 'e_o_k': [1.463870, 1.171096], 'p_i': 10, 'u_i': 3.1325},
        {'id': 1, 'e_m': 0.510977, 'e_o_k': [0.397427, 0.317941], 'p_i': 20, 'u_i': 4.7073},
        {'id': 2, 'e_m': 2.822239, 'e_o_k': [1.070977, 0.856782, 0.685425, 0.548340, 0.438672, 0.350938], 'p_i': 40, 'u_i': 3.8560},
        {'id': 3, 'e_m': 0.414313, 'e_o_k': [0.237721, 0.190177, 0.152141], 'p_i': 80, 'u_i': 2.5226},
        {'id': 4, 'e_m': 2.573196, 'e_o_k': [1.220350, 0.976280, 0.781024, 0.624819], 'p_i': 40, 'u_i': 1.7775},
        {'id': 5, 'e_m': 0.461745, 'e_o_k': [0.359135, 0.287308], 'p_i': 10, 'u_i': 2.7606},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
