"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320014, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.320014, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.389062, 'e_o_k': [0.136172, 0.136172, 0.136172, 0.136172], 'p_i': 10, 'u_i': 1.2652},
        {'id': 1, 'e_m': 0.895639, 'e_o_k': [0.208983, 0.208983, 0.208983, 0.208983, 0.208983, 0.208983], 'p_i': 20, 'u_i': 2.0660},
        {'id': 2, 'e_m': 0.010963, 'e_o_k': [0.007674, 0.007674], 'p_i': 40, 'u_i': 3.5059},
        {'id': 3, 'e_m': 4.905019, 'e_o_k': [2.289009, 2.289009, 2.289009], 'p_i': 80, 'u_i': 1.7742},
        {'id': 4, 'e_m': 8.853066, 'e_o_k': [4.131431, 4.131431, 4.131431], 'p_i': 40, 'u_i': 1.4108},
        {'id': 5, 'e_m': 0.037049, 'e_o_k': [0.012967, 0.012967, 0.012967, 0.012967], 'p_i': 40, 'u_i': 2.2719},
        {'id': 6, 'e_m': 1.507728, 'e_o_k': [0.422164, 0.422164, 0.422164, 0.422164, 0.422164], 'p_i': 80, 'u_i': 4.1261},
        {'id': 7, 'e_m': 1.090040, 'e_o_k': [0.381514, 0.381514, 0.381514, 0.381514], 'p_i': 80, 'u_i': 2.8820},
    ]
    B_BUDGET = 88.320014
    return processors, tasks, B_BUDGET
