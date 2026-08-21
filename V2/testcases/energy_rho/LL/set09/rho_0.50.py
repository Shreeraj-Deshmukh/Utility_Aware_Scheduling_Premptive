"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 46.000003, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.5, "seed": 1009, "set": 9, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.50"}
"""

_SPEC = '{"B": 46.000003, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.5, "seed": 1009, "set": 9, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.868614, 'e_o_k': [0.241282, 0.193025], 'p_i': 10, 'u_i': 1.8132},
        {'id': 1, 'e_m': 0.707032, 'e_o_k': [0.095822, 0.076658, 0.061326, 0.049061, 0.039249, 0.031399], 'p_i': 20, 'u_i': 1.3118},
        {'id': 2, 'e_m': 4.447481, 'e_o_k': [0.661512, 0.529210, 0.423368, 0.338694, 0.270956], 'p_i': 40, 'u_i': 1.6432},
        {'id': 3, 'e_m': 1.996160, 'e_o_k': [0.554489, 0.443591], 'p_i': 80, 'u_i': 3.2827},
        {'id': 4, 'e_m': 0.078011, 'e_o_k': [0.011603, 0.009283, 0.007426, 0.005941, 0.004753], 'p_i': 20, 'u_i': 1.0597},
        {'id': 5, 'e_m': 0.176089, 'e_o_k': [0.036084, 0.028867, 0.023094], 'p_i': 20, 'u_i': 4.4596},
        {'id': 6, 'e_m': 2.563544, 'e_o_k': [0.434205, 0.347364, 0.277891, 0.222313], 'p_i': 40, 'u_i': 4.8824},
        {'id': 7, 'e_m': 0.648544, 'e_o_k': [0.132898, 0.106319, 0.085055], 'p_i': 10, 'u_i': 1.5609},
    ]
    B_BUDGET = 46.000003
    return processors, tasks, B_BUDGET
