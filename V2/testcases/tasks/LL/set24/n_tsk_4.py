"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199979, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199979, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.291296, 'e_o_k': [0.039479, 0.031583, 0.025266, 0.020213, 0.016170, 0.012936], 'p_i': 10, 'u_i': 1.4017},
        {'id': 1, 'e_m': 2.259781, 'e_o_k': [0.306263, 0.245011, 0.196008, 0.156807, 0.125445, 0.100356], 'p_i': 20, 'u_i': 2.4636},
        {'id': 2, 'e_m': 6.298206, 'e_o_k': [1.066769, 0.853415, 0.682732, 0.546186], 'p_i': 40, 'u_i': 2.5536},
        {'id': 3, 'e_m': 8.034092, 'e_o_k': [2.231692, 1.785354], 'p_i': 80, 'u_i': 3.8458},
    ]
    B_BUDGET = 55.199979
    return processors, tasks, B_BUDGET
