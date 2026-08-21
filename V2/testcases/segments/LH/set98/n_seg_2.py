"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320005, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.320005, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.877722, 'e_o_k': [0.682673, 0.546138], 'p_i': 10, 'u_i': 2.2749},
        {'id': 1, 'e_m': 0.626081, 'e_o_k': [0.486952, 0.389561], 'p_i': 20, 'u_i': 4.9536},
        {'id': 2, 'e_m': 2.383329, 'e_o_k': [1.853700, 1.482960], 'p_i': 40, 'u_i': 2.9112},
        {'id': 3, 'e_m': 0.098499, 'e_o_k': [0.076611, 0.061288], 'p_i': 80, 'u_i': 2.1467},
        {'id': 4, 'e_m': 0.036647, 'e_o_k': [0.028503, 0.022803], 'p_i': 10, 'u_i': 3.3563},
        {'id': 5, 'e_m': 5.989060, 'e_o_k': [4.658158, 3.726526], 'p_i': 80, 'u_i': 2.2972},
        {'id': 6, 'e_m': 0.258182, 'e_o_k': [0.200808, 0.160647], 'p_i': 10, 'u_i': 3.3121},
        {'id': 7, 'e_m': 4.630526, 'e_o_k': [3.601520, 2.881216], 'p_i': 40, 'u_i': 4.6359},
    ]
    B_BUDGET = 88.320005
    return processors, tasks, B_BUDGET
