"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280001, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280001, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.715637, 'e_o_k': [0.119273, 0.095418], 'p_i': 10, 'u_i': 1.8047},
        {'id': 1, 'e_m': 5.484716, 'e_o_k': [0.914119, 0.731295], 'p_i': 20, 'u_i': 1.0945},
        {'id': 2, 'e_m': 4.481064, 'e_o_k': [0.399905, 0.319924, 0.255939, 0.204751, 0.163801], 'p_i': 40, 'u_i': 2.4137},
        {'id': 3, 'e_m': 24.164385, 'e_o_k': [4.027397, 3.221918], 'p_i': 80, 'u_i': 1.6729},
        {'id': 4, 'e_m': 4.133198, 'e_o_k': [0.336098, 0.268878, 0.215103, 0.172082, 0.137666, 0.110133], 'p_i': 40, 'u_i': 2.8481},
        {'id': 5, 'e_m': 3.831583, 'e_o_k': [0.389389, 0.311511, 0.249209, 0.199367], 'p_i': 10, 'u_i': 3.6691},
        {'id': 6, 'e_m': 6.435983, 'e_o_k': [0.654063, 0.523251, 0.418601, 0.334880], 'p_i': 20, 'u_i': 3.0767},
        {'id': 7, 'e_m': 18.546530, 'e_o_k': [1.508142, 1.206514, 0.965211, 0.772169, 0.617735, 0.494188], 'p_i': 80, 'u_i': 1.7471},
    ]
    B_BUDGET = 215.280001
    return processors, tasks, B_BUDGET
