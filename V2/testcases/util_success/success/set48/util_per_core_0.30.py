"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759994, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759994, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.029009, 'e_o_k': [0.171501, 0.137201], 'p_i': 10, 'u_i': 2.6470},
        {'id': 1, 'e_m': 2.616249, 'e_o_k': [0.321670, 0.257336, 0.205869], 'p_i': 20, 'u_i': 4.9479},
        {'id': 2, 'e_m': 0.071973, 'e_o_k': [0.008849, 0.007079, 0.005663], 'p_i': 40, 'u_i': 2.1346},
        {'id': 3, 'e_m': 2.894647, 'e_o_k': [0.482441, 0.385953], 'p_i': 80, 'u_i': 1.3827},
        {'id': 4, 'e_m': 8.728294, 'e_o_k': [1.454716, 1.163773], 'p_i': 80, 'u_i': 3.9576},
        {'id': 5, 'e_m': 1.638940, 'e_o_k': [0.146264, 0.117011, 0.093609, 0.074887, 0.059910], 'p_i': 20, 'u_i': 4.9670},
        {'id': 6, 'e_m': 1.263114, 'e_o_k': [0.112724, 0.090180, 0.072144, 0.057715, 0.046172], 'p_i': 10, 'u_i': 4.5958},
        {'id': 7, 'e_m': 0.875372, 'e_o_k': [0.078121, 0.062497, 0.049997, 0.039998, 0.031998], 'p_i': 80, 'u_i': 1.9552},
    ]
    B_BUDGET = 71.759994
    return processors, tasks, B_BUDGET
