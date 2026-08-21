"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.533781, 'e_o_k': [0.115757, 0.069454, 0.041673, 0.025004, 0.015002], 'p_i': 10, 'u_i': 4.6830},
        {'id': 1, 'e_m': 3.051801, 'e_o_k': [0.953688, 0.572213], 'p_i': 20, 'u_i': 2.4027},
        {'id': 2, 'e_m': 2.268878, 'e_o_k': [0.709024, 0.425415], 'p_i': 40, 'u_i': 2.7203},
        {'id': 3, 'e_m': 2.027473, 'e_o_k': [0.425339, 0.255204, 0.153122, 0.091873, 0.055124, 0.033074], 'p_i': 80, 'u_i': 2.4000},
        {'id': 4, 'e_m': 0.174589, 'e_o_k': [0.054559, 0.032735], 'p_i': 20, 'u_i': 2.9059},
        {'id': 5, 'e_m': 0.345496, 'e_o_k': [0.088137, 0.052882, 0.031729], 'p_i': 10, 'u_i': 3.1411},
        {'id': 6, 'e_m': 2.718295, 'e_o_k': [0.624608, 0.374765, 0.224859, 0.134915], 'p_i': 80, 'u_i': 3.1206},
        {'id': 7, 'e_m': 1.388352, 'e_o_k': [0.354171, 0.212503, 0.127502], 'p_i': 40, 'u_i': 4.7030},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
