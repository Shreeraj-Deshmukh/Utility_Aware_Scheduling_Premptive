"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.062885, 'e_o_k': [0.504078, 0.403262, 0.322610, 0.258088], 'p_i': 10, 'u_i': 2.8802},
        {'id': 1, 'e_m': 1.880293, 'e_o_k': [0.891738, 0.713390, 0.570712, 0.456570], 'p_i': 20, 'u_i': 1.9313},
        {'id': 2, 'e_m': 4.030110, 'e_o_k': [3.134530, 2.507624], 'p_i': 40, 'u_i': 4.0147},
        {'id': 3, 'e_m': 1.729233, 'e_o_k': [0.656206, 0.524965, 0.419972, 0.335977, 0.268782, 0.215025], 'p_i': 80, 'u_i': 3.8759},
        {'id': 4, 'e_m': 2.650485, 'e_o_k': [1.520770, 1.216616, 0.973293], 'p_i': 80, 'u_i': 4.3076},
        {'id': 5, 'e_m': 3.535813, 'e_o_k': [1.341763, 1.073410, 0.858728, 0.686983, 0.549586, 0.439669], 'p_i': 80, 'u_i': 1.9116},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
