"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439984, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439984, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.102657, 'e_o_k': [0.170981, 0.136785, 0.109428, 0.087542, 0.070034, 0.056027], 'p_i': 10, 'u_i': 2.8402},
        {'id': 1, 'e_m': 2.324709, 'e_o_k': [0.189038, 0.151230, 0.120984, 0.096787, 0.077430, 0.061944], 'p_i': 20, 'u_i': 1.6917},
        {'id': 2, 'e_m': 5.191533, 'e_o_k': [0.463309, 0.370647, 0.296518, 0.237214, 0.189771], 'p_i': 40, 'u_i': 1.6028},
        {'id': 3, 'e_m': 33.038086, 'e_o_k': [4.062060, 3.249648, 2.599718], 'p_i': 80, 'u_i': 2.5090},
        {'id': 4, 'e_m': 3.059257, 'e_o_k': [0.376138, 0.300911, 0.240728], 'p_i': 40, 'u_i': 2.5667},
        {'id': 5, 'e_m': 8.309440, 'e_o_k': [0.844455, 0.675564, 0.540451, 0.432361], 'p_i': 40, 'u_i': 2.7205},
        {'id': 6, 'e_m': 0.236360, 'e_o_k': [0.024020, 0.019216, 0.015373, 0.012298], 'p_i': 10, 'u_i': 1.7673},
        {'id': 7, 'e_m': 2.228810, 'e_o_k': [0.274034, 0.219227, 0.175382], 'p_i': 10, 'u_i': 2.9380},
    ]
    B_BUDGET = 167.439984
    return processors, tasks, B_BUDGET
