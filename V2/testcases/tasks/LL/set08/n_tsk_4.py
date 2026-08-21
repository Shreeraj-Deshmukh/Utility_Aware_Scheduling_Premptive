"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.783783, 'e_o_k': [0.217717, 0.174174], 'p_i': 10, 'u_i': 1.2013},
        {'id': 1, 'e_m': 0.135220, 'e_o_k': [0.027709, 0.022167, 0.017734], 'p_i': 20, 'u_i': 4.4940},
        {'id': 2, 'e_m': 8.308601, 'e_o_k': [1.126046, 0.900837, 0.720670, 0.576536, 0.461229, 0.368983], 'p_i': 40, 'u_i': 4.9438},
        {'id': 3, 'e_m': 8.571659, 'e_o_k': [1.161698, 0.929358, 0.743487, 0.594789, 0.475832, 0.380665], 'p_i': 80, 'u_i': 2.3791},
    ]
    B_BUDGET = 55.200005
    return processors, tasks, B_BUDGET
