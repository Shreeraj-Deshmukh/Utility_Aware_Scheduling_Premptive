"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.63999, "H": 80, "J": 29, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 176.63999, "H": 80, "J": 29, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.049022, 'e_o_k': [0.028127, 0.022502, 0.018002], 'p_i': 10, 'u_i': 1.5167},
        {'id': 1, 'e_m': 2.109402, 'e_o_k': [0.800471, 0.640377, 0.512302, 0.409841, 0.327873, 0.262298], 'p_i': 20, 'u_i': 1.9429},
        {'id': 2, 'e_m': 2.697147, 'e_o_k': [2.097781, 1.678225], 'p_i': 40, 'u_i': 3.7850},
        {'id': 3, 'e_m': 4.992978, 'e_o_k': [2.367944, 1.894355, 1.515484, 1.212387], 'p_i': 80, 'u_i': 4.0345},
        {'id': 4, 'e_m': 19.099547, 'e_o_k': [9.058051, 7.246441, 5.797153, 4.637722], 'p_i': 80, 'u_i': 2.7750},
        {'id': 5, 'e_m': 0.082986, 'e_o_k': [0.039357, 0.031485, 0.025188, 0.020151], 'p_i': 10, 'u_i': 2.7906},
        {'id': 6, 'e_m': 1.458740, 'e_o_k': [0.691814, 0.553451, 0.442761, 0.354209], 'p_i': 80, 'u_i': 2.6928},
        {'id': 7, 'e_m': 5.890191, 'e_o_k': [3.379618, 2.703694, 2.162955], 'p_i': 20, 'u_i': 1.6301},
    ]
    B_BUDGET = 176.639990
    return processors, tasks, B_BUDGET
