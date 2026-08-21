"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.048710, 'e_o_k': [0.569086, 0.455269], 'p_i': 10, 'u_i': 3.2108},
        {'id': 1, 'e_m': 1.584179, 'e_o_k': [0.440050, 0.352040], 'p_i': 20, 'u_i': 1.2189},
        {'id': 2, 'e_m': 1.324389, 'e_o_k': [0.179492, 0.143593, 0.114875, 0.091900, 0.073520, 0.058816], 'p_i': 40, 'u_i': 1.4602},
        {'id': 3, 'e_m': 6.624827, 'e_o_k': [1.840230, 1.472184], 'p_i': 80, 'u_i': 2.5890},
    ]
    B_BUDGET = 55.200008
    return processors, tasks, B_BUDGET
