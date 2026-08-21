"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199985, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199985, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.908996, 'e_o_k': [0.432680, 0.346144, 0.276915, 0.221532, 0.177226], 'p_i': 10, 'u_i': 1.8764},
        {'id': 1, 'e_m': 0.104544, 'e_o_k': [0.014169, 0.011335, 0.009068, 0.007254, 0.005803, 0.004643], 'p_i': 20, 'u_i': 4.1968},
        {'id': 2, 'e_m': 1.907409, 'e_o_k': [0.283705, 0.226964, 0.181571, 0.145257, 0.116206], 'p_i': 40, 'u_i': 4.4928},
        {'id': 3, 'e_m': 4.495037, 'e_o_k': [0.609202, 0.487362, 0.389890, 0.311912, 0.249529, 0.199623], 'p_i': 80, 'u_i': 4.0915},
    ]
    B_BUDGET = 55.199985
    return processors, tasks, B_BUDGET
