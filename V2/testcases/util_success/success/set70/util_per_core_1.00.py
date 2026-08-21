"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199989, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199989, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.845694, 'e_o_k': [0.164716, 0.131773, 0.105418, 0.084334, 0.067468], 'p_i': 10, 'u_i': 1.3844},
        {'id': 1, 'e_m': 7.272406, 'e_o_k': [0.649013, 0.519210, 0.415368, 0.332295, 0.265836], 'p_i': 20, 'u_i': 3.8571},
        {'id': 2, 'e_m': 9.485707, 'e_o_k': [1.580951, 1.264761], 'p_i': 40, 'u_i': 3.6185},
        {'id': 3, 'e_m': 1.282898, 'e_o_k': [0.130376, 0.104301, 0.083441, 0.066752], 'p_i': 80, 'u_i': 1.1495},
        {'id': 4, 'e_m': 5.200206, 'e_o_k': [0.528476, 0.422781, 0.338225, 0.270580], 'p_i': 20, 'u_i': 2.9121},
        {'id': 5, 'e_m': 2.669813, 'e_o_k': [0.238263, 0.190610, 0.152488, 0.121991, 0.097592], 'p_i': 10, 'u_i': 1.1301},
        {'id': 6, 'e_m': 6.109202, 'e_o_k': [1.018200, 0.814560], 'p_i': 20, 'u_i': 4.2884},
        {'id': 7, 'e_m': 3.661796, 'e_o_k': [0.326790, 0.261432, 0.209146, 0.167317, 0.133853], 'p_i': 10, 'u_i': 4.6426},
    ]
    B_BUDGET = 239.199989
    return processors, tasks, B_BUDGET
