"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639994, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 176.639994, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.049022, 'e_o_k': [0.022877, 0.022877, 0.022877], 'p_i': 10, 'u_i': 1.0223},
        {'id': 1, 'e_m': 2.109402, 'e_o_k': [0.492194, 0.492194, 0.492194, 0.492194, 0.492194, 0.492194], 'p_i': 20, 'u_i': 1.5905},
        {'id': 2, 'e_m': 2.697147, 'e_o_k': [1.888003, 1.888003], 'p_i': 40, 'u_i': 4.0467},
        {'id': 3, 'e_m': 4.992978, 'e_o_k': [1.747542, 1.747542, 1.747542, 1.747542], 'p_i': 80, 'u_i': 4.3793},
        {'id': 4, 'e_m': 19.099547, 'e_o_k': [6.684842, 6.684842, 6.684842, 6.684842], 'p_i': 80, 'u_i': 2.7000},
        {'id': 5, 'e_m': 0.082986, 'e_o_k': [0.029045, 0.029045, 0.029045, 0.029045], 'p_i': 10, 'u_i': 2.7208},
        {'id': 6, 'e_m': 1.458740, 'e_o_k': [0.510559, 0.510559, 0.510559, 0.510559], 'p_i': 80, 'u_i': 2.5904},
        {'id': 7, 'e_m': 5.890191, 'e_o_k': [2.748756, 2.748756, 2.748756], 'p_i': 20, 'u_i': 1.1735},
    ]
    B_BUDGET = 176.639994
    return processors, tasks, B_BUDGET
