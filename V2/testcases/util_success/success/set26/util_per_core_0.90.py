"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279993, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279993, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.889803, 'e_o_k': [0.232353, 0.185882, 0.148706], 'p_i': 10, 'u_i': 2.5499},
        {'id': 1, 'e_m': 0.684258, 'e_o_k': [0.061065, 0.048852, 0.039082, 0.031265, 0.025012], 'p_i': 20, 'u_i': 1.7451},
        {'id': 2, 'e_m': 18.669750, 'e_o_k': [1.666149, 1.332919, 1.066335, 0.853068, 0.682454], 'p_i': 40, 'u_i': 2.4288},
        {'id': 3, 'e_m': 15.508020, 'e_o_k': [1.261061, 1.008849, 0.807079, 0.645663, 0.516530, 0.413224], 'p_i': 80, 'u_i': 3.9538},
        {'id': 4, 'e_m': 16.645202, 'e_o_k': [1.691586, 1.353268, 1.082615, 0.866092], 'p_i': 40, 'u_i': 2.5770},
        {'id': 5, 'e_m': 15.434537, 'e_o_k': [1.568551, 1.254840, 1.003872, 0.803098], 'p_i': 80, 'u_i': 3.2919},
        {'id': 6, 'e_m': 9.927597, 'e_o_k': [0.885971, 0.708777, 0.567021, 0.453617, 0.362894], 'p_i': 40, 'u_i': 3.8099},
        {'id': 7, 'e_m': 2.358443, 'e_o_k': [0.393074, 0.314459], 'p_i': 40, 'u_i': 1.0957},
    ]
    B_BUDGET = 215.279993
    return processors, tasks, B_BUDGET
