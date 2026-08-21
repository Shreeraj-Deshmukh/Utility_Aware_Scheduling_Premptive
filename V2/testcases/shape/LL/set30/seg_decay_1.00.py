"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200008, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.200008, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.024511, 'e_o_k': [0.004085, 0.004085, 0.004085], 'p_i': 10, 'u_i': 1.0223},
        {'id': 1, 'e_m': 1.054701, 'e_o_k': [0.087892, 0.087892, 0.087892, 0.087892, 0.087892, 0.087892], 'p_i': 20, 'u_i': 1.5905},
        {'id': 2, 'e_m': 1.348573, 'e_o_k': [0.337143, 0.337143], 'p_i': 40, 'u_i': 4.0467},
        {'id': 3, 'e_m': 2.496489, 'e_o_k': [0.312061, 0.312061, 0.312061, 0.312061], 'p_i': 80, 'u_i': 4.3793},
        {'id': 4, 'e_m': 9.549774, 'e_o_k': [1.193722, 1.193722, 1.193722, 1.193722], 'p_i': 80, 'u_i': 2.7000},
        {'id': 5, 'e_m': 0.041493, 'e_o_k': [0.005187, 0.005187, 0.005187, 0.005187], 'p_i': 10, 'u_i': 2.7208},
        {'id': 6, 'e_m': 0.729370, 'e_o_k': [0.091171, 0.091171, 0.091171, 0.091171], 'p_i': 80, 'u_i': 2.5904},
        {'id': 7, 'e_m': 2.945096, 'e_o_k': [0.490849, 0.490849, 0.490849], 'p_i': 20, 'u_i': 1.1735},
    ]
    B_BUDGET = 55.200008
    return processors, tasks, B_BUDGET
