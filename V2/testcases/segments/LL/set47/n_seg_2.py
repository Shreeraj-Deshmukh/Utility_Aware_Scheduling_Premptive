"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200002, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200002, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.216718, 'e_o_k': [0.337977, 0.270382], 'p_i': 10, 'u_i': 3.4259},
        {'id': 1, 'e_m': 0.839332, 'e_o_k': [0.233148, 0.186518], 'p_i': 20, 'u_i': 1.3819},
        {'id': 2, 'e_m': 1.348859, 'e_o_k': [0.374683, 0.299746], 'p_i': 40, 'u_i': 1.7445},
        {'id': 3, 'e_m': 2.791709, 'e_o_k': [0.775475, 0.620380], 'p_i': 80, 'u_i': 2.0127},
        {'id': 4, 'e_m': 0.479983, 'e_o_k': [0.133329, 0.106663], 'p_i': 10, 'u_i': 4.7864},
        {'id': 5, 'e_m': 0.600183, 'e_o_k': [0.166718, 0.133374], 'p_i': 10, 'u_i': 1.7550},
        {'id': 6, 'e_m': 0.097664, 'e_o_k': [0.027129, 0.021703], 'p_i': 10, 'u_i': 2.9364},
        {'id': 7, 'e_m': 1.998429, 'e_o_k': [0.555119, 0.444095], 'p_i': 40, 'u_i': 1.0429},
    ]
    B_BUDGET = 55.200002
    return processors, tasks, B_BUDGET
