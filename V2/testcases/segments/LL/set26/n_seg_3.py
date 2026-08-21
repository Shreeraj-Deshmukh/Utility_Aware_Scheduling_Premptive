"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199997, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199997, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.630729, 'e_o_k': [0.334166, 0.267333, 0.213866], 'p_i': 10, 'u_i': 2.1780},
        {'id': 1, 'e_m': 0.554446, 'e_o_k': [0.113616, 0.090893, 0.072714], 'p_i': 20, 'u_i': 3.8388},
        {'id': 2, 'e_m': 1.443928, 'e_o_k': [0.295887, 0.236710, 0.189368], 'p_i': 40, 'u_i': 1.0041},
        {'id': 3, 'e_m': 3.915968, 'e_o_k': [0.802452, 0.641962, 0.513570], 'p_i': 80, 'u_i': 4.1994},
        {'id': 4, 'e_m': 0.833670, 'e_o_k': [0.170834, 0.136667, 0.109334], 'p_i': 40, 'u_i': 2.3676},
        {'id': 5, 'e_m': 0.367491, 'e_o_k': [0.075305, 0.060244, 0.048196], 'p_i': 10, 'u_i': 3.7622},
        {'id': 6, 'e_m': 0.185253, 'e_o_k': [0.037962, 0.030369, 0.024295], 'p_i': 10, 'u_i': 1.6504},
        {'id': 7, 'e_m': 3.843267, 'e_o_k': [0.787555, 0.630044, 0.504035], 'p_i': 80, 'u_i': 2.4020},
    ]
    B_BUDGET = 55.199997
    return processors, tasks, B_BUDGET
