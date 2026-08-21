"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.830835, 'e_o_k': [0.123577, 0.098862, 0.079089, 0.063272, 0.050617], 'p_i': 10, 'u_i': 3.1570},
        {'id': 1, 'e_m': 2.535383, 'e_o_k': [0.377109, 0.301688, 0.241350, 0.193080, 0.154464], 'p_i': 20, 'u_i': 1.1037},
        {'id': 2, 'e_m': 2.113969, 'e_o_k': [0.358057, 0.286446, 0.229157, 0.183325], 'p_i': 40, 'u_i': 1.2642},
        {'id': 3, 'e_m': 10.983853, 'e_o_k': [1.488617, 1.190894, 0.952715, 0.762172, 0.609738, 0.487790], 'p_i': 80, 'u_i': 2.8053},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
