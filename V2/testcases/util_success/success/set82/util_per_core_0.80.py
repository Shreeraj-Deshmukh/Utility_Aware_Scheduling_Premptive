"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359993, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359993, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.379613, 'e_o_k': [0.301608, 0.241286, 0.193029, 0.154423, 0.123538], 'p_i': 10, 'u_i': 3.8434},
        {'id': 1, 'e_m': 0.710339, 'e_o_k': [0.118390, 0.094712], 'p_i': 20, 'u_i': 3.7460},
        {'id': 2, 'e_m': 5.734173, 'e_o_k': [0.582741, 0.466193, 0.372954, 0.298363], 'p_i': 40, 'u_i': 2.3844},
        {'id': 3, 'e_m': 6.995448, 'e_o_k': [1.165908, 0.932726], 'p_i': 80, 'u_i': 3.6397},
        {'id': 4, 'e_m': 27.660128, 'e_o_k': [2.249230, 1.799384, 1.439507, 1.151606, 0.921285, 0.737028], 'p_i': 80, 'u_i': 2.0089},
        {'id': 5, 'e_m': 6.203061, 'e_o_k': [0.630392, 0.504314, 0.403451, 0.322761], 'p_i': 20, 'u_i': 4.2973},
        {'id': 6, 'e_m': 0.444562, 'e_o_k': [0.074094, 0.059275], 'p_i': 10, 'u_i': 3.5880},
        {'id': 7, 'e_m': 5.907268, 'e_o_k': [0.480359, 0.384288, 0.307430, 0.245944, 0.196755, 0.157404], 'p_i': 20, 'u_i': 4.0384},
    ]
    B_BUDGET = 191.359993
    return processors, tasks, B_BUDGET
