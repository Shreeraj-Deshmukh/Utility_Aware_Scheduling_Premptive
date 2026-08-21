"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.994838, 'e_o_k': [1.718350, 1.374680, 1.099744], 'p_i': 10, 'u_i': 1.5654},
        {'id': 1, 'e_m': 8.718212, 'e_o_k': [6.780831, 5.424665], 'p_i': 20, 'u_i': 4.2073},
        {'id': 2, 'e_m': 0.889270, 'e_o_k': [0.510237, 0.408189, 0.326552], 'p_i': 40, 'u_i': 3.9694},
        {'id': 3, 'e_m': 3.389908, 'e_o_k': [2.636595, 2.109276], 'p_i': 80, 'u_i': 2.4321},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
