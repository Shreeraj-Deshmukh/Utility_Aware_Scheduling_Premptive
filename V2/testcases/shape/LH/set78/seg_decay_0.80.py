"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320008, "H": 80, "J": 26, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "shape", "util_per_core": 0.2, "value": "0.80"}
"""

_SPEC = '{"B": 88.320008, "H": 80, "J": 26, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "shape", "util_per_core": 0.2, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.143220, 'e_o_k': [0.542178, 0.433742, 0.346994, 0.277595], 'p_i': 10, 'u_i': 1.7025},
        {'id': 1, 'e_m': 0.721620, 'e_o_k': [0.300532, 0.240426, 0.192340, 0.153872, 0.123098], 'p_i': 20, 'u_i': 2.0058},
        {'id': 2, 'e_m': 0.561215, 'e_o_k': [0.436501, 0.349200], 'p_i': 40, 'u_i': 3.5722},
        {'id': 3, 'e_m': 9.907138, 'e_o_k': [4.698507, 3.758806, 3.007045, 2.405636], 'p_i': 80, 'u_i': 1.2384},
        {'id': 4, 'e_m': 0.924900, 'e_o_k': [0.719367, 0.575493], 'p_i': 40, 'u_i': 4.5379},
        {'id': 5, 'e_m': 1.311382, 'e_o_k': [1.019964, 0.815971], 'p_i': 20, 'u_i': 1.9982},
        {'id': 6, 'e_m': 0.152759, 'e_o_k': [0.118813, 0.095050], 'p_i': 20, 'u_i': 2.1252},
        {'id': 7, 'e_m': 1.231826, 'e_o_k': [0.584199, 0.467360, 0.373888, 0.299110], 'p_i': 80, 'u_i': 4.2384},
    ]
    B_BUDGET = 88.320008
    return processors, tasks, B_BUDGET
