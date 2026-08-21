"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359995, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359995, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.682918, 'e_o_k': [0.329867, 0.263894, 0.211115], 'p_i': 10, 'u_i': 3.1129},
        {'id': 1, 'e_m': 5.645629, 'e_o_k': [0.503834, 0.403067, 0.322454, 0.257963, 0.206370], 'p_i': 20, 'u_i': 1.3211},
        {'id': 2, 'e_m': 14.288690, 'e_o_k': [2.381448, 1.905159], 'p_i': 40, 'u_i': 4.8977},
        {'id': 3, 'e_m': 17.463234, 'e_o_k': [2.910539, 2.328431], 'p_i': 80, 'u_i': 2.1715},
        {'id': 4, 'e_m': 5.725232, 'e_o_k': [0.703922, 0.563138, 0.450510], 'p_i': 20, 'u_i': 1.5264},
        {'id': 5, 'e_m': 0.251835, 'e_o_k': [0.041972, 0.033578], 'p_i': 40, 'u_i': 1.6618},
        {'id': 6, 'e_m': 1.360738, 'e_o_k': [0.121437, 0.097149, 0.077719, 0.062176, 0.049740], 'p_i': 20, 'u_i': 4.2147},
        {'id': 7, 'e_m': 4.532986, 'e_o_k': [0.755498, 0.604398], 'p_i': 40, 'u_i': 3.7475},
    ]
    B_BUDGET = 191.359995
    return processors, tasks, B_BUDGET
