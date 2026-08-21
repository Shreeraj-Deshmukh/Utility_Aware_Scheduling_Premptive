"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199994, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.199994, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.389062, 'e_o_k': [0.089399, 0.053639, 0.032183, 0.019310], 'p_i': 10, 'u_i': 1.2652},
        {'id': 1, 'e_m': 0.895639, 'e_o_k': [0.187894, 0.112737, 0.067642, 0.040585, 0.024351, 0.014611], 'p_i': 20, 'u_i': 2.0660},
        {'id': 2, 'e_m': 0.010963, 'e_o_k': [0.003426, 0.002056], 'p_i': 40, 'u_i': 3.5059},
        {'id': 3, 'e_m': 4.905019, 'e_o_k': [1.251280, 0.750768, 0.450461], 'p_i': 80, 'u_i': 1.7742},
        {'id': 4, 'e_m': 8.853066, 'e_o_k': [2.258435, 1.355061, 0.813037], 'p_i': 40, 'u_i': 1.4108},
        {'id': 5, 'e_m': 0.037049, 'e_o_k': [0.008513, 0.005108, 0.003065, 0.001839], 'p_i': 40, 'u_i': 2.2719},
        {'id': 6, 'e_m': 1.507728, 'e_o_k': [0.326971, 0.196182, 0.117709, 0.070626, 0.042375], 'p_i': 80, 'u_i': 4.1261},
        {'id': 7, 'e_m': 1.090040, 'e_o_k': [0.250469, 0.150281, 0.090169, 0.054101], 'p_i': 80, 'u_i': 2.8820},
    ]
    B_BUDGET = 55.199994
    return processors, tasks, B_BUDGET
