"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600003, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600003, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.573851, 'e_o_k': [0.127980, 0.102384, 0.081907, 0.065526, 0.052421, 0.041937], 'p_i': 10, 'u_i': 4.1820},
        {'id': 1, 'e_m': 4.888315, 'e_o_k': [0.814719, 0.651775], 'p_i': 20, 'u_i': 2.8729},
        {'id': 2, 'e_m': 0.694168, 'e_o_k': [0.085349, 0.068279, 0.054623], 'p_i': 40, 'u_i': 4.4646},
        {'id': 3, 'e_m': 6.396702, 'e_o_k': [1.066117, 0.852894], 'p_i': 80, 'u_i': 2.8456},
        {'id': 4, 'e_m': 1.038715, 'e_o_k': [0.105561, 0.084448, 0.067559, 0.054047], 'p_i': 10, 'u_i': 4.6357},
        {'id': 5, 'e_m': 17.496855, 'e_o_k': [2.916143, 2.332914], 'p_i': 80, 'u_i': 3.1275},
        {'id': 6, 'e_m': 1.658857, 'e_o_k': [0.168583, 0.134866, 0.107893, 0.086315], 'p_i': 10, 'u_i': 2.7677},
        {'id': 7, 'e_m': 0.124183, 'e_o_k': [0.012620, 0.010096, 0.008077, 0.006462], 'p_i': 10, 'u_i': 2.2237},
    ]
    B_BUDGET = 119.600003
    return processors, tasks, B_BUDGET
