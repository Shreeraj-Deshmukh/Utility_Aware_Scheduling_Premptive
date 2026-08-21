"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119998, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119998, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.925864, 'e_o_k': [0.171870, 0.137496, 0.109997, 0.087998, 0.070398], 'p_i': 10, 'u_i': 1.7291},
        {'id': 1, 'e_m': 9.212317, 'e_o_k': [1.535386, 1.228309], 'p_i': 20, 'u_i': 2.1239},
        {'id': 2, 'e_m': 8.409035, 'e_o_k': [1.033898, 0.827118, 0.661695], 'p_i': 40, 'u_i': 3.4501},
        {'id': 3, 'e_m': 27.959990, 'e_o_k': [3.437704, 2.750163, 2.200130], 'p_i': 80, 'u_i': 2.5124},
        {'id': 4, 'e_m': 2.936512, 'e_o_k': [0.262064, 0.209651, 0.167721, 0.134177, 0.107341], 'p_i': 80, 'u_i': 1.0830},
        {'id': 5, 'e_m': 21.928163, 'e_o_k': [2.696086, 2.156869, 1.725495], 'p_i': 80, 'u_i': 1.0449},
        {'id': 6, 'e_m': 5.948200, 'e_o_k': [0.991367, 0.793093], 'p_i': 20, 'u_i': 4.1051},
        {'id': 7, 'e_m': 15.154142, 'e_o_k': [1.540055, 1.232044, 0.985635, 0.788508], 'p_i': 40, 'u_i': 3.9017},
    ]
    B_BUDGET = 263.119998
    return processors, tasks, B_BUDGET
