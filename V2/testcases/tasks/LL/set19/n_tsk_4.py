"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.700833, 'e_o_k': [0.401718, 0.321375, 0.257100, 0.205680, 0.164544], 'p_i': 10, 'u_i': 3.4397},
        {'id': 1, 'e_m': 1.395832, 'e_o_k': [0.189174, 0.151339, 0.121071, 0.096857, 0.077486, 0.061989], 'p_i': 20, 'u_i': 4.9693},
        {'id': 2, 'e_m': 0.535278, 'e_o_k': [0.109688, 0.087751, 0.070200], 'p_i': 40, 'u_i': 4.4094},
        {'id': 3, 'e_m': 3.739453, 'e_o_k': [0.633376, 0.506701, 0.405361, 0.324289], 'p_i': 80, 'u_i': 4.1932},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
