"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680006, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680006, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.149966, 'e_o_k': [0.174828, 0.139863, 0.111890, 0.089512, 0.071610, 0.057288], 'p_i': 10, 'u_i': 3.5232},
        {'id': 1, 'e_m': 0.415795, 'e_o_k': [0.069299, 0.055439], 'p_i': 20, 'u_i': 1.0606},
        {'id': 2, 'e_m': 1.011654, 'e_o_k': [0.102810, 0.082248, 0.065799, 0.052639], 'p_i': 40, 'u_i': 3.4010},
        {'id': 3, 'e_m': 23.962531, 'e_o_k': [1.948553, 1.558843, 1.247074, 0.997659, 0.798127, 0.638502], 'p_i': 80, 'u_i': 4.8241},
        {'id': 4, 'e_m': 1.255643, 'e_o_k': [0.127606, 0.102085, 0.081668, 0.065334], 'p_i': 40, 'u_i': 1.6455},
        {'id': 5, 'e_m': 6.392981, 'e_o_k': [0.649693, 0.519755, 0.415804, 0.332643], 'p_i': 40, 'u_i': 1.3745},
        {'id': 6, 'e_m': 1.712311, 'e_o_k': [0.210530, 0.168424, 0.134739], 'p_i': 40, 'u_i': 1.5038},
        {'id': 7, 'e_m': 0.107345, 'e_o_k': [0.013198, 0.010559, 0.008447], 'p_i': 20, 'u_i': 4.4242},
    ]
    B_BUDGET = 95.680006
    return processors, tasks, B_BUDGET
