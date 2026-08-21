"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279995, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279995, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.651247, 'e_o_k': [0.325973, 0.260778, 0.208623], 'p_i': 10, 'u_i': 2.4893},
        {'id': 1, 'e_m': 6.806403, 'e_o_k': [0.836853, 0.669482, 0.535586], 'p_i': 20, 'u_i': 4.7173},
        {'id': 2, 'e_m': 15.229198, 'e_o_k': [2.538200, 2.030560], 'p_i': 40, 'u_i': 2.7558},
        {'id': 3, 'e_m': 35.872365, 'e_o_k': [3.201365, 2.561092, 2.048874, 1.639099, 1.311279], 'p_i': 80, 'u_i': 2.1995},
        {'id': 4, 'e_m': 6.968226, 'e_o_k': [0.856749, 0.685399, 0.548319], 'p_i': 40, 'u_i': 2.7585},
        {'id': 5, 'e_m': 1.297008, 'e_o_k': [0.115749, 0.092599, 0.074079, 0.059264, 0.047411], 'p_i': 10, 'u_i': 4.0797},
        {'id': 6, 'e_m': 0.473650, 'e_o_k': [0.048135, 0.038508, 0.030807, 0.024645], 'p_i': 10, 'u_i': 3.6908},
        {'id': 7, 'e_m': 0.282984, 'e_o_k': [0.028759, 0.023007, 0.018405, 0.014724], 'p_i': 20, 'u_i': 3.3068},
    ]
    B_BUDGET = 215.279995
    return processors, tasks, B_BUDGET
