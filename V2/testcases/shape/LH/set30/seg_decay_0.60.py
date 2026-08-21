"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320013, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.320013, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.024511, 'e_o_k': [0.017508, 0.010505, 0.006303], 'p_i': 10, 'u_i': 1.0223},
        {'id': 1, 'e_m': 1.054701, 'e_o_k': [0.619538, 0.371723, 0.223034, 0.133820, 0.080292, 0.048175], 'p_i': 20, 'u_i': 1.5905},
        {'id': 2, 'e_m': 1.348573, 'e_o_k': [1.180002, 0.708001], 'p_i': 40, 'u_i': 4.0467},
        {'id': 3, 'e_m': 2.496489, 'e_o_k': [1.606197, 0.963718, 0.578231, 0.346939], 'p_i': 80, 'u_i': 4.3793},
        {'id': 4, 'e_m': 9.549774, 'e_o_k': [6.144156, 3.686493, 2.211896, 1.327138], 'p_i': 80, 'u_i': 2.7000},
        {'id': 5, 'e_m': 0.041493, 'e_o_k': [0.026696, 0.016018, 0.009611, 0.005766], 'p_i': 10, 'u_i': 2.7208},
        {'id': 6, 'e_m': 0.729370, 'e_o_k': [0.469264, 0.281558, 0.168935, 0.101361], 'p_i': 80, 'u_i': 2.5904},
        {'id': 7, 'e_m': 2.945096, 'e_o_k': [2.103640, 1.262184, 0.757310], 'p_i': 20, 'u_i': 1.1735},
    ]
    B_BUDGET = 88.320013
    return processors, tasks, B_BUDGET
