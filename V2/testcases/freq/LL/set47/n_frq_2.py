"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.19999, "H": 80, "J": 41, "factor": "n_frq", "n_frq": 2, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "freq", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.19999, "H": 80, "J": 41, "factor": "n_frq", "n_frq": 2, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "freq", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 1.0]},
        {'id': 1, 'frequencies': [0.4, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.216718, 'e_o_k': [0.180973, 0.144778, 0.115823, 0.092658, 0.074127], 'p_i': 10, 'u_i': 3.4259},
        {'id': 1, 'e_m': 0.839332, 'e_o_k': [0.142163, 0.113731, 0.090985, 0.072788], 'p_i': 20, 'u_i': 1.3819},
        {'id': 2, 'e_m': 1.348859, 'e_o_k': [0.374683, 0.299746], 'p_i': 40, 'u_i': 1.7445},
        {'id': 3, 'e_m': 2.791709, 'e_o_k': [0.378354, 0.302683, 0.242147, 0.193717, 0.154974, 0.123979], 'p_i': 80, 'u_i': 3.6642},
        {'id': 4, 'e_m': 0.479983, 'e_o_k': [0.081298, 0.065038, 0.052031, 0.041625], 'p_i': 10, 'u_i': 2.6174},
        {'id': 5, 'e_m': 0.600183, 'e_o_k': [0.089270, 0.071416, 0.057133, 0.045706, 0.036565], 'p_i': 10, 'u_i': 2.3254},
        {'id': 6, 'e_m': 0.097664, 'e_o_k': [0.027129, 0.021703], 'p_i': 10, 'u_i': 3.2626},
        {'id': 7, 'e_m': 1.998429, 'e_o_k': [0.297244, 0.237795, 0.190236, 0.152189, 0.121751], 'p_i': 40, 'u_i': 1.6837},
    ]
    B_BUDGET = 55.199990
    return processors, tasks, B_BUDGET
