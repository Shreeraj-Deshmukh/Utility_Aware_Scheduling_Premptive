"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.283614, 'e_o_k': [0.309493, 0.247595, 0.198076, 0.158461, 0.126768, 0.101415], 'p_i': 10, 'u_i': 1.6837},
        {'id': 1, 'e_m': 4.288893, 'e_o_k': [1.191359, 0.953087], 'p_i': 20, 'u_i': 2.3942},
        {'id': 2, 'e_m': 9.305656, 'e_o_k': [1.384111, 1.107289, 0.885831, 0.708665, 0.566932], 'p_i': 40, 'u_i': 1.1399},
        {'id': 3, 'e_m': 9.964201, 'e_o_k': [1.350426, 1.080341, 0.864273, 0.691418, 0.553135, 0.442508], 'p_i': 80, 'u_i': 4.6324},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET
