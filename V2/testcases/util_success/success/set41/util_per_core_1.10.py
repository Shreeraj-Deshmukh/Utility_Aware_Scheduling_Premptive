"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120002, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120002, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.263179, 'e_o_k': [0.401210, 0.320968, 0.256775], 'p_i': 10, 'u_i': 3.2904},
        {'id': 1, 'e_m': 1.041570, 'e_o_k': [0.128062, 0.102450, 0.081960], 'p_i': 20, 'u_i': 1.8156},
        {'id': 2, 'e_m': 18.506003, 'e_o_k': [1.651535, 1.321228, 1.056983, 0.845586, 0.676469], 'p_i': 40, 'u_i': 1.9365},
        {'id': 3, 'e_m': 2.417310, 'e_o_k': [0.297210, 0.237768, 0.190215], 'p_i': 80, 'u_i': 2.3606},
        {'id': 4, 'e_m': 7.631583, 'e_o_k': [0.775567, 0.620454, 0.496363, 0.397091], 'p_i': 40, 'u_i': 2.6705},
        {'id': 5, 'e_m': 34.816497, 'e_o_k': [4.280717, 3.424574, 2.739659], 'p_i': 80, 'u_i': 4.9899},
        {'id': 6, 'e_m': 5.161609, 'e_o_k': [0.460639, 0.368511, 0.294809, 0.235847, 0.188678], 'p_i': 20, 'u_i': 3.2939},
        {'id': 7, 'e_m': 17.786435, 'e_o_k': [1.446334, 1.157067, 0.925654, 0.740523, 0.592418, 0.473935], 'p_i': 40, 'u_i': 2.4697},
    ]
    B_BUDGET = 263.120002
    return processors, tasks, B_BUDGET
