"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639999, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639999, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.659774, 'e_o_k': [2.846491, 2.277193], 'p_i': 10, 'u_i': 4.8131},
        {'id': 1, 'e_m': 3.615342, 'e_o_k': [1.505675, 1.204540, 0.963632, 0.770906, 0.616725], 'p_i': 20, 'u_i': 1.8577},
        {'id': 2, 'e_m': 2.245523, 'e_o_k': [1.288415, 1.030732, 0.824586], 'p_i': 40, 'u_i': 4.0468},
        {'id': 3, 'e_m': 3.223826, 'e_o_k': [1.342621, 1.074097, 0.859278, 0.687422, 0.549938], 'p_i': 80, 'u_i': 2.5682},
        {'id': 4, 'e_m': 9.283514, 'e_o_k': [3.522888, 2.818310, 2.254648, 1.803718, 1.442975, 1.154380], 'p_i': 80, 'u_i': 1.7800},
        {'id': 5, 'e_m': 0.407757, 'e_o_k': [0.154735, 0.123788, 0.099030, 0.079224, 0.063379, 0.050703], 'p_i': 10, 'u_i': 2.6825},
    ]
    B_BUDGET = 176.639999
    return processors, tasks, B_BUDGET
