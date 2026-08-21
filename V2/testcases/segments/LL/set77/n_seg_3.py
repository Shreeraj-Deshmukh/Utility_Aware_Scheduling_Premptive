"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.219693, 'e_o_k': [0.045019, 0.036015, 0.028812], 'p_i': 10, 'u_i': 3.0447},
        {'id': 1, 'e_m': 1.690611, 'e_o_k': [0.346437, 0.277149, 0.221719], 'p_i': 20, 'u_i': 2.1118},
        {'id': 2, 'e_m': 2.250553, 'e_o_k': [0.461179, 0.368943, 0.295155], 'p_i': 40, 'u_i': 4.2305},
        {'id': 3, 'e_m': 0.648336, 'e_o_k': [0.132856, 0.106285, 0.085028], 'p_i': 80, 'u_i': 2.0791},
        {'id': 4, 'e_m': 7.268970, 'e_o_k': [1.489543, 1.191634, 0.953308], 'p_i': 80, 'u_i': 1.4810},
        {'id': 5, 'e_m': 3.974108, 'e_o_k': [0.814366, 0.651493, 0.521194], 'p_i': 80, 'u_i': 3.5439},
        {'id': 6, 'e_m': 3.618059, 'e_o_k': [0.741406, 0.593124, 0.474500], 'p_i': 80, 'u_i': 1.8113},
        {'id': 7, 'e_m': 0.433679, 'e_o_k': [0.088869, 0.071095, 0.056876], 'p_i': 10, 'u_i': 4.9983},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
