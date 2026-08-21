"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599984, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599984, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.251860, 'e_o_k': [0.022477, 0.017981, 0.014385, 0.011508, 0.009206], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 1.802287, 'e_o_k': [0.146556, 0.117245, 0.093796, 0.075037, 0.060029, 0.048023], 'p_i': 20, 'u_i': 3.3967},
        {'id': 2, 'e_m': 10.827363, 'e_o_k': [1.804560, 1.443648], 'p_i': 40, 'u_i': 1.9449},
        {'id': 3, 'e_m': 11.127716, 'e_o_k': [1.854619, 1.483695], 'p_i': 80, 'u_i': 4.6056},
        {'id': 4, 'e_m': 7.492032, 'e_o_k': [1.248672, 0.998938], 'p_i': 40, 'u_i': 2.0280},
        {'id': 5, 'e_m': 5.428016, 'e_o_k': [0.441388, 0.353111, 0.282488, 0.225991, 0.180793, 0.144634], 'p_i': 80, 'u_i': 1.2717},
        {'id': 6, 'e_m': 1.626692, 'e_o_k': [0.271115, 0.216892], 'p_i': 10, 'u_i': 1.1584},
        {'id': 7, 'e_m': 4.567915, 'e_o_k': [0.561629, 0.449303, 0.359442], 'p_i': 80, 'u_i': 3.8897},
    ]
    B_BUDGET = 119.599984
    return processors, tasks, B_BUDGET
