"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.52, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.52, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.720525, 'e_o_k': [0.286754, 0.229403], 'p_i': 10, 'u_i': 2.5980},
        {'id': 1, 'e_m': 5.660633, 'e_o_k': [0.943439, 0.754751], 'p_i': 20, 'u_i': 2.9083},
        {'id': 2, 'e_m': 8.025716, 'e_o_k': [0.986768, 0.789415, 0.631532], 'p_i': 40, 'u_i': 4.8275},
        {'id': 3, 'e_m': 25.453870, 'e_o_k': [2.271585, 1.817268, 1.453815, 1.163052, 0.930441], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 1.649245, 'e_o_k': [0.202776, 0.162221, 0.129777], 'p_i': 20, 'u_i': 1.8333},
        {'id': 5, 'e_m': 0.223446, 'e_o_k': [0.019941, 0.015953, 0.012762, 0.010210, 0.008168], 'p_i': 20, 'u_i': 4.5368},
        {'id': 6, 'e_m': 4.946868, 'e_o_k': [0.402263, 0.321810, 0.257448, 0.205959, 0.164767, 0.131813], 'p_i': 80, 'u_i': 4.6383},
        {'id': 7, 'e_m': 5.650335, 'e_o_k': [0.504254, 0.403403, 0.322723, 0.258178, 0.206542], 'p_i': 80, 'u_i': 3.5515},
    ]
    B_BUDGET = 143.520000
    return processors, tasks, B_BUDGET
