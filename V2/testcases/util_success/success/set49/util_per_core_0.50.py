"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599983, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599983, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.749047, 'e_o_k': [0.142227, 0.113781, 0.091025, 0.072820, 0.058256, 0.046605], 'p_i': 10, 'u_i': 3.0661},
        {'id': 1, 'e_m': 4.114800, 'e_o_k': [0.334602, 0.267682, 0.214145, 0.171316, 0.137053, 0.109642], 'p_i': 20, 'u_i': 2.9486},
        {'id': 2, 'e_m': 14.089946, 'e_o_k': [2.348324, 1.878660], 'p_i': 40, 'u_i': 3.9206},
        {'id': 3, 'e_m': 8.949020, 'e_o_k': [0.909453, 0.727563, 0.582050, 0.465640], 'p_i': 80, 'u_i': 3.4151},
        {'id': 4, 'e_m': 2.019429, 'e_o_k': [0.205227, 0.164181, 0.131345, 0.105076], 'p_i': 40, 'u_i': 2.3956},
        {'id': 5, 'e_m': 4.682516, 'e_o_k': [0.417883, 0.334306, 0.267445, 0.213956, 0.171165], 'p_i': 80, 'u_i': 3.6029},
        {'id': 6, 'e_m': 0.365831, 'e_o_k': [0.037178, 0.029742, 0.023794, 0.019035], 'p_i': 10, 'u_i': 4.4783},
        {'id': 7, 'e_m': 0.385740, 'e_o_k': [0.064290, 0.051432], 'p_i': 40, 'u_i': 1.4735},
    ]
    B_BUDGET = 119.599983
    return processors, tasks, B_BUDGET
