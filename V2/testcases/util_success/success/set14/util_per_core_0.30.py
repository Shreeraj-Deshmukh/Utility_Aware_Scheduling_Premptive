"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.76, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.76, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.541844, 'e_o_k': [0.090307, 0.072246], 'p_i': 10, 'u_i': 1.0216},
        {'id': 1, 'e_m': 2.315166, 'e_o_k': [0.284652, 0.227721, 0.182177], 'p_i': 20, 'u_i': 4.0085},
        {'id': 2, 'e_m': 8.409504, 'e_o_k': [1.033955, 0.827164, 0.661731], 'p_i': 40, 'u_i': 1.9931},
        {'id': 3, 'e_m': 3.349549, 'e_o_k': [0.411830, 0.329464, 0.263571], 'p_i': 80, 'u_i': 2.4773},
        {'id': 4, 'e_m': 0.126630, 'e_o_k': [0.012869, 0.010295, 0.008236, 0.006589], 'p_i': 80, 'u_i': 3.1022},
        {'id': 5, 'e_m': 1.491060, 'e_o_k': [0.121248, 0.096998, 0.077599, 0.062079, 0.049663, 0.039731], 'p_i': 40, 'u_i': 1.9821},
        {'id': 6, 'e_m': 5.933416, 'e_o_k': [0.729518, 0.583615, 0.466892], 'p_i': 80, 'u_i': 1.2190},
        {'id': 7, 'e_m': 5.193863, 'e_o_k': [0.527832, 0.422265, 0.337812, 0.270250], 'p_i': 80, 'u_i': 2.8489},
    ]
    B_BUDGET = 71.760000
    return processors, tasks, B_BUDGET
