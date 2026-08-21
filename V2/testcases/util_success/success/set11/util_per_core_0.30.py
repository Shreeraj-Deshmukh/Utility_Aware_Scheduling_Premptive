"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760012, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760012, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.800671, 'e_o_k': [0.071454, 0.057164, 0.045731, 0.036585, 0.029268], 'p_i': 10, 'u_i': 4.6830},
        {'id': 1, 'e_m': 4.577702, 'e_o_k': [0.762950, 0.610360], 'p_i': 20, 'u_i': 2.4027},
        {'id': 2, 'e_m': 3.403317, 'e_o_k': [0.567219, 0.453776], 'p_i': 40, 'u_i': 2.7203},
        {'id': 3, 'e_m': 3.041210, 'e_o_k': [0.247301, 0.197841, 0.158273, 0.126618, 0.101295, 0.081036], 'p_i': 80, 'u_i': 2.4000},
        {'id': 4, 'e_m': 0.261884, 'e_o_k': [0.043647, 0.034918], 'p_i': 20, 'u_i': 2.9059},
        {'id': 5, 'e_m': 0.518244, 'e_o_k': [0.063718, 0.050975, 0.040780], 'p_i': 10, 'u_i': 3.1411},
        {'id': 6, 'e_m': 4.077442, 'e_o_k': [0.414374, 0.331499, 0.265199, 0.212160], 'p_i': 80, 'u_i': 3.1206},
        {'id': 7, 'e_m': 2.082528, 'e_o_k': [0.256049, 0.204839, 0.163871], 'p_i': 40, 'u_i': 4.7030},
    ]
    B_BUDGET = 71.760012
    return processors, tasks, B_BUDGET
