"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280018, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280018, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.251722, 'e_o_k': [0.101786, 0.081429, 0.065143, 0.052114, 0.041692, 0.033353], 'p_i': 10, 'u_i': 4.6185},
        {'id': 1, 'e_m': 5.517276, 'e_o_k': [0.560699, 0.448559, 0.358847, 0.287078], 'p_i': 20, 'u_i': 4.7933},
        {'id': 2, 'e_m': 3.835451, 'e_o_k': [0.389782, 0.311825, 0.249460, 0.199568], 'p_i': 40, 'u_i': 3.4915},
        {'id': 3, 'e_m': 10.617511, 'e_o_k': [1.769585, 1.415668], 'p_i': 80, 'u_i': 2.0641},
        {'id': 4, 'e_m': 0.208424, 'e_o_k': [0.016948, 0.013559, 0.010847, 0.008678, 0.006942, 0.005554], 'p_i': 10, 'u_i': 2.2431},
        {'id': 5, 'e_m': 4.782732, 'e_o_k': [0.588041, 0.470433, 0.376346], 'p_i': 10, 'u_i': 2.3907},
        {'id': 6, 'e_m': 4.065654, 'e_o_k': [0.413176, 0.330541, 0.264433, 0.211546], 'p_i': 20, 'u_i': 1.1089},
        {'id': 7, 'e_m': 18.718423, 'e_o_k': [1.902279, 1.521823, 1.217458, 0.973967], 'p_i': 40, 'u_i': 1.2989},
    ]
    B_BUDGET = 215.280018
    return processors, tasks, B_BUDGET
