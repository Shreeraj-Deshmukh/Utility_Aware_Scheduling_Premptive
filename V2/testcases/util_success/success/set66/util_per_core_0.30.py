"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759991, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759991, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.100711, 'e_o_k': [0.010235, 0.008188, 0.006550, 0.005240], 'p_i': 10, 'u_i': 3.0491},
        {'id': 1, 'e_m': 1.196329, 'e_o_k': [0.106764, 0.085411, 0.068329, 0.054663, 0.043731], 'p_i': 20, 'u_i': 3.9469},
        {'id': 2, 'e_m': 3.065248, 'e_o_k': [0.376875, 0.301500, 0.241200], 'p_i': 40, 'u_i': 1.2331},
        {'id': 3, 'e_m': 7.584180, 'e_o_k': [0.932481, 0.745985, 0.596788], 'p_i': 80, 'u_i': 3.8857},
        {'id': 4, 'e_m': 1.436970, 'e_o_k': [0.239495, 0.191596], 'p_i': 20, 'u_i': 4.4773},
        {'id': 5, 'e_m': 0.754023, 'e_o_k': [0.125671, 0.100536], 'p_i': 10, 'u_i': 2.4546},
        {'id': 6, 'e_m': 0.820124, 'e_o_k': [0.083346, 0.066677, 0.053341, 0.042673], 'p_i': 80, 'u_i': 1.1544},
        {'id': 7, 'e_m': 16.094129, 'e_o_k': [1.978786, 1.583029, 1.266423], 'p_i': 80, 'u_i': 4.0204},
    ]
    B_BUDGET = 71.759991
    return processors, tasks, B_BUDGET
