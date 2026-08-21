"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199997, "H": 80, "J": 33, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "utility", "util_per_core": 0.2, "value": "1.0-5.0"}
"""

_SPEC = '{"B": 55.199997, "H": 80, "J": 33, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "utility", "util_per_core": 0.2, "value": "1.0-5.0"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.056307, 'e_o_k': [0.011538, 0.009231, 0.007385], 'p_i': 10, 'u_i': 4.5768},
        {'id': 1, 'e_m': 0.343444, 'e_o_k': [0.095401, 0.076321], 'p_i': 20, 'u_i': 3.5463},
        {'id': 2, 'e_m': 1.086388, 'e_o_k': [0.301774, 0.241420], 'p_i': 40, 'u_i': 3.4252},
        {'id': 3, 'e_m': 2.157450, 'e_o_k': [0.365422, 0.292337, 0.233870, 0.187096], 'p_i': 80, 'u_i': 1.2792},
        {'id': 4, 'e_m': 0.190372, 'e_o_k': [0.032245, 0.025796, 0.020637, 0.016509], 'p_i': 10, 'u_i': 2.1862},
        {'id': 5, 'e_m': 4.007311, 'e_o_k': [0.821170, 0.656936, 0.525549], 'p_i': 80, 'u_i': 2.5645},
        {'id': 6, 'e_m': 1.096980, 'e_o_k': [0.185803, 0.148642, 0.118914, 0.095131], 'p_i': 10, 'u_i': 2.2998},
        {'id': 7, 'e_m': 11.539405, 'e_o_k': [2.364632, 1.891706, 1.513365], 'p_i': 80, 'u_i': 1.4896},
    ]
    B_BUDGET = 55.199997
    return processors, tasks, B_BUDGET
