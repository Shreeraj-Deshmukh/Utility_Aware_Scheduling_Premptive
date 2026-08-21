"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.355596, 'e_o_k': [0.148095, 0.118476, 0.094781, 0.075824, 0.060660], 'p_i': 10, 'u_i': 3.8879},
        {'id': 1, 'e_m': 7.765711, 'e_o_k': [2.946915, 2.357532, 1.886026, 1.508821, 1.207057, 0.965645], 'p_i': 20, 'u_i': 3.5961},
        {'id': 2, 'e_m': 1.313886, 'e_o_k': [0.547192, 0.437754, 0.350203, 0.280162, 0.224130], 'p_i': 40, 'u_i': 4.1247},
        {'id': 3, 'e_m': 1.954973, 'e_o_k': [1.121706, 0.897365, 0.717892], 'p_i': 80, 'u_i': 3.4312},
        {'id': 4, 'e_m': 23.181270, 'e_o_k': [18.029877, 14.423901], 'p_i': 80, 'u_i': 1.1226},
        {'id': 5, 'e_m': 0.582092, 'e_o_k': [0.242423, 0.193938, 0.155151, 0.124120, 0.099296], 'p_i': 20, 'u_i': 3.8598},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
