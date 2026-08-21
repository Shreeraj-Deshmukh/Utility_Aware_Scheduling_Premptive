"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400005, "H": 80, "J": 33, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 110.400005, "H": 80, "J": 33, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.150064, 'e_o_k': [0.291393, 0.233115, 0.186492, 0.149193, 0.119355, 0.095484], 'p_i': 10, 'u_i': 3.2148},
        {'id': 1, 'e_m': 0.276887, 'e_o_k': [0.041184, 0.032947, 0.026358, 0.021086, 0.016869], 'p_i': 20, 'u_i': 3.1746},
        {'id': 2, 'e_m': 1.036903, 'e_o_k': [0.154228, 0.123382, 0.098706, 0.078965, 0.063172], 'p_i': 40, 'u_i': 3.0168},
        {'id': 3, 'e_m': 0.261660, 'e_o_k': [0.072683, 0.058147], 'p_i': 80, 'u_i': 2.8137},
        {'id': 4, 'e_m': 12.654356, 'e_o_k': [3.515099, 2.812079], 'p_i': 80, 'u_i': 3.0907},
        {'id': 5, 'e_m': 0.168799, 'e_o_k': [0.046889, 0.037511], 'p_i': 10, 'u_i': 2.7358},
        {'id': 6, 'e_m': 2.612506, 'e_o_k': [0.388581, 0.310865, 0.248692, 0.198953, 0.159163], 'p_i': 80, 'u_i': 3.3095},
        {'id': 7, 'e_m': 3.342402, 'e_o_k': [0.684918, 0.547935, 0.438348], 'p_i': 10, 'u_i': 2.6421},
    ]
    B_BUDGET = 110.400005
    return processors, tasks, B_BUDGET
