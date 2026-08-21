"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519998, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519998, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.184932, 'e_o_k': [0.222046, 0.177637, 0.142109, 0.113688], 'p_i': 10, 'u_i': 4.9967},
        {'id': 1, 'e_m': 9.709474, 'e_o_k': [1.193788, 0.955030, 0.764024], 'p_i': 20, 'u_i': 3.1686},
        {'id': 2, 'e_m': 1.605046, 'e_o_k': [0.197342, 0.157873, 0.126299], 'p_i': 40, 'u_i': 1.4833},
        {'id': 3, 'e_m': 14.251464, 'e_o_k': [1.158882, 0.927105, 0.741684, 0.593347, 0.474678, 0.379742], 'p_i': 80, 'u_i': 1.9048},
        {'id': 4, 'e_m': 0.548153, 'e_o_k': [0.091359, 0.073087], 'p_i': 40, 'u_i': 4.4078},
        {'id': 5, 'e_m': 0.276066, 'e_o_k': [0.033943, 0.027154, 0.021723], 'p_i': 10, 'u_i': 3.6020},
        {'id': 6, 'e_m': 7.924000, 'e_o_k': [0.805285, 0.644228, 0.515382, 0.412306], 'p_i': 40, 'u_i': 4.8789},
        {'id': 7, 'e_m': 0.383532, 'e_o_k': [0.038977, 0.031181, 0.024945, 0.019956], 'p_i': 10, 'u_i': 3.0372},
    ]
    B_BUDGET = 143.519998
    return processors, tasks, B_BUDGET
