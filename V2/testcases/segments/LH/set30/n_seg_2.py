"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.024511, 'e_o_k': [0.019064, 0.015251], 'p_i': 10, 'u_i': 1.0223},
        {'id': 1, 'e_m': 1.054701, 'e_o_k': [0.820323, 0.656258], 'p_i': 20, 'u_i': 1.6533},
        {'id': 2, 'e_m': 1.348573, 'e_o_k': [1.048890, 0.839112], 'p_i': 40, 'u_i': 4.3793},
        {'id': 3, 'e_m': 2.496489, 'e_o_k': [1.941714, 1.553371], 'p_i': 80, 'u_i': 2.7000},
        {'id': 4, 'e_m': 9.549774, 'e_o_k': [7.427602, 5.942081], 'p_i': 80, 'u_i': 2.7208},
        {'id': 5, 'e_m': 0.041493, 'e_o_k': [0.032273, 0.025818], 'p_i': 10, 'u_i': 2.5904},
        {'id': 6, 'e_m': 0.729370, 'e_o_k': [0.567288, 0.453830], 'p_i': 80, 'u_i': 1.1735},
        {'id': 7, 'e_m': 2.945096, 'e_o_k': [2.290630, 1.832504], 'p_i': 20, 'u_i': 1.5807},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET
