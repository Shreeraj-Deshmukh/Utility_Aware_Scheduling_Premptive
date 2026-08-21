"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200003, "H": 80, "J": 40, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200003, "H": 80, "J": 40, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.629540, 'e_o_k': [0.129004, 0.103203, 0.082563], 'p_i': 10, 'u_i': 2.8729},
        {'id': 1, 'e_m': 1.955326, 'e_o_k': [0.400682, 0.320545, 0.256436], 'p_i': 20, 'u_i': 4.4646},
        {'id': 2, 'e_m': 0.277667, 'e_o_k': [0.056899, 0.045519, 0.036415], 'p_i': 40, 'u_i': 2.8456},
        {'id': 3, 'e_m': 2.558681, 'e_o_k': [0.524320, 0.419456, 0.335565], 'p_i': 80, 'u_i': 4.6357},
        {'id': 4, 'e_m': 0.415486, 'e_o_k': [0.085141, 0.068112, 0.054490], 'p_i': 10, 'u_i': 3.1275},
        {'id': 5, 'e_m': 6.998742, 'e_o_k': [1.434168, 1.147335, 0.917868], 'p_i': 80, 'u_i': 2.7677},
        {'id': 6, 'e_m': 0.663543, 'e_o_k': [0.135972, 0.108778, 0.087022], 'p_i': 10, 'u_i': 2.2237},
        {'id': 7, 'e_m': 0.049673, 'e_o_k': [0.010179, 0.008143, 0.006515], 'p_i': 10, 'u_i': 3.7702},
    ]
    B_BUDGET = 55.200003
    return processors, tasks, B_BUDGET
