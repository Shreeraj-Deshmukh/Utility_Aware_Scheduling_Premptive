"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.849593, 'e_o_k': [0.126367, 0.101094, 0.080875, 0.064700, 0.051760], 'p_i': 10, 'u_i': 2.2469},
        {'id': 1, 'e_m': 2.065527, 'e_o_k': [0.307224, 0.245779, 0.196623, 0.157299, 0.125839], 'p_i': 20, 'u_i': 2.3819},
        {'id': 2, 'e_m': 0.036634, 'e_o_k': [0.006205, 0.004964, 0.003971, 0.003177], 'p_i': 40, 'u_i': 2.4700},
        {'id': 3, 'e_m': 16.867879, 'e_o_k': [2.508906, 2.007125, 1.605700, 1.284560, 1.027648], 'p_i': 80, 'u_i': 2.1021},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET
