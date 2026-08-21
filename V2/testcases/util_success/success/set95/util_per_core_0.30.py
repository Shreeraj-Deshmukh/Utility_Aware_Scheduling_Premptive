"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760003, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760003, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.187866, 'e_o_k': [0.120718, 0.096574, 0.077260, 0.061808], 'p_i': 10, 'u_i': 1.9313},
        {'id': 1, 'e_m': 2.182641, 'e_o_k': [0.363773, 0.291019], 'p_i': 20, 'u_i': 4.0147},
        {'id': 2, 'e_m': 5.117424, 'e_o_k': [0.416132, 0.332906, 0.266324, 0.213060, 0.170448, 0.136358], 'p_i': 40, 'u_i': 3.8759},
        {'id': 3, 'e_m': 2.264753, 'e_o_k': [0.278453, 0.222763, 0.178210], 'p_i': 80, 'u_i': 4.3076},
        {'id': 4, 'e_m': 2.937308, 'e_o_k': [0.238852, 0.191082, 0.152865, 0.122292, 0.097834, 0.078267], 'p_i': 80, 'u_i': 1.9116},
        {'id': 5, 'e_m': 2.029849, 'e_o_k': [0.249572, 0.199657, 0.159726], 'p_i': 40, 'u_i': 2.7475},
        {'id': 6, 'e_m': 6.173471, 'e_o_k': [0.550940, 0.440752, 0.352602, 0.282082, 0.225665], 'p_i': 80, 'u_i': 2.9584},
        {'id': 7, 'e_m': 1.024107, 'e_o_k': [0.104076, 0.083261, 0.066609, 0.053287], 'p_i': 20, 'u_i': 3.8181},
    ]
    B_BUDGET = 71.760003
    return processors, tasks, B_BUDGET
