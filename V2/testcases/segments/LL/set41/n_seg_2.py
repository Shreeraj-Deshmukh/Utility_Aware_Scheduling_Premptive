"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200011, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200011, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.439041, 'e_o_k': [0.121956, 0.097565], 'p_i': 10, 'u_i': 1.3531},
        {'id': 1, 'e_m': 0.880194, 'e_o_k': [0.244498, 0.195599], 'p_i': 20, 'u_i': 2.6488},
        {'id': 2, 'e_m': 7.606803, 'e_o_k': [2.113001, 1.690401], 'p_i': 40, 'u_i': 4.8206},
        {'id': 3, 'e_m': 0.610708, 'e_o_k': [0.169641, 0.135713], 'p_i': 80, 'u_i': 3.3334},
        {'id': 4, 'e_m': 0.933835, 'e_o_k': [0.259399, 0.207519], 'p_i': 20, 'u_i': 2.1081},
        {'id': 5, 'e_m': 0.975572, 'e_o_k': [0.270992, 0.216794], 'p_i': 20, 'u_i': 1.8691},
        {'id': 6, 'e_m': 0.921104, 'e_o_k': [0.255862, 0.204690], 'p_i': 80, 'u_i': 3.0834},
        {'id': 7, 'e_m': 0.583852, 'e_o_k': [0.162181, 0.129745], 'p_i': 80, 'u_i': 3.6806},
    ]
    B_BUDGET = 55.200011
    return processors, tasks, B_BUDGET
