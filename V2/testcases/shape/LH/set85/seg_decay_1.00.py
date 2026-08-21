"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320024, "H": 80, "J": 37, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.320024, "H": 80, "J": 37, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.244220, 'e_o_k': [0.170954, 0.170954], 'p_i': 10, 'u_i': 1.2408},
        {'id': 1, 'e_m': 0.462328, 'e_o_k': [0.161815, 0.161815, 0.161815, 0.161815], 'p_i': 20, 'u_i': 2.7274},
        {'id': 2, 'e_m': 1.144163, 'e_o_k': [0.320366, 0.320366, 0.320366, 0.320366, 0.320366], 'p_i': 40, 'u_i': 3.7398},
        {'id': 3, 'e_m': 2.328605, 'e_o_k': [1.086682, 1.086682, 1.086682], 'p_i': 80, 'u_i': 1.4758},
        {'id': 4, 'e_m': 0.072384, 'e_o_k': [0.016890, 0.016890, 0.016890, 0.016890, 0.016890, 0.016890], 'p_i': 10, 'u_i': 1.9890},
        {'id': 5, 'e_m': 0.070477, 'e_o_k': [0.032889, 0.032889, 0.032889], 'p_i': 40, 'u_i': 1.7667},
        {'id': 6, 'e_m': 2.462336, 'e_o_k': [1.149090, 1.149090, 1.149090], 'p_i': 20, 'u_i': 2.7743},
        {'id': 7, 'e_m': 1.626328, 'e_o_k': [0.569215, 0.569215, 0.569215, 0.569215], 'p_i': 10, 'u_i': 3.3191},
    ]
    B_BUDGET = 88.320024
    return processors, tasks, B_BUDGET
