"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 53.359991, "H": 80, "J": 31, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.9, "seed": 1032, "set": 32, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.90"}
"""

_SPEC = '{"B": 53.359991, "H": 80, "J": 31, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.9, "seed": 1032, "set": 32, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.507641, 'e_o_k': [0.075506, 0.060405, 0.048324, 0.038659, 0.030927], 'p_i': 10, 'u_i': 2.6437},
        {'id': 1, 'e_m': 0.669069, 'e_o_k': [0.090677, 0.072542, 0.058034, 0.046427, 0.037141, 0.029713], 'p_i': 20, 'u_i': 2.4707},
        {'id': 2, 'e_m': 0.607685, 'e_o_k': [0.082358, 0.065887, 0.052709, 0.042167, 0.033734, 0.026987], 'p_i': 40, 'u_i': 1.1046},
        {'id': 3, 'e_m': 5.713737, 'e_o_k': [1.587149, 1.269719], 'p_i': 80, 'u_i': 3.2848},
        {'id': 4, 'e_m': 2.096375, 'e_o_k': [0.355077, 0.284062, 0.227249, 0.181799], 'p_i': 40, 'u_i': 2.0063},
        {'id': 5, 'e_m': 0.270524, 'e_o_k': [0.045820, 0.036656, 0.029325, 0.023460], 'p_i': 10, 'u_i': 1.2869},
        {'id': 6, 'e_m': 2.830351, 'e_o_k': [0.786208, 0.628967], 'p_i': 20, 'u_i': 2.7193},
        {'id': 7, 'e_m': 0.327572, 'e_o_k': [0.090992, 0.072794], 'p_i': 40, 'u_i': 1.9085},
    ]
    B_BUDGET = 53.359991
    return processors, tasks, B_BUDGET
