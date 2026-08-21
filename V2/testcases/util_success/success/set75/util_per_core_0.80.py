"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360002, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360002, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.176608, 'e_o_k': [0.529435, 0.423548], 'p_i': 10, 'u_i': 1.1590},
        {'id': 1, 'e_m': 8.317512, 'e_o_k': [1.386252, 1.109002], 'p_i': 20, 'u_i': 4.3960},
        {'id': 2, 'e_m': 10.095915, 'e_o_k': [0.900992, 0.720794, 0.576635, 0.461308, 0.369046], 'p_i': 40, 'u_i': 2.4870},
        {'id': 3, 'e_m': 8.708780, 'e_o_k': [0.708169, 0.566535, 0.453228, 0.362583, 0.290066, 0.232053], 'p_i': 80, 'u_i': 2.1849},
        {'id': 4, 'e_m': 8.096957, 'e_o_k': [0.722599, 0.578079, 0.462463, 0.369970, 0.295976], 'p_i': 40, 'u_i': 2.3820},
        {'id': 5, 'e_m': 1.683079, 'e_o_k': [0.150203, 0.120163, 0.096130, 0.076904, 0.061523], 'p_i': 40, 'u_i': 1.7984},
        {'id': 6, 'e_m': 10.074330, 'e_o_k': [1.238647, 0.990918, 0.792734], 'p_i': 40, 'u_i': 4.6658},
        {'id': 7, 'e_m': 0.353871, 'e_o_k': [0.043509, 0.034807, 0.027846], 'p_i': 40, 'u_i': 1.0345},
    ]
    B_BUDGET = 191.360002
    return processors, tasks, B_BUDGET
