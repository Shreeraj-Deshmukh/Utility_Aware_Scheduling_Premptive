"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.093623, 'e_o_k': [0.415006, 0.332004, 0.265604, 0.212483, 0.169986, 0.135989], 'p_i': 10, 'u_i': 4.7125},
        {'id': 1, 'e_m': 2.396718, 'e_o_k': [1.136655, 0.909324, 0.727459, 0.581967], 'p_i': 20, 'u_i': 3.2766},
        {'id': 2, 'e_m': 7.878113, 'e_o_k': [6.127421, 4.901937], 'p_i': 40, 'u_i': 2.3226},
        {'id': 3, 'e_m': 29.907920, 'e_o_k': [23.261716, 18.609372], 'p_i': 80, 'u_i': 1.3159},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
