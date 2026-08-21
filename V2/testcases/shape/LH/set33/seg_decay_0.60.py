"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320001, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.320001, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.024096, 'e_o_k': [0.017212, 0.010327, 0.006196], 'p_i': 10, 'u_i': 4.1859},
        {'id': 1, 'e_m': 1.824026, 'e_o_k': [1.302875, 0.781725, 0.469035], 'p_i': 20, 'u_i': 1.3758},
        {'id': 2, 'e_m': 2.806108, 'e_o_k': [2.004363, 1.202618, 0.721571], 'p_i': 40, 'u_i': 3.6848},
        {'id': 3, 'e_m': 0.481622, 'e_o_k': [0.421419, 0.252852], 'p_i': 80, 'u_i': 1.6851},
        {'id': 4, 'e_m': 2.721725, 'e_o_k': [1.652678, 0.991607, 0.594964, 0.356979, 0.214187], 'p_i': 20, 'u_i': 1.3700},
        {'id': 5, 'e_m': 0.681310, 'e_o_k': [0.413703, 0.248222, 0.148933, 0.089360, 0.053616], 'p_i': 10, 'u_i': 3.3252},
        {'id': 6, 'e_m': 0.612959, 'e_o_k': [0.536339, 0.321804], 'p_i': 80, 'u_i': 4.3008},
        {'id': 7, 'e_m': 1.466951, 'e_o_k': [0.943810, 0.566286, 0.339772, 0.203863], 'p_i': 80, 'u_i': 2.2362},
    ]
    B_BUDGET = 88.320001
    return processors, tasks, B_BUDGET
