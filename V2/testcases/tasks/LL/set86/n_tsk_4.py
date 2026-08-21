"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.116204, 'e_o_k': [0.019682, 0.015746, 0.012597, 0.010077], 'p_i': 10, 'u_i': 4.2389},
        {'id': 1, 'e_m': 0.594557, 'e_o_k': [0.088434, 0.070747, 0.056598, 0.045278, 0.036222], 'p_i': 20, 'u_i': 4.7607},
        {'id': 2, 'e_m': 4.754990, 'e_o_k': [0.805384, 0.644308, 0.515446, 0.412357], 'p_i': 40, 'u_i': 3.2703},
        {'id': 3, 'e_m': 19.182159, 'e_o_k': [3.930770, 3.144616, 2.515693], 'p_i': 80, 'u_i': 4.5676},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
