"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.024096, 'e_o_k': [0.013826, 0.011061, 0.008848], 'p_i': 10, 'u_i': 4.1859},
        {'id': 1, 'e_m': 1.824026, 'e_o_k': [1.046572, 0.837258, 0.669806], 'p_i': 20, 'u_i': 1.3758},
        {'id': 2, 'e_m': 2.806108, 'e_o_k': [1.610062, 1.288050, 1.030440], 'p_i': 40, 'u_i': 3.6848},
        {'id': 3, 'e_m': 0.481622, 'e_o_k': [0.276341, 0.221072, 0.176858], 'p_i': 80, 'u_i': 1.6851},
        {'id': 4, 'e_m': 2.721725, 'e_o_k': [1.561646, 1.249317, 0.999453], 'p_i': 20, 'u_i': 1.3700},
        {'id': 5, 'e_m': 0.681310, 'e_o_k': [0.390915, 0.312732, 0.250186], 'p_i': 10, 'u_i': 3.3252},
        {'id': 6, 'e_m': 0.612959, 'e_o_k': [0.351698, 0.281358, 0.225087], 'p_i': 80, 'u_i': 4.3008},
        {'id': 7, 'e_m': 1.466951, 'e_o_k': [0.841693, 0.673355, 0.538684], 'p_i': 80, 'u_i': 2.2362},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET
