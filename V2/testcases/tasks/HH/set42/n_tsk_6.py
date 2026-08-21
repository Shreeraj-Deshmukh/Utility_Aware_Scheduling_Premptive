"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640017, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640017, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.939509, 'e_o_k': [0.807744, 0.646195, 0.516956, 0.413565, 0.330852], 'p_i': 10, 'u_i': 2.8937},
        {'id': 1, 'e_m': 2.763818, 'e_o_k': [1.310754, 1.048603, 0.838882, 0.671106], 'p_i': 20, 'u_i': 3.5048},
        {'id': 2, 'e_m': 0.413834, 'e_o_k': [0.157041, 0.125633, 0.100506, 0.080405, 0.064324, 0.051459], 'p_i': 40, 'u_i': 4.5166},
        {'id': 3, 'e_m': 2.175525, 'e_o_k': [1.031753, 0.825402, 0.660322, 0.528257], 'p_i': 80, 'u_i': 1.0922},
        {'id': 4, 'e_m': 8.790579, 'e_o_k': [6.837117, 5.469694], 'p_i': 40, 'u_i': 2.4300},
        {'id': 5, 'e_m': 4.211078, 'e_o_k': [1.753781, 1.403024, 1.122420, 0.897936, 0.718349], 'p_i': 20, 'u_i': 4.3958},
    ]
    B_BUDGET = 176.640017
    return processors, tasks, B_BUDGET
