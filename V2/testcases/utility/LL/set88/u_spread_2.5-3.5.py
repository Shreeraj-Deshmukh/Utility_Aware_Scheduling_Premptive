"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200012, "H": 80, "J": 29, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "utility", "util_per_core": 0.2, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 55.200012, "H": 80, "J": 29, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "utility", "util_per_core": 0.2, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.343272, 'e_o_k': [0.070343, 0.056274, 0.045019], 'p_i': 10, 'u_i': 3.1397},
        {'id': 1, 'e_m': 0.791370, 'e_o_k': [0.219825, 0.175860], 'p_i': 20, 'u_i': 2.5219},
        {'id': 2, 'e_m': 2.553569, 'e_o_k': [0.432515, 0.346012, 0.276810, 0.221448], 'p_i': 40, 'u_i': 2.9862},
        {'id': 3, 'e_m': 0.112895, 'e_o_k': [0.019122, 0.015297, 0.012238, 0.009790], 'p_i': 80, 'u_i': 2.8822},
        {'id': 4, 'e_m': 5.014202, 'e_o_k': [0.745806, 0.596645, 0.477316, 0.381853, 0.305482], 'p_i': 40, 'u_i': 2.9735},
        {'id': 5, 'e_m': 2.695419, 'e_o_k': [0.365304, 0.292243, 0.233795, 0.187036, 0.149629, 0.119703], 'p_i': 40, 'u_i': 3.3904},
        {'id': 6, 'e_m': 0.133194, 'e_o_k': [0.036998, 0.029599], 'p_i': 10, 'u_i': 3.2297},
        {'id': 7, 'e_m': 2.191761, 'e_o_k': [0.371233, 0.296987, 0.237589, 0.190071], 'p_i': 40, 'u_i': 2.7836},
    ]
    B_BUDGET = 55.200012
    return processors, tasks, B_BUDGET
