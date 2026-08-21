"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 36.800002, "H": 80, "J": 25, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.0, "seed": 1041, "set": 41, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.00"}
"""

_SPEC = '{"B": 36.800002, "H": 80, "J": 25, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.0, "seed": 1041, "set": 41, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.439041, 'e_o_k': [0.089967, 0.071974, 0.057579], 'p_i': 10, 'u_i': 1.3531},
        {'id': 1, 'e_m': 0.880194, 'e_o_k': [0.119291, 0.095433, 0.076346, 0.061077, 0.048862, 0.039089], 'p_i': 20, 'u_i': 3.7145},
        {'id': 2, 'e_m': 7.606803, 'e_o_k': [2.113001, 1.690401], 'p_i': 40, 'u_i': 2.6488},
        {'id': 3, 'e_m': 0.610708, 'e_o_k': [0.082768, 0.066214, 0.052971, 0.042377, 0.033902, 0.027121], 'p_i': 80, 'u_i': 4.3024},
        {'id': 4, 'e_m': 0.933835, 'e_o_k': [0.191360, 0.153088, 0.122470], 'p_i': 20, 'u_i': 4.8206},
        {'id': 5, 'e_m': 0.975572, 'e_o_k': [0.132217, 0.105774, 0.084619, 0.067695, 0.054156, 0.043325], 'p_i': 20, 'u_i': 3.2508},
        {'id': 6, 'e_m': 0.921104, 'e_o_k': [0.188751, 0.151001, 0.120801], 'p_i': 80, 'u_i': 3.3334},
        {'id': 7, 'e_m': 0.583852, 'e_o_k': [0.162181, 0.129745], 'p_i': 80, 'u_i': 2.1081},
    ]
    B_BUDGET = 36.800002
    return processors, tasks, B_BUDGET
