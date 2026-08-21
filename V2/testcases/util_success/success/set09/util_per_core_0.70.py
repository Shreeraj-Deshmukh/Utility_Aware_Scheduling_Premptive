"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439998, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439998, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.040148, 'e_o_k': [0.506691, 0.405353], 'p_i': 10, 'u_i': 1.8132},
        {'id': 1, 'e_m': 2.474612, 'e_o_k': [0.201227, 0.160982, 0.128785, 0.103028, 0.082423, 0.065938], 'p_i': 20, 'u_i': 1.3118},
        {'id': 2, 'e_m': 15.566183, 'e_o_k': [1.389176, 1.111341, 0.889073, 0.711258, 0.569007], 'p_i': 40, 'u_i': 1.6432},
        {'id': 3, 'e_m': 6.986561, 'e_o_k': [1.164427, 0.931542], 'p_i': 80, 'u_i': 3.2827},
        {'id': 4, 'e_m': 0.273038, 'e_o_k': [0.024367, 0.019493, 0.015595, 0.012476, 0.009981], 'p_i': 20, 'u_i': 1.0597},
        {'id': 5, 'e_m': 0.616310, 'e_o_k': [0.075776, 0.060621, 0.048497], 'p_i': 20, 'u_i': 4.4596},
        {'id': 6, 'e_m': 8.972404, 'e_o_k': [0.911830, 0.729464, 0.583571, 0.466857], 'p_i': 40, 'u_i': 4.8824},
        {'id': 7, 'e_m': 2.269905, 'e_o_k': [0.279087, 0.223269, 0.178615], 'p_i': 10, 'u_i': 1.5609},
    ]
    B_BUDGET = 167.439998
    return processors, tasks, B_BUDGET
