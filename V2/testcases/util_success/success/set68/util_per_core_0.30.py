"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759991, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759991, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.697975, 'e_o_k': [0.116329, 0.093063], 'p_i': 10, 'u_i': 3.1458},
        {'id': 1, 'e_m': 2.448209, 'e_o_k': [0.248802, 0.199041, 0.159233, 0.127386], 'p_i': 20, 'u_i': 4.9683},
        {'id': 2, 'e_m': 2.082847, 'e_o_k': [0.347141, 0.277713], 'p_i': 40, 'u_i': 2.4718},
        {'id': 3, 'e_m': 6.198211, 'e_o_k': [0.504018, 0.403214, 0.322571, 0.258057, 0.206446, 0.165157], 'p_i': 80, 'u_i': 4.0774},
        {'id': 4, 'e_m': 2.249155, 'e_o_k': [0.182894, 0.146315, 0.117052, 0.093642, 0.074913, 0.059931], 'p_i': 80, 'u_i': 2.9703},
        {'id': 5, 'e_m': 0.296524, 'e_o_k': [0.026463, 0.021170, 0.016936, 0.013549, 0.010839], 'p_i': 40, 'u_i': 3.9269},
        {'id': 6, 'e_m': 1.909314, 'e_o_k': [0.318219, 0.254575], 'p_i': 10, 'u_i': 3.4836},
        {'id': 7, 'e_m': 2.071372, 'e_o_k': [0.184856, 0.147885, 0.118308, 0.094646, 0.075717], 'p_i': 40, 'u_i': 2.8974},
    ]
    B_BUDGET = 71.759991
    return processors, tasks, B_BUDGET
