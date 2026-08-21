"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.760654, 'e_o_k': [0.360744, 0.288595, 0.230876, 0.184701], 'p_i': 10, 'u_i': 3.1389},
        {'id': 1, 'e_m': 3.743173, 'e_o_k': [1.420451, 1.136361, 0.909089, 0.727271, 0.581817, 0.465453], 'p_i': 20, 'u_i': 2.7195},
        {'id': 2, 'e_m': 4.127417, 'e_o_k': [1.718938, 1.375151, 1.100121, 0.880097, 0.704077], 'p_i': 40, 'u_i': 2.3377},
        {'id': 3, 'e_m': 2.687240, 'e_o_k': [2.090076, 1.672060], 'p_i': 80, 'u_i': 4.2462},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET
