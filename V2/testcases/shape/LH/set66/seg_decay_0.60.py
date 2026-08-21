"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320001, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.320001, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.067141, 'e_o_k': [0.043197, 0.025918, 0.015551, 0.009331], 'p_i': 10, 'u_i': 3.0491},
        {'id': 1, 'e_m': 0.797553, 'e_o_k': [0.484288, 0.290573, 0.174344, 0.104606, 0.062764], 'p_i': 20, 'u_i': 3.9469},
        {'id': 2, 'e_m': 2.043499, 'e_o_k': [1.459642, 0.875785, 0.525471], 'p_i': 40, 'u_i': 1.2331},
        {'id': 3, 'e_m': 5.056120, 'e_o_k': [3.611514, 2.166909, 1.300145], 'p_i': 80, 'u_i': 3.8857},
        {'id': 4, 'e_m': 0.957980, 'e_o_k': [0.838232, 0.502939], 'p_i': 20, 'u_i': 4.4773},
        {'id': 5, 'e_m': 0.502682, 'e_o_k': [0.439847, 0.263908], 'p_i': 10, 'u_i': 2.4546},
        {'id': 6, 'e_m': 0.546749, 'e_o_k': [0.351769, 0.211061, 0.126637, 0.075982], 'p_i': 80, 'u_i': 1.1544},
        {'id': 7, 'e_m': 10.729419, 'e_o_k': [7.663871, 4.598322, 2.758993], 'p_i': 80, 'u_i': 4.0204},
    ]
    B_BUDGET = 88.320001
    return processors, tasks, B_BUDGET
