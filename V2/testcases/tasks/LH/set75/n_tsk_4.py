"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.966054, 'e_o_k': [0.366596, 0.293277, 0.234622, 0.187697, 0.150158, 0.120126], 'p_i': 10, 'u_i': 2.1800},
        {'id': 1, 'e_m': 0.002627, 'e_o_k': [0.000997, 0.000797, 0.000638, 0.000510, 0.000408, 0.000327], 'p_i': 20, 'u_i': 3.3278},
        {'id': 2, 'e_m': 11.582843, 'e_o_k': [5.493218, 4.394575, 3.515660, 2.812528], 'p_i': 40, 'u_i': 2.2754},
        {'id': 3, 'e_m': 1.095371, 'e_o_k': [0.851955, 0.681564], 'p_i': 80, 'u_i': 1.2102},
    ]
    B_BUDGET = 88.319993
    return processors, tasks, B_BUDGET
