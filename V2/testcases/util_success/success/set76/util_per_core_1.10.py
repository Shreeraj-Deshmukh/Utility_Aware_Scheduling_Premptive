"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119994, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119994, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.689013, 'e_o_k': [0.453567, 0.362854, 0.290283], 'p_i': 10, 'u_i': 3.1129},
        {'id': 1, 'e_m': 7.762740, 'e_o_k': [0.692772, 0.554218, 0.443374, 0.354699, 0.283759], 'p_i': 20, 'u_i': 1.3211},
        {'id': 2, 'e_m': 19.646949, 'e_o_k': [3.274491, 2.619593], 'p_i': 40, 'u_i': 4.8977},
        {'id': 3, 'e_m': 24.011947, 'e_o_k': [4.001991, 3.201593], 'p_i': 80, 'u_i': 2.1715},
        {'id': 4, 'e_m': 7.872195, 'e_o_k': [0.967893, 0.774314, 0.619451], 'p_i': 20, 'u_i': 1.5264},
        {'id': 5, 'e_m': 0.346273, 'e_o_k': [0.057712, 0.046170], 'p_i': 40, 'u_i': 1.6618},
        {'id': 6, 'e_m': 1.871014, 'e_o_k': [0.166975, 0.133580, 0.106864, 0.085491, 0.068393], 'p_i': 20, 'u_i': 4.2147},
        {'id': 7, 'e_m': 6.232856, 'e_o_k': [1.038809, 0.831047], 'p_i': 40, 'u_i': 3.7475},
    ]
    B_BUDGET = 263.119994
    return processors, tasks, B_BUDGET
