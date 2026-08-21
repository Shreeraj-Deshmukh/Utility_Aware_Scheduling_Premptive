"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639992, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639992, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.453571, 'e_o_k': [0.834016, 0.667213, 0.533770], 'p_i': 10, 'u_i': 1.4749},
        {'id': 1, 'e_m': 7.609330, 'e_o_k': [3.608761, 2.887009, 2.309607, 1.847686], 'p_i': 20, 'u_i': 4.2682},
        {'id': 2, 'e_m': 4.803876, 'e_o_k': [2.000662, 1.600530, 1.280424, 1.024339, 0.819471], 'p_i': 40, 'u_i': 4.6830},
        {'id': 3, 'e_m': 4.130258, 'e_o_k': [3.212423, 2.569939], 'p_i': 80, 'u_i': 2.4027},
        {'id': 4, 'e_m': 1.771448, 'e_o_k': [1.377793, 1.102234], 'p_i': 80, 'u_i': 2.7203},
        {'id': 5, 'e_m': 3.212326, 'e_o_k': [1.219006, 0.975205, 0.780164, 0.624131, 0.499305, 0.399444], 'p_i': 40, 'u_i': 2.4000},
    ]
    B_BUDGET = 176.639992
    return processors, tasks, B_BUDGET
