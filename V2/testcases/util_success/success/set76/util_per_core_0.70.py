"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440006, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440006, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.347553, 'e_o_k': [0.288634, 0.230907, 0.184726], 'p_i': 10, 'u_i': 3.1129},
        {'id': 1, 'e_m': 4.939926, 'e_o_k': [0.440855, 0.352684, 0.282147, 0.225718, 0.180574], 'p_i': 20, 'u_i': 1.3211},
        {'id': 2, 'e_m': 12.502604, 'e_o_k': [2.083767, 1.667014], 'p_i': 40, 'u_i': 4.8977},
        {'id': 3, 'e_m': 15.280330, 'e_o_k': [2.546722, 2.037377], 'p_i': 80, 'u_i': 2.1715},
        {'id': 4, 'e_m': 5.009578, 'e_o_k': [0.615932, 0.492745, 0.394196], 'p_i': 20, 'u_i': 1.5264},
        {'id': 5, 'e_m': 0.220355, 'e_o_k': [0.036726, 0.029381], 'p_i': 40, 'u_i': 1.6618},
        {'id': 6, 'e_m': 1.190645, 'e_o_k': [0.106257, 0.085006, 0.068005, 0.054404, 0.043523], 'p_i': 20, 'u_i': 4.2147},
        {'id': 7, 'e_m': 3.966363, 'e_o_k': [0.661060, 0.528848], 'p_i': 40, 'u_i': 3.7475},
    ]
    B_BUDGET = 167.440006
    return processors, tasks, B_BUDGET
