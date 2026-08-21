"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520001, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520001, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.098857, 'e_o_k': [0.170672, 0.136538, 0.109230, 0.087384, 0.069907, 0.055926], 'p_i': 10, 'u_i': 3.0661},
        {'id': 1, 'e_m': 4.937760, 'e_o_k': [0.401522, 0.321218, 0.256974, 0.205579, 0.164464, 0.131571], 'p_i': 20, 'u_i': 2.9486},
        {'id': 2, 'e_m': 16.907936, 'e_o_k': [2.817989, 2.254391], 'p_i': 40, 'u_i': 3.9206},
        {'id': 3, 'e_m': 10.738824, 'e_o_k': [1.091344, 0.873075, 0.698460, 0.558768], 'p_i': 80, 'u_i': 3.4151},
        {'id': 4, 'e_m': 2.423315, 'e_o_k': [0.246272, 0.197017, 0.157614, 0.126091], 'p_i': 40, 'u_i': 2.3956},
        {'id': 5, 'e_m': 5.619019, 'e_o_k': [0.501459, 0.401167, 0.320934, 0.256747, 0.205398], 'p_i': 80, 'u_i': 3.6029},
        {'id': 6, 'e_m': 0.438998, 'e_o_k': [0.044614, 0.035691, 0.028553, 0.022842], 'p_i': 10, 'u_i': 4.4783},
        {'id': 7, 'e_m': 0.462888, 'e_o_k': [0.077148, 0.061718], 'p_i': 40, 'u_i': 1.4735},
    ]
    B_BUDGET = 143.520001
    return processors, tasks, B_BUDGET
