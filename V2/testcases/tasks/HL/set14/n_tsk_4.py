"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.585280, 'e_o_k': [0.235793, 0.188634, 0.150907, 0.120726, 0.096581], 'p_i': 10, 'u_i': 3.7039},
        {'id': 1, 'e_m': 6.553932, 'e_o_k': [0.888240, 0.710592, 0.568474, 0.454779, 0.363823, 0.291058], 'p_i': 20, 'u_i': 3.4878},
        {'id': 2, 'e_m': 12.113109, 'e_o_k': [1.801688, 1.441350, 1.153080, 0.922464, 0.737971], 'p_i': 40, 'u_i': 4.7761},
        {'id': 3, 'e_m': 0.875811, 'e_o_k': [0.130267, 0.104214, 0.083371, 0.066697, 0.053357], 'p_i': 80, 'u_i': 2.0030},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
