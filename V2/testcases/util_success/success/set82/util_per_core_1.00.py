"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199997, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199997, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.224517, 'e_o_k': [0.377009, 0.301608, 0.241286, 0.193029, 0.154423], 'p_i': 10, 'u_i': 3.8434},
        {'id': 1, 'e_m': 0.887924, 'e_o_k': [0.147987, 0.118390], 'p_i': 20, 'u_i': 3.7460},
        {'id': 2, 'e_m': 7.167716, 'e_o_k': [0.728426, 0.582741, 0.466193, 0.372954], 'p_i': 40, 'u_i': 2.3844},
        {'id': 3, 'e_m': 8.744311, 'e_o_k': [1.457385, 1.165908], 'p_i': 80, 'u_i': 3.6397},
        {'id': 4, 'e_m': 34.575160, 'e_o_k': [2.811537, 2.249230, 1.799384, 1.439507, 1.151606, 0.921285], 'p_i': 80, 'u_i': 2.0089},
        {'id': 5, 'e_m': 7.753826, 'e_o_k': [0.787990, 0.630392, 0.504314, 0.403451], 'p_i': 20, 'u_i': 4.2973},
        {'id': 6, 'e_m': 0.555703, 'e_o_k': [0.092617, 0.074094], 'p_i': 10, 'u_i': 3.5880},
        {'id': 7, 'e_m': 7.384085, 'e_o_k': [0.600449, 0.480359, 0.384288, 0.307430, 0.245944, 0.196755], 'p_i': 20, 'u_i': 4.0384},
    ]
    B_BUDGET = 239.199997
    return processors, tasks, B_BUDGET
