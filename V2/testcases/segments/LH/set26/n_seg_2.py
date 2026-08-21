"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320007, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.320007, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.630729, 'e_o_k': [1.268345, 1.014676], 'p_i': 10, 'u_i': 2.1780},
        {'id': 1, 'e_m': 0.554446, 'e_o_k': [0.431236, 0.344989], 'p_i': 20, 'u_i': 3.8388},
        {'id': 2, 'e_m': 1.443928, 'e_o_k': [1.123055, 0.898444], 'p_i': 40, 'u_i': 1.0041},
        {'id': 3, 'e_m': 3.915968, 'e_o_k': [3.045753, 2.436602], 'p_i': 80, 'u_i': 4.1994},
        {'id': 4, 'e_m': 0.833670, 'e_o_k': [0.648410, 0.518728], 'p_i': 40, 'u_i': 2.3676},
        {'id': 5, 'e_m': 0.367491, 'e_o_k': [0.285826, 0.228661], 'p_i': 10, 'u_i': 3.7622},
        {'id': 6, 'e_m': 0.185253, 'e_o_k': [0.144086, 0.115269], 'p_i': 10, 'u_i': 1.6504},
        {'id': 7, 'e_m': 3.843267, 'e_o_k': [2.989208, 2.391366], 'p_i': 80, 'u_i': 2.4020},
    ]
    B_BUDGET = 88.320007
    return processors, tasks, B_BUDGET
