"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.52, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.52, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.664836, 'e_o_k': [0.054062, 0.043250, 0.034600, 0.027680, 0.022144, 0.017715], 'p_i': 10, 'u_i': 3.7777},
        {'id': 1, 'e_m': 0.577555, 'e_o_k': [0.051543, 0.041234, 0.032987, 0.026390, 0.021112], 'p_i': 20, 'u_i': 2.9102},
        {'id': 2, 'e_m': 10.780428, 'e_o_k': [1.095572, 0.876458, 0.701166, 0.560933], 'p_i': 40, 'u_i': 3.0744},
        {'id': 3, 'e_m': 30.931068, 'e_o_k': [5.155178, 4.124142], 'p_i': 80, 'u_i': 3.1102},
        {'id': 4, 'e_m': 2.177310, 'e_o_k': [0.177052, 0.141641, 0.113313, 0.090650, 0.072520, 0.058016], 'p_i': 20, 'u_i': 3.9746},
        {'id': 5, 'e_m': 2.019450, 'e_o_k': [0.248293, 0.198634, 0.158908], 'p_i': 10, 'u_i': 1.5757},
        {'id': 6, 'e_m': 3.101906, 'e_o_k': [0.381382, 0.305105, 0.244084], 'p_i': 40, 'u_i': 4.9941},
        {'id': 7, 'e_m': 2.405260, 'e_o_k': [0.400877, 0.320701], 'p_i': 40, 'u_i': 1.7632},
    ]
    B_BUDGET = 143.520000
    return processors, tasks, B_BUDGET
