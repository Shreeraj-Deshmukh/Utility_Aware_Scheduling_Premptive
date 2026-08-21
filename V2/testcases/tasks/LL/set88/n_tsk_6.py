"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199987, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199987, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.472186, 'e_o_k': [0.079977, 0.063982, 0.051185, 0.040948], 'p_i': 10, 'u_i': 3.1874},
        {'id': 1, 'e_m': 1.113643, 'e_o_k': [0.309345, 0.247476], 'p_i': 20, 'u_i': 2.4550},
        {'id': 2, 'e_m': 3.618489, 'e_o_k': [0.741494, 0.593195, 0.474556], 'p_i': 40, 'u_i': 4.1368},
        {'id': 3, 'e_m': 0.177419, 'e_o_k': [0.049283, 0.039427], 'p_i': 80, 'u_i': 2.0023},
        {'id': 4, 'e_m': 7.030740, 'e_o_k': [1.045743, 0.836594, 0.669276, 0.535420, 0.428336], 'p_i': 40, 'u_i': 1.7941},
        {'id': 5, 'e_m': 1.146032, 'e_o_k': [0.170459, 0.136367, 0.109094, 0.087275, 0.069820], 'p_i': 40, 'u_i': 1.7354},
    ]
    B_BUDGET = 55.199987
    return processors, tasks, B_BUDGET
