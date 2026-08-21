"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "segments", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "segments", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.198004, 'e_o_k': [0.093904, 0.075123, 0.060099, 0.048079], 'p_i': 10, 'u_i': 2.2582},
        {'id': 1, 'e_m': 0.719096, 'e_o_k': [0.341035, 0.272828, 0.218262, 0.174610], 'p_i': 20, 'u_i': 2.9332},
        {'id': 2, 'e_m': 0.087079, 'e_o_k': [0.041298, 0.033038, 0.026431, 0.021144], 'p_i': 40, 'u_i': 1.0372},
        {'id': 3, 'e_m': 1.106586, 'e_o_k': [0.524804, 0.419843, 0.335874, 0.268699], 'p_i': 80, 'u_i': 1.7921},
        {'id': 4, 'e_m': 4.205332, 'e_o_k': [1.994399, 1.595519, 1.276415, 1.021132], 'p_i': 40, 'u_i': 3.3121},
        {'id': 5, 'e_m': 7.009502, 'e_o_k': [3.324290, 2.659432, 2.127545, 1.702036], 'p_i': 40, 'u_i': 3.7636},
        {'id': 6, 'e_m': 0.734312, 'e_o_k': [0.348251, 0.278601, 0.222880, 0.178304], 'p_i': 80, 'u_i': 1.1326},
        {'id': 7, 'e_m': 3.094861, 'e_o_k': [1.467752, 1.174202, 0.939362, 0.751489], 'p_i': 80, 'u_i': 3.1203},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
