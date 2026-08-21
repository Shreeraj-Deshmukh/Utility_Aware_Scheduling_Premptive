"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320007, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.320007, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.529710, 'e_o_k': [0.535399, 0.535399, 0.535399, 0.535399], 'p_i': 10, 'u_i': 1.9017},
        {'id': 1, 'e_m': 1.119012, 'e_o_k': [0.783308, 0.783308], 'p_i': 20, 'u_i': 4.1004},
        {'id': 2, 'e_m': 0.375318, 'e_o_k': [0.131361, 0.131361, 0.131361, 0.131361], 'p_i': 40, 'u_i': 2.6358},
        {'id': 3, 'e_m': 2.653251, 'e_o_k': [1.238184, 1.238184, 1.238184], 'p_i': 80, 'u_i': 4.3577},
        {'id': 4, 'e_m': 0.027963, 'e_o_k': [0.009787, 0.009787, 0.009787, 0.009787], 'p_i': 40, 'u_i': 4.2383},
        {'id': 5, 'e_m': 0.045505, 'e_o_k': [0.012741, 0.012741, 0.012741, 0.012741, 0.012741], 'p_i': 80, 'u_i': 1.1754},
        {'id': 6, 'e_m': 9.092843, 'e_o_k': [6.364990, 6.364990], 'p_i': 80, 'u_i': 2.9766},
        {'id': 7, 'e_m': 1.344054, 'e_o_k': [0.313613, 0.313613, 0.313613, 0.313613, 0.313613, 0.313613], 'p_i': 40, 'u_i': 4.8798},
    ]
    B_BUDGET = 88.320007
    return processors, tasks, B_BUDGET
