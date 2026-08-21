"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320001, "H": 80, "J": 40, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.320001, "H": 80, "J": 40, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.629540, 'e_o_k': [0.489642, 0.391714], 'p_i': 10, 'u_i': 2.8729},
        {'id': 1, 'e_m': 1.955326, 'e_o_k': [1.520809, 1.216647], 'p_i': 20, 'u_i': 4.4646},
        {'id': 2, 'e_m': 0.277667, 'e_o_k': [0.215963, 0.172771], 'p_i': 40, 'u_i': 2.8456},
        {'id': 3, 'e_m': 2.558681, 'e_o_k': [1.990085, 1.592068], 'p_i': 80, 'u_i': 4.6357},
        {'id': 4, 'e_m': 0.415486, 'e_o_k': [0.323156, 0.258525], 'p_i': 10, 'u_i': 3.1275},
        {'id': 5, 'e_m': 6.998742, 'e_o_k': [5.443466, 4.354773], 'p_i': 80, 'u_i': 2.7677},
        {'id': 6, 'e_m': 0.663543, 'e_o_k': [0.516089, 0.412871], 'p_i': 10, 'u_i': 2.2237},
        {'id': 7, 'e_m': 0.049673, 'e_o_k': [0.038635, 0.030908], 'p_i': 10, 'u_i': 3.7702},
    ]
    B_BUDGET = 88.320001
    return processors, tasks, B_BUDGET
