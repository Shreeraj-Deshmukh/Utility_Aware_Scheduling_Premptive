"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.389062, 'e_o_k': [0.250316, 0.150190, 0.090114, 0.054068], 'p_i': 10, 'u_i': 1.2652},
        {'id': 1, 'e_m': 0.895639, 'e_o_k': [0.526104, 0.315662, 0.189397, 0.113638, 0.068183, 0.040910], 'p_i': 20, 'u_i': 2.0660},
        {'id': 2, 'e_m': 0.010963, 'e_o_k': [0.009593, 0.005756], 'p_i': 40, 'u_i': 3.5059},
        {'id': 3, 'e_m': 4.905019, 'e_o_k': [3.503585, 2.102151, 1.261291], 'p_i': 80, 'u_i': 1.7742},
        {'id': 4, 'e_m': 8.853066, 'e_o_k': [6.323618, 3.794171, 2.276503], 'p_i': 40, 'u_i': 1.4108},
        {'id': 5, 'e_m': 0.037049, 'e_o_k': [0.023837, 0.014302, 0.008581, 0.005149], 'p_i': 40, 'u_i': 2.2719},
        {'id': 6, 'e_m': 1.507728, 'e_o_k': [0.915518, 0.549311, 0.329587, 0.197752, 0.118651], 'p_i': 80, 'u_i': 4.1261},
        {'id': 7, 'e_m': 1.090040, 'e_o_k': [0.701313, 0.420788, 0.252473, 0.151484], 'p_i': 80, 'u_i': 2.8820},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
