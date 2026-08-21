"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.32002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.285319, 'e_o_k': [0.535295, 0.428236, 0.342589, 0.274071, 0.219257], 'p_i': 10, 'u_i': 2.3680},
        {'id': 1, 'e_m': 1.739923, 'e_o_k': [1.353274, 1.082619], 'p_i': 20, 'u_i': 4.2120},
        {'id': 2, 'e_m': 2.896760, 'e_o_k': [2.253035, 1.802428], 'p_i': 40, 'u_i': 4.4653},
        {'id': 3, 'e_m': 8.964238, 'e_o_k': [6.972185, 5.577748], 'p_i': 80, 'u_i': 4.6069},
    ]
    B_BUDGET = 88.320020
    return processors, tasks, B_BUDGET
