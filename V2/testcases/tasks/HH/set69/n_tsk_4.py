"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.281523, 'e_o_k': [0.486310, 0.389048, 0.311238, 0.248990, 0.199192, 0.159354], 'p_i': 10, 'u_i': 1.7448},
        {'id': 1, 'e_m': 4.014414, 'e_o_k': [1.671876, 1.337501, 1.070001, 0.856001, 0.684801], 'p_i': 20, 'u_i': 2.9486},
        {'id': 2, 'e_m': 17.639969, 'e_o_k': [7.346489, 5.877191, 4.701753, 3.761402, 3.009122], 'p_i': 40, 'u_i': 1.5908},
        {'id': 3, 'e_m': 2.410225, 'e_o_k': [1.003782, 0.803026, 0.642421, 0.513937, 0.411149], 'p_i': 80, 'u_i': 1.2188},
    ]
    B_BUDGET = 176.640009
    return processors, tasks, B_BUDGET
