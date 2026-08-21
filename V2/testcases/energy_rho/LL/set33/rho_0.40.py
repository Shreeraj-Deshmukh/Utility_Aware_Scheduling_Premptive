"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 44.160006, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.4, "seed": 1033, "set": 33, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.40"}
"""

_SPEC = '{"B": 44.160006, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.4, "seed": 1033, "set": 33, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.024096, 'e_o_k': [0.004938, 0.003950, 0.003160], 'p_i': 10, 'u_i': 4.1859},
        {'id': 1, 'e_m': 1.824026, 'e_o_k': [0.373776, 0.299021, 0.239216], 'p_i': 20, 'u_i': 1.3758},
        {'id': 2, 'e_m': 2.806108, 'e_o_k': [0.575022, 0.460018, 0.368014], 'p_i': 40, 'u_i': 3.6848},
        {'id': 3, 'e_m': 0.481622, 'e_o_k': [0.133784, 0.107027], 'p_i': 80, 'u_i': 1.6851},
        {'id': 4, 'e_m': 2.721725, 'e_o_k': [0.404826, 0.323861, 0.259089, 0.207271, 0.165817], 'p_i': 20, 'u_i': 1.3700},
        {'id': 5, 'e_m': 0.681310, 'e_o_k': [0.101337, 0.081070, 0.064856, 0.051885, 0.041508], 'p_i': 10, 'u_i': 3.3252},
        {'id': 6, 'e_m': 0.612959, 'e_o_k': [0.170266, 0.136213], 'p_i': 80, 'u_i': 4.3008},
        {'id': 7, 'e_m': 1.466951, 'e_o_k': [0.248467, 0.198774, 0.159019, 0.127215], 'p_i': 80, 'u_i': 2.2362},
    ]
    B_BUDGET = 44.160006
    return processors, tasks, B_BUDGET
