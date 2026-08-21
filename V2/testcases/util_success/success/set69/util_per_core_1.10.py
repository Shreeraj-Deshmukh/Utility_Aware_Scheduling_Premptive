"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120014, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120014, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.750645, 'e_o_k': [0.584096, 0.467277, 0.373821], 'p_i': 10, 'u_i': 2.7456},
        {'id': 1, 'e_m': 4.534156, 'e_o_k': [0.557478, 0.445983, 0.356786], 'p_i': 20, 'u_i': 1.4781},
        {'id': 2, 'e_m': 9.721597, 'e_o_k': [0.790528, 0.632422, 0.505938, 0.404750, 0.323800, 0.259040], 'p_i': 40, 'u_i': 4.2271},
        {'id': 3, 'e_m': 11.154203, 'e_o_k': [1.133557, 0.906846, 0.725477, 0.580381], 'p_i': 80, 'u_i': 2.1613},
        {'id': 4, 'e_m': 2.677275, 'e_o_k': [0.272081, 0.217665, 0.174132, 0.139305], 'p_i': 10, 'u_i': 3.4475},
        {'id': 5, 'e_m': 3.424552, 'e_o_k': [0.570759, 0.456607], 'p_i': 10, 'u_i': 3.7603},
        {'id': 6, 'e_m': 4.863616, 'e_o_k': [0.597986, 0.478388, 0.382711], 'p_i': 10, 'u_i': 4.2692},
        {'id': 7, 'e_m': 0.768638, 'e_o_k': [0.128106, 0.102485], 'p_i': 40, 'u_i': 2.3975},
    ]
    B_BUDGET = 263.120014
    return processors, tasks, B_BUDGET
