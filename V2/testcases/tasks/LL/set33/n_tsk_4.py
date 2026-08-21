"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199992, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199992, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.055999, 'e_o_k': [0.015555, 0.012444], 'p_i': 10, 'u_i': 3.5447},
        {'id': 1, 'e_m': 4.278233, 'e_o_k': [0.876687, 0.701350, 0.561080], 'p_i': 20, 'u_i': 1.0370},
        {'id': 2, 'e_m': 5.252208, 'e_o_k': [0.781207, 0.624965, 0.499972, 0.399978, 0.319982], 'p_i': 40, 'u_i': 1.6130},
        {'id': 3, 'e_m': 3.934656, 'e_o_k': [0.806282, 0.645026, 0.516021], 'p_i': 80, 'u_i': 1.3758},
    ]
    B_BUDGET = 55.199992
    return processors, tasks, B_BUDGET
