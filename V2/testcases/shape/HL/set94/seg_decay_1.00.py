"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400003, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.400003, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.667633, 'e_o_k': [0.083454, 0.083454, 0.083454, 0.083454], 'p_i': 10, 'u_i': 1.6879},
        {'id': 1, 'e_m': 1.022805, 'e_o_k': [0.127851, 0.127851, 0.127851, 0.127851], 'p_i': 20, 'u_i': 2.2588},
        {'id': 2, 'e_m': 4.952657, 'e_o_k': [1.238164, 1.238164], 'p_i': 40, 'u_i': 4.0829},
        {'id': 3, 'e_m': 7.527601, 'e_o_k': [1.254600, 1.254600, 1.254600], 'p_i': 80, 'u_i': 1.6866},
        {'id': 4, 'e_m': 0.525923, 'e_o_k': [0.087654, 0.087654, 0.087654], 'p_i': 40, 'u_i': 3.5950},
        {'id': 5, 'e_m': 15.701459, 'e_o_k': [3.925365, 3.925365], 'p_i': 80, 'u_i': 4.2025},
        {'id': 6, 'e_m': 6.203629, 'e_o_k': [1.550907, 1.550907], 'p_i': 40, 'u_i': 3.6883},
        {'id': 7, 'e_m': 7.974239, 'e_o_k': [1.993560, 1.993560], 'p_i': 80, 'u_i': 1.6967},
    ]
    B_BUDGET = 110.400003
    return processors, tasks, B_BUDGET
