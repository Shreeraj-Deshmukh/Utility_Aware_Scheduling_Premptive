"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519997, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519997, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.659080, 'e_o_k': [0.053594, 0.042875, 0.034300, 0.027440, 0.021952, 0.017562], 'p_i': 10, 'u_i': 3.3901},
        {'id': 1, 'e_m': 5.071832, 'e_o_k': [0.412425, 0.329940, 0.263952, 0.211161, 0.168929, 0.135143], 'p_i': 20, 'u_i': 2.3217},
        {'id': 2, 'e_m': 6.751660, 'e_o_k': [0.686144, 0.548915, 0.439132, 0.351306], 'p_i': 40, 'u_i': 2.1118},
        {'id': 3, 'e_m': 1.945009, 'e_o_k': [0.197663, 0.158131, 0.126505, 0.101204], 'p_i': 80, 'u_i': 4.2305},
        {'id': 4, 'e_m': 21.806910, 'e_o_k': [3.634485, 2.907588], 'p_i': 80, 'u_i': 2.0791},
        {'id': 5, 'e_m': 11.922324, 'e_o_k': [1.987054, 1.589643], 'p_i': 80, 'u_i': 1.4810},
        {'id': 6, 'e_m': 10.854177, 'e_o_k': [1.809030, 1.447224], 'p_i': 80, 'u_i': 3.5439},
        {'id': 7, 'e_m': 1.301037, 'e_o_k': [0.105796, 0.084637, 0.067709, 0.054168, 0.043334, 0.034667], 'p_i': 10, 'u_i': 4.1958},
    ]
    B_BUDGET = 143.519997
    return processors, tasks, B_BUDGET
