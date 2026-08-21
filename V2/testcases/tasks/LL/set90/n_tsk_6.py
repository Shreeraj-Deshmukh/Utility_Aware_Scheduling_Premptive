"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.586040, 'e_o_k': [0.162789, 0.130231], 'p_i': 10, 'u_i': 3.4053},
        {'id': 1, 'e_m': 1.423539, 'e_o_k': [0.241114, 0.192892, 0.154313, 0.123451], 'p_i': 20, 'u_i': 3.7246},
        {'id': 2, 'e_m': 1.290688, 'e_o_k': [0.218613, 0.174890, 0.139912, 0.111930], 'p_i': 40, 'u_i': 3.7938},
        {'id': 3, 'e_m': 0.607687, 'e_o_k': [0.082358, 0.065887, 0.052709, 0.042168, 0.033734, 0.026987], 'p_i': 80, 'u_i': 1.4474},
        {'id': 4, 'e_m': 0.622404, 'e_o_k': [0.092576, 0.074060, 0.059248, 0.047399, 0.037919], 'p_i': 10, 'u_i': 3.1824},
        {'id': 5, 'e_m': 13.449227, 'e_o_k': [1.822744, 1.458195, 1.166556, 0.933245, 0.746596, 0.597277], 'p_i': 80, 'u_i': 3.3367},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
