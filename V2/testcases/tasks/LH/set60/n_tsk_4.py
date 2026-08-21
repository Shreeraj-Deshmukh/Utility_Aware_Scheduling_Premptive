"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.497419, 'e_o_k': [0.859175, 0.687340, 0.549872], 'p_i': 10, 'u_i': 1.5654},
        {'id': 1, 'e_m': 4.359106, 'e_o_k': [3.390416, 2.712333], 'p_i': 20, 'u_i': 4.2073},
        {'id': 2, 'e_m': 0.444635, 'e_o_k': [0.255118, 0.204095, 0.163276], 'p_i': 40, 'u_i': 3.9694},
        {'id': 3, 'e_m': 1.694954, 'e_o_k': [1.318298, 1.054638], 'p_i': 80, 'u_i': 2.4321},
    ]
    B_BUDGET = 88.320007
    return processors, tasks, B_BUDGET
