"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.116204, 'e_o_k': [0.055110, 0.044088, 0.035271, 0.028217], 'p_i': 10, 'u_i': 4.2389},
        {'id': 1, 'e_m': 0.594557, 'e_o_k': [0.247614, 0.198091, 0.158473, 0.126778, 0.101423], 'p_i': 20, 'u_i': 4.7607},
        {'id': 2, 'e_m': 4.754990, 'e_o_k': [2.255076, 1.804061, 1.443249, 1.154599], 'p_i': 40, 'u_i': 3.2703},
        {'id': 3, 'e_m': 19.182159, 'e_o_k': [11.006157, 8.804925, 7.043940], 'p_i': 80, 'u_i': 4.5676},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET
