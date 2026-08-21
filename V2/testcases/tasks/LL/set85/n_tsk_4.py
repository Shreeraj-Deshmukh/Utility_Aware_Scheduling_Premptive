"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.546811, 'e_o_k': [0.074108, 0.059287, 0.047429, 0.037943, 0.030355, 0.024284], 'p_i': 10, 'u_i': 4.7125},
        {'id': 1, 'e_m': 1.198359, 'e_o_k': [0.202974, 0.162379, 0.129903, 0.103923], 'p_i': 20, 'u_i': 3.2766},
        {'id': 2, 'e_m': 3.939056, 'e_o_k': [1.094182, 0.875346], 'p_i': 40, 'u_i': 2.3226},
        {'id': 3, 'e_m': 14.953960, 'e_o_k': [4.153878, 3.323102], 'p_i': 80, 'u_i': 1.3159},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET
