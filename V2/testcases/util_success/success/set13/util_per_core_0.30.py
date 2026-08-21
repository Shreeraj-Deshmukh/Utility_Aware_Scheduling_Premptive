"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760007, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760007, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.084461, 'e_o_k': [0.010385, 0.008308, 0.006646], 'p_i': 10, 'u_i': 4.5768},
        {'id': 1, 'e_m': 0.515166, 'e_o_k': [0.085861, 0.068689], 'p_i': 20, 'u_i': 3.5463},
        {'id': 2, 'e_m': 1.629582, 'e_o_k': [0.271597, 0.217278], 'p_i': 40, 'u_i': 3.4252},
        {'id': 3, 'e_m': 3.236175, 'e_o_k': [0.328880, 0.263104, 0.210483, 0.168386], 'p_i': 80, 'u_i': 1.2792},
        {'id': 4, 'e_m': 0.285559, 'e_o_k': [0.029020, 0.023216, 0.018573, 0.014858], 'p_i': 10, 'u_i': 2.1862},
        {'id': 5, 'e_m': 6.010966, 'e_o_k': [0.739053, 0.591243, 0.472994], 'p_i': 80, 'u_i': 2.5645},
        {'id': 6, 'e_m': 1.645471, 'e_o_k': [0.167223, 0.133778, 0.107022, 0.085618], 'p_i': 10, 'u_i': 2.2998},
        {'id': 7, 'e_m': 17.309108, 'e_o_k': [2.128169, 1.702535, 1.362028], 'p_i': 80, 'u_i': 1.4896},
    ]
    B_BUDGET = 71.760007
    return processors, tasks, B_BUDGET
