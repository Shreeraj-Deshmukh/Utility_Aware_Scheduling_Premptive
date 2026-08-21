"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.755587, 'e_o_k': [0.154833, 0.123867, 0.099093], 'p_i': 10, 'u_i': 2.2612},
        {'id': 1, 'e_m': 1.886707, 'e_o_k': [0.319564, 0.255651, 0.204521, 0.163617], 'p_i': 20, 'u_i': 2.3936},
        {'id': 2, 'e_m': 6.107478, 'e_o_k': [1.034464, 0.827572, 0.662057, 0.529646], 'p_i': 40, 'u_i': 4.7316},
        {'id': 3, 'e_m': 6.193521, 'e_o_k': [1.049038, 0.839231, 0.671384, 0.537108], 'p_i': 80, 'u_i': 1.7602},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET
