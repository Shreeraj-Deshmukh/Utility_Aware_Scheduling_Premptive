"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.6, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.6, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.693970, 'e_o_k': [0.070525, 0.056420, 0.045136, 0.036109], 'p_i': 10, 'u_i': 2.4751},
        {'id': 1, 'e_m': 1.064325, 'e_o_k': [0.094984, 0.075987, 0.060790, 0.048632, 0.038905], 'p_i': 20, 'u_i': 3.6644},
        {'id': 2, 'e_m': 4.244629, 'e_o_k': [0.378804, 0.303043, 0.242435, 0.193948, 0.155158], 'p_i': 40, 'u_i': 2.2976},
        {'id': 3, 'e_m': 4.352892, 'e_o_k': [0.388466, 0.310773, 0.248618, 0.198895, 0.159116], 'p_i': 80, 'u_i': 4.8639},
        {'id': 4, 'e_m': 5.041728, 'e_o_k': [0.840288, 0.672230], 'p_i': 40, 'u_i': 4.5045},
        {'id': 5, 'e_m': 3.486683, 'e_o_k': [0.428691, 0.342952, 0.274362], 'p_i': 80, 'u_i': 1.0020},
        {'id': 6, 'e_m': 4.459095, 'e_o_k': [0.453160, 0.362528, 0.290022, 0.232018], 'p_i': 40, 'u_i': 4.9529},
        {'id': 7, 'e_m': 4.357558, 'e_o_k': [0.726260, 0.581008], 'p_i': 10, 'u_i': 2.3587},
    ]
    B_BUDGET = 119.600000
    return processors, tasks, B_BUDGET
