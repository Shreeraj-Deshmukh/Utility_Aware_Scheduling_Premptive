"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639997, "H": 80, "J": 40, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639997, "H": 80, "J": 40, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.259080, 'e_o_k': [0.722423, 0.577939, 0.462351], 'p_i': 10, 'u_i': 2.8729},
        {'id': 1, 'e_m': 3.910652, 'e_o_k': [2.243817, 1.795053, 1.436043], 'p_i': 20, 'u_i': 4.4646},
        {'id': 2, 'e_m': 0.555334, 'e_o_k': [0.318634, 0.254908, 0.203926], 'p_i': 40, 'u_i': 2.8456},
        {'id': 3, 'e_m': 5.117361, 'e_o_k': [2.936191, 2.348953, 1.879162], 'p_i': 80, 'u_i': 4.6357},
        {'id': 4, 'e_m': 0.830972, 'e_o_k': [0.476787, 0.381430, 0.305144], 'p_i': 10, 'u_i': 3.1275},
        {'id': 5, 'e_m': 13.997484, 'e_o_k': [8.031343, 6.425075, 5.140060], 'p_i': 80, 'u_i': 2.7677},
        {'id': 6, 'e_m': 1.327086, 'e_o_k': [0.761443, 0.609154, 0.487323], 'p_i': 10, 'u_i': 2.2237},
        {'id': 7, 'e_m': 0.099346, 'e_o_k': [0.057002, 0.045602, 0.036481], 'p_i': 10, 'u_i': 3.7702},
    ]
    B_BUDGET = 176.639997
    return processors, tasks, B_BUDGET
