"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.235946, 'e_o_k': [0.167505, 0.134004, 0.107203, 0.085763, 0.068610, 0.054888], 'p_i': 10, 'u_i': 3.2393},
        {'id': 1, 'e_m': 2.190617, 'e_o_k': [0.296890, 0.237512, 0.190009, 0.152007, 0.121606, 0.097285], 'p_i': 20, 'u_i': 4.1852},
        {'id': 2, 'e_m': 10.772796, 'e_o_k': [1.824661, 1.459729, 1.167783, 0.934226], 'p_i': 40, 'u_i': 4.0538},
        {'id': 3, 'e_m': 23.804367, 'e_o_k': [4.031905, 3.225524, 2.580419, 2.064335], 'p_i': 80, 'u_i': 4.3622},
    ]
    B_BUDGET = 110.399995
    return processors, tasks, B_BUDGET
