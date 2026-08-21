"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639997, "H": 80, "J": 25, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 176.639997, "H": 80, "J": 25, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.147016, 'e_o_k': [0.802912, 0.802912], 'p_i': 10, 'u_i': 2.5980},
        {'id': 1, 'e_m': 3.773755, 'e_o_k': [2.641629, 2.641629], 'p_i': 20, 'u_i': 2.9083},
        {'id': 2, 'e_m': 5.350477, 'e_o_k': [2.496889, 2.496889, 2.496889], 'p_i': 40, 'u_i': 4.8275},
        {'id': 3, 'e_m': 16.969247, 'e_o_k': [4.751389, 4.751389, 4.751389, 4.751389, 4.751389], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 1.099497, 'e_o_k': [0.513098, 0.513098, 0.513098], 'p_i': 20, 'u_i': 1.8333},
        {'id': 5, 'e_m': 0.148964, 'e_o_k': [0.041710, 0.041710, 0.041710, 0.041710, 0.041710], 'p_i': 20, 'u_i': 4.5368},
        {'id': 6, 'e_m': 3.297912, 'e_o_k': [0.769513, 0.769513, 0.769513, 0.769513, 0.769513, 0.769513], 'p_i': 80, 'u_i': 4.6383},
        {'id': 7, 'e_m': 3.766890, 'e_o_k': [1.054729, 1.054729, 1.054729, 1.054729, 1.054729], 'p_i': 80, 'u_i': 3.5515},
    ]
    B_BUDGET = 176.639997
    return processors, tasks, B_BUDGET
