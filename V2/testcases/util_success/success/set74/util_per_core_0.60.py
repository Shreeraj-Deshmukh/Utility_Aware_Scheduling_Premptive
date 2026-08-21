"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520014, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520014, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.356660, 'e_o_k': [0.031829, 0.025464, 0.020371, 0.016297, 0.013037], 'p_i': 10, 'u_i': 4.9795},
        {'id': 1, 'e_m': 3.454794, 'e_o_k': [0.424770, 0.339816, 0.271853], 'p_i': 20, 'u_i': 4.9448},
        {'id': 2, 'e_m': 11.351156, 'e_o_k': [1.013014, 0.810411, 0.648329, 0.518663, 0.414930], 'p_i': 40, 'u_i': 4.4554},
        {'id': 3, 'e_m': 30.139555, 'e_o_k': [2.689751, 2.151801, 1.721441, 1.377152, 1.101722], 'p_i': 80, 'u_i': 2.2591},
        {'id': 4, 'e_m': 0.329358, 'e_o_k': [0.040495, 0.032396, 0.025917], 'p_i': 10, 'u_i': 2.7803},
        {'id': 5, 'e_m': 14.958776, 'e_o_k': [1.216398, 0.973118, 0.778495, 0.622796, 0.498237, 0.398589], 'p_i': 80, 'u_i': 3.4160},
        {'id': 6, 'e_m': 4.660507, 'e_o_k': [0.573013, 0.458411, 0.366728], 'p_i': 80, 'u_i': 3.4712},
        {'id': 7, 'e_m': 1.057883, 'e_o_k': [0.094409, 0.075527, 0.060422, 0.048337, 0.038670], 'p_i': 20, 'u_i': 4.3322},
    ]
    B_BUDGET = 143.520014
    return processors, tasks, B_BUDGET
