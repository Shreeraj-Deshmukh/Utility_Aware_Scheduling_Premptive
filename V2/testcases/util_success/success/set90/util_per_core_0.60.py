"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520001, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520001, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.692418, 'e_o_k': [0.171994, 0.137595, 0.110076, 0.088061], 'p_i': 10, 'u_i': 1.1071},
        {'id': 1, 'e_m': 1.278005, 'e_o_k': [0.213001, 0.170401], 'p_i': 20, 'u_i': 4.7513},
        {'id': 2, 'e_m': 8.113876, 'e_o_k': [0.659793, 0.527835, 0.422268, 0.337814, 0.270251, 0.216201], 'p_i': 40, 'u_i': 2.4512},
        {'id': 3, 'e_m': 2.589075, 'e_o_k': [0.431512, 0.345210], 'p_i': 80, 'u_i': 1.4858},
        {'id': 4, 'e_m': 15.164852, 'e_o_k': [1.233155, 0.986524, 0.789219, 0.631376, 0.505100, 0.404080], 'p_i': 40, 'u_i': 3.8296},
        {'id': 5, 'e_m': 2.261721, 'e_o_k': [0.229850, 0.183880, 0.147104, 0.117683], 'p_i': 20, 'u_i': 2.8775},
        {'id': 6, 'e_m': 4.544412, 'e_o_k': [0.405558, 0.324446, 0.259557, 0.207646, 0.166117], 'p_i': 40, 'u_i': 4.5934},
        {'id': 7, 'e_m': 2.516599, 'e_o_k': [0.204641, 0.163713, 0.130971, 0.104776, 0.083821, 0.067057], 'p_i': 20, 'u_i': 1.6361},
    ]
    B_BUDGET = 143.520001
    return processors, tasks, B_BUDGET
