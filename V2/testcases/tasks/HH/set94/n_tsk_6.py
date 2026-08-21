"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.918816, 'e_o_k': [0.714634, 0.571708], 'p_i': 10, 'u_i': 4.1192},
        {'id': 1, 'e_m': 1.455508, 'e_o_k': [0.690282, 0.552225, 0.441780, 0.353424], 'p_i': 20, 'u_i': 2.9903},
        {'id': 2, 'e_m': 7.213412, 'e_o_k': [3.420995, 2.736796, 2.189437, 1.751549], 'p_i': 40, 'u_i': 3.9277},
        {'id': 3, 'e_m': 11.236205, 'e_o_k': [4.679524, 3.743619, 2.994895, 2.395916, 1.916733], 'p_i': 80, 'u_i': 2.3920},
        {'id': 4, 'e_m': 1.039177, 'e_o_k': [0.492835, 0.394268, 0.315414, 0.252331], 'p_i': 40, 'u_i': 2.2588},
        {'id': 5, 'e_m': 23.086059, 'e_o_k': [17.955824, 14.364659], 'p_i': 80, 'u_i': 4.0829},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
