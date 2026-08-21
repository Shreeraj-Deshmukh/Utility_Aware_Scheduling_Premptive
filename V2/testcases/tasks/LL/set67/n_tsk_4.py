"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.020282, 'e_o_k': [0.409332, 0.327466, 0.261973, 0.209578, 0.167662, 0.134130], 'p_i': 10, 'u_i': 2.2803},
        {'id': 1, 'e_m': 0.067315, 'e_o_k': [0.010012, 0.008010, 0.006408, 0.005126, 0.004101], 'p_i': 20, 'u_i': 3.0147},
        {'id': 2, 'e_m': 3.120452, 'e_o_k': [0.528532, 0.422825, 0.338260, 0.270608], 'p_i': 40, 'u_i': 1.8147},
        {'id': 3, 'e_m': 1.327580, 'e_o_k': [0.224861, 0.179889, 0.143911, 0.115129], 'p_i': 80, 'u_i': 2.7697},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET
