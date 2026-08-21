"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360003, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360003, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.992402, 'e_o_k': [0.832067, 0.665654], 'p_i': 10, 'u_i': 2.5346},
        {'id': 1, 'e_m': 6.129817, 'e_o_k': [0.753666, 0.602933, 0.482346], 'p_i': 20, 'u_i': 2.7749},
        {'id': 2, 'e_m': 13.659895, 'e_o_k': [1.110777, 0.888622, 0.710897, 0.568718, 0.454974, 0.363979], 'p_i': 40, 'u_i': 1.2098},
        {'id': 3, 'e_m': 2.490933, 'e_o_k': [0.306262, 0.245010, 0.196008], 'p_i': 80, 'u_i': 1.7928},
        {'id': 4, 'e_m': 2.782825, 'e_o_k': [0.226290, 0.181032, 0.144826, 0.115861, 0.092688, 0.074151], 'p_i': 20, 'u_i': 1.8586},
        {'id': 5, 'e_m': 7.007129, 'e_o_k': [0.861532, 0.689226, 0.551381], 'p_i': 40, 'u_i': 3.5571},
        {'id': 6, 'e_m': 3.849098, 'e_o_k': [0.312996, 0.250397, 0.200317, 0.160254, 0.128203, 0.102562], 'p_i': 40, 'u_i': 3.6967},
        {'id': 7, 'e_m': 0.221760, 'e_o_k': [0.027266, 0.021812, 0.017450], 'p_i': 20, 'u_i': 3.6040},
    ]
    B_BUDGET = 191.360003
    return processors, tasks, B_BUDGET
