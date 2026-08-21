"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.260305, 'e_o_k': [0.053341, 0.042673, 0.034138], 'p_i': 10, 'u_i': 3.2721},
        {'id': 1, 'e_m': 1.935309, 'e_o_k': [0.537586, 0.430069], 'p_i': 20, 'u_i': 2.5377},
        {'id': 2, 'e_m': 8.445409, 'e_o_k': [2.345947, 1.876758], 'p_i': 40, 'u_i': 2.5387},
        {'id': 3, 'e_m': 37.285509, 'e_o_k': [6.315296, 5.052237, 4.041790, 3.233432], 'p_i': 80, 'u_i': 1.0056},
    ]
    B_BUDGET = 110.400005
    return processors, tasks, B_BUDGET
