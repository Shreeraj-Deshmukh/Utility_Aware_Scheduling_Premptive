"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600008, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600008, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.606206, 'e_o_k': [0.054100, 0.043280, 0.034624, 0.027699, 0.022159], 'p_i': 10, 'u_i': 1.7042},
        {'id': 1, 'e_m': 0.920800, 'e_o_k': [0.113213, 0.090571, 0.072456], 'p_i': 20, 'u_i': 4.3788},
        {'id': 2, 'e_m': 5.709519, 'e_o_k': [0.580236, 0.464189, 0.371351, 0.297081], 'p_i': 40, 'u_i': 3.2500},
        {'id': 3, 'e_m': 3.238104, 'e_o_k': [0.539684, 0.431747], 'p_i': 80, 'u_i': 3.9101},
        {'id': 4, 'e_m': 1.495450, 'e_o_k': [0.151977, 0.121581, 0.097265, 0.077812], 'p_i': 80, 'u_i': 2.7187},
        {'id': 5, 'e_m': 7.055293, 'e_o_k': [0.573713, 0.458970, 0.367176, 0.293741, 0.234993, 0.187994], 'p_i': 40, 'u_i': 3.8755},
        {'id': 6, 'e_m': 32.494858, 'e_o_k': [3.995269, 3.196216, 2.556972], 'p_i': 80, 'u_i': 3.4836},
        {'id': 7, 'e_m': 4.354560, 'e_o_k': [0.535397, 0.428317, 0.342654], 'p_i': 40, 'u_i': 4.1699},
    ]
    B_BUDGET = 119.600008
    return processors, tasks, B_BUDGET
