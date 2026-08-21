"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199976, "H": 80, "J": 34, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "freq", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199976, "H": 80, "J": 34, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "freq", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.630729, 'e_o_k': [0.276207, 0.220966, 0.176773, 0.141418], 'p_i': 10, 'u_i': 2.1780},
        {'id': 1, 'e_m': 0.554446, 'e_o_k': [0.113616, 0.090893, 0.072714], 'p_i': 20, 'u_i': 3.8388},
        {'id': 2, 'e_m': 1.443928, 'e_o_k': [0.244568, 0.195654, 0.156523, 0.125219], 'p_i': 40, 'u_i': 1.0041},
        {'id': 3, 'e_m': 3.915968, 'e_o_k': [1.087769, 0.870215], 'p_i': 80, 'u_i': 4.1994},
        {'id': 4, 'e_m': 0.833670, 'e_o_k': [0.112985, 0.090388, 0.072311, 0.057849, 0.046279, 0.037023], 'p_i': 40, 'u_i': 2.8402},
        {'id': 5, 'e_m': 0.367491, 'e_o_k': [0.049805, 0.039844, 0.031875, 0.025500, 0.020400, 0.016320], 'p_i': 10, 'u_i': 1.6917},
        {'id': 6, 'e_m': 0.185253, 'e_o_k': [0.027554, 0.022043, 0.017635, 0.014108, 0.011286], 'p_i': 10, 'u_i': 1.6028},
        {'id': 7, 'e_m': 3.843267, 'e_o_k': [0.787555, 0.630044, 0.504035], 'p_i': 80, 'u_i': 2.5090},
    ]
    B_BUDGET = 55.199976
    return processors, tasks, B_BUDGET
