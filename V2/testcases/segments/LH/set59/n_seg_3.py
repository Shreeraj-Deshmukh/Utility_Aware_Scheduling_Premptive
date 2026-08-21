"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320018, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320018, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.460174, 'e_o_k': [0.837805, 0.670244, 0.536195], 'p_i': 10, 'u_i': 1.9752},
        {'id': 1, 'e_m': 0.417207, 'e_o_k': [0.239381, 0.191505, 0.153204], 'p_i': 20, 'u_i': 3.9662},
        {'id': 2, 'e_m': 2.317386, 'e_o_k': [1.329648, 1.063718, 0.850975], 'p_i': 40, 'u_i': 1.9890},
        {'id': 3, 'e_m': 0.317304, 'e_o_k': [0.182060, 0.145648, 0.116518], 'p_i': 80, 'u_i': 3.3639},
        {'id': 4, 'e_m': 1.728593, 'e_o_k': [0.991815, 0.793452, 0.634762], 'p_i': 40, 'u_i': 4.7869},
        {'id': 5, 'e_m': 0.210554, 'e_o_k': [0.120810, 0.096648, 0.077318], 'p_i': 10, 'u_i': 2.7944},
        {'id': 6, 'e_m': 0.207004, 'e_o_k': [0.118773, 0.095018, 0.076015], 'p_i': 10, 'u_i': 4.7769},
        {'id': 7, 'e_m': 0.862507, 'e_o_k': [0.494881, 0.395905, 0.316724], 'p_i': 10, 'u_i': 1.3167},
    ]
    B_BUDGET = 88.320018
    return processors, tasks, B_BUDGET
