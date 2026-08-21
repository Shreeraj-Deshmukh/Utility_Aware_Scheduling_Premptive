"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120003, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120003, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.078877, 'e_o_k': [0.255600, 0.204480, 0.163584], 'p_i': 10, 'u_i': 4.0982},
        {'id': 1, 'e_m': 1.760233, 'e_o_k': [0.143136, 0.114509, 0.091607, 0.073286, 0.058629, 0.046903], 'p_i': 20, 'u_i': 1.1937},
        {'id': 2, 'e_m': 14.854170, 'e_o_k': [1.207892, 0.966313, 0.773051, 0.618441, 0.494752, 0.395802], 'p_i': 40, 'u_i': 2.2048},
        {'id': 3, 'e_m': 37.655737, 'e_o_k': [3.062040, 2.449632, 1.959705, 1.567764, 1.254211, 1.003369], 'p_i': 80, 'u_i': 4.8929},
        {'id': 4, 'e_m': 36.310103, 'e_o_k': [3.240430, 2.592344, 2.073875, 1.659100, 1.327280], 'p_i': 80, 'u_i': 2.7826},
        {'id': 5, 'e_m': 3.483056, 'e_o_k': [0.580509, 0.464407], 'p_i': 80, 'u_i': 2.2829},
        {'id': 6, 'e_m': 36.070122, 'e_o_k': [3.219014, 2.575211, 2.060169, 1.648135, 1.318508], 'p_i': 80, 'u_i': 4.3795},
        {'id': 7, 'e_m': 2.275173, 'e_o_k': [0.279734, 0.223788, 0.179030], 'p_i': 20, 'u_i': 3.6679},
    ]
    B_BUDGET = 263.120003
    return processors, tasks, B_BUDGET
