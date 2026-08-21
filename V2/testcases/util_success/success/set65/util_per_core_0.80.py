"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359995, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359995, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.255615, 'e_o_k': [0.025977, 0.020782, 0.016625, 0.013300], 'p_i': 10, 'u_i': 3.7146},
        {'id': 1, 'e_m': 9.276574, 'e_o_k': [1.140562, 0.912450, 0.729960], 'p_i': 20, 'u_i': 2.7971},
        {'id': 2, 'e_m': 1.601580, 'e_o_k': [0.196916, 0.157532, 0.126026], 'p_i': 40, 'u_i': 1.6396},
        {'id': 3, 'e_m': 18.875721, 'e_o_k': [2.320785, 1.856628, 1.485303], 'p_i': 80, 'u_i': 4.1445},
        {'id': 4, 'e_m': 6.966258, 'e_o_k': [0.707953, 0.566362, 0.453090, 0.362472], 'p_i': 20, 'u_i': 4.6205},
        {'id': 5, 'e_m': 29.047273, 'e_o_k': [2.362028, 1.889622, 1.511698, 1.209358, 0.967487, 0.773989], 'p_i': 80, 'u_i': 1.3665},
        {'id': 6, 'e_m': 0.146711, 'e_o_k': [0.014910, 0.011928, 0.009542, 0.007634], 'p_i': 20, 'u_i': 3.3652},
        {'id': 7, 'e_m': 2.317689, 'e_o_k': [0.206838, 0.165470, 0.132376, 0.105901, 0.084721], 'p_i': 20, 'u_i': 2.1692},
    ]
    B_BUDGET = 191.359995
    return processors, tasks, B_BUDGET
