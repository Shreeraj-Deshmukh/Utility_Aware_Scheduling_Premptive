"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.210650, 'e_o_k': [0.205056, 0.164045, 0.131236, 0.104989], 'p_i': 10, 'u_i': 4.8908},
        {'id': 1, 'e_m': 1.270017, 'e_o_k': [0.188901, 0.151121, 0.120896, 0.096717, 0.077374], 'p_i': 20, 'u_i': 3.7143},
        {'id': 2, 'e_m': 2.460196, 'e_o_k': [0.365926, 0.292741, 0.234193, 0.187354, 0.149883], 'p_i': 40, 'u_i': 4.3200},
        {'id': 3, 'e_m': 12.314336, 'e_o_k': [1.668935, 1.335148, 1.068118, 0.854495, 0.683596, 0.546877], 'p_i': 80, 'u_i': 3.1069},
    ]
    B_BUDGET = 55.200003
    return processors, tasks, B_BUDGET
