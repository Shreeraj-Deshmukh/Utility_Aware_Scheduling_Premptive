"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.242482, 'e_o_k': [0.188597, 0.150878], 'p_i': 10, 'u_i': 1.7042},
        {'id': 1, 'e_m': 0.368320, 'e_o_k': [0.286471, 0.229177], 'p_i': 20, 'u_i': 4.3788},
        {'id': 2, 'e_m': 2.283808, 'e_o_k': [1.776295, 1.421036], 'p_i': 40, 'u_i': 3.2500},
        {'id': 3, 'e_m': 1.295241, 'e_o_k': [1.007410, 0.805928], 'p_i': 80, 'u_i': 3.9101},
        {'id': 4, 'e_m': 0.598180, 'e_o_k': [0.465251, 0.372201], 'p_i': 80, 'u_i': 2.7187},
        {'id': 5, 'e_m': 2.822117, 'e_o_k': [2.194980, 1.755984], 'p_i': 40, 'u_i': 1.9356},
        {'id': 6, 'e_m': 12.997943, 'e_o_k': [10.109511, 8.087609], 'p_i': 80, 'u_i': 1.5831},
        {'id': 7, 'e_m': 1.741824, 'e_o_k': [1.354752, 1.083802], 'p_i': 40, 'u_i': 3.6851},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET
