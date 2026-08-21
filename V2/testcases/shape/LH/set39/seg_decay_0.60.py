"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319995, "H": 80, "J": 35, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319995, "H": 80, "J": 35, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.217662, 'e_o_k': [0.190455, 0.114273], 'p_i': 10, 'u_i': 1.4412},
        {'id': 1, 'e_m': 1.846208, 'e_o_k': [1.187818, 0.712691, 0.427614, 0.256569], 'p_i': 20, 'u_i': 3.7136},
        {'id': 2, 'e_m': 0.830898, 'e_o_k': [0.488074, 0.292845, 0.175707, 0.105424, 0.063254, 0.037953], 'p_i': 40, 'u_i': 3.0715},
        {'id': 3, 'e_m': 10.940022, 'e_o_k': [6.426235, 3.855741, 2.313445, 1.388067, 0.832840, 0.499704], 'p_i': 80, 'u_i': 2.1053},
        {'id': 4, 'e_m': 0.087893, 'e_o_k': [0.076907, 0.046144], 'p_i': 20, 'u_i': 3.9261},
        {'id': 5, 'e_m': 0.266000, 'e_o_k': [0.232750, 0.139650], 'p_i': 20, 'u_i': 2.2961},
        {'id': 6, 'e_m': 0.085726, 'e_o_k': [0.052054, 0.031232, 0.018739, 0.011244, 0.006746], 'p_i': 10, 'u_i': 1.3761},
        {'id': 7, 'e_m': 2.042668, 'e_o_k': [1.459048, 0.875429, 0.525257], 'p_i': 20, 'u_i': 2.1930},
    ]
    B_BUDGET = 88.319995
    return processors, tasks, B_BUDGET
