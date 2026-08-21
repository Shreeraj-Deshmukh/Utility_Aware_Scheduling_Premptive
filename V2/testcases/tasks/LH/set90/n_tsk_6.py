"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319993, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319993, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.586040, 'e_o_k': [0.455809, 0.364647], 'p_i': 10, 'u_i': 3.4053},
        {'id': 1, 'e_m': 1.423539, 'e_o_k': [0.675120, 0.540096, 0.432077, 0.345662], 'p_i': 20, 'u_i': 3.7246},
        {'id': 2, 'e_m': 1.290688, 'e_o_k': [0.612115, 0.489692, 0.391754, 0.313403], 'p_i': 40, 'u_i': 3.7938},
        {'id': 3, 'e_m': 0.607687, 'e_o_k': [0.230604, 0.184483, 0.147586, 0.118069, 0.094455, 0.075564], 'p_i': 80, 'u_i': 1.4474},
        {'id': 4, 'e_m': 0.622404, 'e_o_k': [0.259212, 0.207369, 0.165895, 0.132716, 0.106173], 'p_i': 10, 'u_i': 3.1824},
        {'id': 5, 'e_m': 13.449227, 'e_o_k': [5.103684, 4.082947, 3.266358, 2.613086, 2.090469, 1.672375], 'p_i': 80, 'u_i': 3.3367},
    ]
    B_BUDGET = 88.319993
    return processors, tasks, B_BUDGET
