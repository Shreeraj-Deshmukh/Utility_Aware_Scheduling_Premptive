"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.067880, 'e_o_k': [1.186488, 0.949191, 0.759353], 'p_i': 10, 'u_i': 2.1828},
        {'id': 1, 'e_m': 1.237267, 'e_o_k': [0.709907, 0.567926, 0.454341], 'p_i': 20, 'u_i': 3.4051},
        {'id': 2, 'e_m': 3.123831, 'e_o_k': [1.481492, 1.185193, 0.948155, 0.758524], 'p_i': 40, 'u_i': 2.6596},
        {'id': 3, 'e_m': 4.260232, 'e_o_k': [1.616664, 1.293331, 1.034665, 0.827732, 0.662185, 0.529748], 'p_i': 80, 'u_i': 2.1030},
    ]
    B_BUDGET = 88.320008
    return processors, tasks, B_BUDGET
