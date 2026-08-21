"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679994, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679994, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.259080, 'e_o_k': [0.102384, 0.081907, 0.065526, 0.052421, 0.041937, 0.033549], 'p_i': 10, 'u_i': 4.1820},
        {'id': 1, 'e_m': 3.910652, 'e_o_k': [0.651775, 0.521420], 'p_i': 20, 'u_i': 2.8729},
        {'id': 2, 'e_m': 0.555334, 'e_o_k': [0.068279, 0.054623, 0.043698], 'p_i': 40, 'u_i': 4.4646},
        {'id': 3, 'e_m': 5.117361, 'e_o_k': [0.852894, 0.682315], 'p_i': 80, 'u_i': 2.8456},
        {'id': 4, 'e_m': 0.830972, 'e_o_k': [0.084448, 0.067559, 0.054047, 0.043238], 'p_i': 10, 'u_i': 4.6357},
        {'id': 5, 'e_m': 13.997484, 'e_o_k': [2.332914, 1.866331], 'p_i': 80, 'u_i': 3.1275},
        {'id': 6, 'e_m': 1.327086, 'e_o_k': [0.134866, 0.107893, 0.086315, 0.069052], 'p_i': 10, 'u_i': 2.7677},
        {'id': 7, 'e_m': 0.099346, 'e_o_k': [0.010096, 0.008077, 0.006462, 0.005169], 'p_i': 10, 'u_i': 2.2237},
    ]
    B_BUDGET = 95.679994
    return processors, tasks, B_BUDGET
