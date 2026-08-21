"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.024511, 'e_o_k': [0.006253, 0.003752, 0.002251], 'p_i': 10, 'u_i': 1.0223},
        {'id': 1, 'e_m': 1.054701, 'e_o_k': [0.221263, 0.132758, 0.079655, 0.047793, 0.028676, 0.017205], 'p_i': 20, 'u_i': 1.5905},
        {'id': 2, 'e_m': 1.348573, 'e_o_k': [0.421429, 0.252857], 'p_i': 40, 'u_i': 4.0467},
        {'id': 3, 'e_m': 2.496489, 'e_o_k': [0.573642, 0.344185, 0.206511, 0.123907], 'p_i': 80, 'u_i': 4.3793},
        {'id': 4, 'e_m': 9.549774, 'e_o_k': [2.194341, 1.316605, 0.789963, 0.473978], 'p_i': 80, 'u_i': 2.7000},
        {'id': 5, 'e_m': 0.041493, 'e_o_k': [0.009534, 0.005721, 0.003432, 0.002059], 'p_i': 10, 'u_i': 2.7208},
        {'id': 6, 'e_m': 0.729370, 'e_o_k': [0.167594, 0.100557, 0.060334, 0.036200], 'p_i': 80, 'u_i': 2.5904},
        {'id': 7, 'e_m': 2.945096, 'e_o_k': [0.751300, 0.450780, 0.270468], 'p_i': 20, 'u_i': 1.1735},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET
