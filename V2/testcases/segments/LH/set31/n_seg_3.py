"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.198004, 'e_o_k': [0.113609, 0.090887, 0.072710], 'p_i': 10, 'u_i': 2.2582},
        {'id': 1, 'e_m': 0.719096, 'e_o_k': [0.412596, 0.330077, 0.264061], 'p_i': 20, 'u_i': 2.9332},
        {'id': 2, 'e_m': 0.087079, 'e_o_k': [0.049963, 0.039971, 0.031977], 'p_i': 40, 'u_i': 1.0372},
        {'id': 3, 'e_m': 1.106586, 'e_o_k': [0.634926, 0.507941, 0.406353], 'p_i': 80, 'u_i': 1.7921},
        {'id': 4, 'e_m': 4.205332, 'e_o_k': [2.412895, 1.930316, 1.544253], 'p_i': 40, 'u_i': 3.3121},
        {'id': 5, 'e_m': 7.009502, 'e_o_k': [4.021846, 3.217476, 2.573981], 'p_i': 40, 'u_i': 3.7636},
        {'id': 6, 'e_m': 0.734312, 'e_o_k': [0.421326, 0.337061, 0.269649], 'p_i': 80, 'u_i': 1.1326},
        {'id': 7, 'e_m': 3.094861, 'e_o_k': [1.775740, 1.420592, 1.136474], 'p_i': 80, 'u_i': 3.1203},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET
