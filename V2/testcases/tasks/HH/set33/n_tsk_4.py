"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.111998, 'e_o_k': [0.087110, 0.069688], 'p_i': 10, 'u_i': 3.5447},
        {'id': 1, 'e_m': 8.556467, 'e_o_k': [4.909448, 3.927559, 3.142047], 'p_i': 20, 'u_i': 1.0370},
        {'id': 2, 'e_m': 10.504417, 'e_o_k': [4.374757, 3.499806, 2.799845, 2.239876, 1.791901], 'p_i': 40, 'u_i': 1.6130},
        {'id': 3, 'e_m': 7.869313, 'e_o_k': [4.515180, 3.612144, 2.889715], 'p_i': 80, 'u_i': 1.3758},
    ]
    B_BUDGET = 176.640009
    return processors, tasks, B_BUDGET
