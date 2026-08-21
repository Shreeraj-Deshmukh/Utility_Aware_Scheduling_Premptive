"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199991, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199991, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.389062, 'e_o_k': [0.108073, 0.086458], 'p_i': 10, 'u_i': 1.2652},
        {'id': 1, 'e_m': 0.895639, 'e_o_k': [0.248789, 0.199031], 'p_i': 20, 'u_i': 2.8552},
        {'id': 2, 'e_m': 0.010963, 'e_o_k': [0.003045, 0.002436], 'p_i': 40, 'u_i': 3.5059},
        {'id': 3, 'e_m': 4.905019, 'e_o_k': [1.362505, 1.090004], 'p_i': 80, 'u_i': 1.7742},
        {'id': 4, 'e_m': 8.853066, 'e_o_k': [2.459185, 1.967348], 'p_i': 40, 'u_i': 1.4108},
        {'id': 5, 'e_m': 0.037049, 'e_o_k': [0.010291, 0.008233], 'p_i': 40, 'u_i': 2.2719},
        {'id': 6, 'e_m': 1.507728, 'e_o_k': [0.418813, 0.335051], 'p_i': 80, 'u_i': 4.1261},
        {'id': 7, 'e_m': 1.090040, 'e_o_k': [0.302789, 0.242231], 'p_i': 80, 'u_i': 2.8820},
    ]
    B_BUDGET = 55.199991
    return processors, tasks, B_BUDGET
