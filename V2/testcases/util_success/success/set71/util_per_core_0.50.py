"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600011, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600011, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.687458, 'e_o_k': [0.218535, 0.174828, 0.139863, 0.111890, 0.089512, 0.071610], 'p_i': 10, 'u_i': 3.5232},
        {'id': 1, 'e_m': 0.519744, 'e_o_k': [0.086624, 0.069299], 'p_i': 20, 'u_i': 1.0606},
        {'id': 2, 'e_m': 1.264568, 'e_o_k': [0.128513, 0.102810, 0.082248, 0.065799], 'p_i': 40, 'u_i': 3.4010},
        {'id': 3, 'e_m': 29.953164, 'e_o_k': [2.435692, 1.948553, 1.558843, 1.247074, 0.997659, 0.798127], 'p_i': 80, 'u_i': 4.8241},
        {'id': 4, 'e_m': 1.569553, 'e_o_k': [0.159507, 0.127606, 0.102085, 0.081668], 'p_i': 40, 'u_i': 1.6455},
        {'id': 5, 'e_m': 7.991226, 'e_o_k': [0.812116, 0.649693, 0.519755, 0.415804], 'p_i': 40, 'u_i': 1.3745},
        {'id': 6, 'e_m': 2.140389, 'e_o_k': [0.263163, 0.210530, 0.168424], 'p_i': 40, 'u_i': 1.5038},
        {'id': 7, 'e_m': 0.134182, 'e_o_k': [0.016498, 0.013198, 0.010559], 'p_i': 20, 'u_i': 4.4242},
    ]
    B_BUDGET = 119.600011
    return processors, tasks, B_BUDGET
