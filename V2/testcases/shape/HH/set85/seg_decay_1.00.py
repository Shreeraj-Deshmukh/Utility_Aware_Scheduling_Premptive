"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639999, "H": 80, "J": 37, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 176.639999, "H": 80, "J": 37, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.488440, 'e_o_k': [0.341908, 0.341908], 'p_i': 10, 'u_i': 1.2408},
        {'id': 1, 'e_m': 0.924655, 'e_o_k': [0.323629, 0.323629, 0.323629, 0.323629], 'p_i': 20, 'u_i': 2.7274},
        {'id': 2, 'e_m': 2.288327, 'e_o_k': [0.640731, 0.640731, 0.640731, 0.640731, 0.640731], 'p_i': 40, 'u_i': 3.7398},
        {'id': 3, 'e_m': 4.657210, 'e_o_k': [2.173365, 2.173365, 2.173365], 'p_i': 80, 'u_i': 1.4758},
        {'id': 4, 'e_m': 0.144768, 'e_o_k': [0.033779, 0.033779, 0.033779, 0.033779, 0.033779, 0.033779], 'p_i': 10, 'u_i': 1.9890},
        {'id': 5, 'e_m': 0.140954, 'e_o_k': [0.065779, 0.065779, 0.065779], 'p_i': 40, 'u_i': 1.7667},
        {'id': 6, 'e_m': 4.924673, 'e_o_k': [2.298181, 2.298181, 2.298181], 'p_i': 20, 'u_i': 2.7743},
        {'id': 7, 'e_m': 3.252657, 'e_o_k': [1.138430, 1.138430, 1.138430, 1.138430], 'p_i': 10, 'u_i': 3.3191},
    ]
    B_BUDGET = 176.639999
    return processors, tasks, B_BUDGET
