"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640008, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640008, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.701313, 'e_o_k': [0.402393, 0.321914, 0.257531], 'p_i': 10, 'u_i': 4.4298},
        {'id': 1, 'e_m': 6.860890, 'e_o_k': [3.936576, 3.149261, 2.519409], 'p_i': 20, 'u_i': 1.5050},
        {'id': 2, 'e_m': 0.414599, 'e_o_k': [0.237885, 0.190308, 0.152246], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 3.429684, 'e_o_k': [1.967851, 1.574281, 1.259425], 'p_i': 80, 'u_i': 2.5958},
        {'id': 4, 'e_m': 1.398858, 'e_o_k': [0.802623, 0.642099, 0.513679], 'p_i': 20, 'u_i': 1.3643},
        {'id': 5, 'e_m': 5.494678, 'e_o_k': [3.152684, 2.522147, 2.017718], 'p_i': 80, 'u_i': 4.2904},
        {'id': 6, 'e_m': 5.102592, 'e_o_k': [2.927717, 2.342174, 1.873739], 'p_i': 40, 'u_i': 4.4714},
        {'id': 7, 'e_m': 5.391763, 'e_o_k': [3.093634, 2.474908, 1.979926], 'p_i': 80, 'u_i': 4.7028},
    ]
    B_BUDGET = 176.640008
    return processors, tasks, B_BUDGET
