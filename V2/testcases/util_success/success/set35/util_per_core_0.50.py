"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600006, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600006, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.383283, 'e_o_k': [0.038952, 0.031161, 0.024929, 0.019943], 'p_i': 10, 'u_i': 2.6246},
        {'id': 1, 'e_m': 0.370923, 'e_o_k': [0.030162, 0.024130, 0.019304, 0.015443, 0.012354, 0.009884], 'p_i': 20, 'u_i': 2.3478},
        {'id': 2, 'e_m': 5.675558, 'e_o_k': [0.697815, 0.558252, 0.446601], 'p_i': 40, 'u_i': 2.5491},
        {'id': 3, 'e_m': 18.189193, 'e_o_k': [1.623262, 1.298610, 1.038888, 0.831110, 0.664888], 'p_i': 80, 'u_i': 2.9783},
        {'id': 4, 'e_m': 6.701254, 'e_o_k': [1.116876, 0.893501], 'p_i': 20, 'u_i': 1.6186},
        {'id': 5, 'e_m': 3.670264, 'e_o_k': [0.298454, 0.238763, 0.191010, 0.152808, 0.122247, 0.097797], 'p_i': 40, 'u_i': 2.1935},
        {'id': 6, 'e_m': 1.424703, 'e_o_k': [0.175168, 0.140135, 0.112108], 'p_i': 20, 'u_i': 1.0173},
        {'id': 7, 'e_m': 0.758172, 'e_o_k': [0.126362, 0.101090], 'p_i': 10, 'u_i': 4.7591},
    ]
    B_BUDGET = 119.600006
    return processors, tasks, B_BUDGET
