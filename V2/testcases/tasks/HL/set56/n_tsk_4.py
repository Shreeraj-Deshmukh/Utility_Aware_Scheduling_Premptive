"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.146111, 'e_o_k': [0.849613, 0.679690, 0.543752], 'p_i': 10, 'u_i': 2.4204},
        {'id': 1, 'e_m': 0.534383, 'e_o_k': [0.072424, 0.057939, 0.046351, 0.037081, 0.029665, 0.023732], 'p_i': 20, 'u_i': 4.6440},
        {'id': 2, 'e_m': 2.973342, 'e_o_k': [0.402971, 0.322376, 0.257901, 0.206321, 0.165057, 0.132045], 'p_i': 40, 'u_i': 4.0628},
        {'id': 3, 'e_m': 22.746898, 'e_o_k': [3.383344, 2.706675, 2.165340, 1.732272, 1.385818], 'p_i': 80, 'u_i': 1.2692},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
