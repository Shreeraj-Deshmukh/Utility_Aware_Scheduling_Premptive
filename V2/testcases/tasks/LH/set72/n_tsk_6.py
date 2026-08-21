"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320001, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320001, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.160373, 'e_o_k': [0.066790, 0.053432, 0.042746, 0.034197, 0.027357], 'p_i': 10, 'u_i': 1.6464},
        {'id': 1, 'e_m': 1.239537, 'e_o_k': [0.964084, 0.771267], 'p_i': 20, 'u_i': 4.4830},
        {'id': 2, 'e_m': 3.471757, 'e_o_k': [1.317455, 1.053964, 0.843171, 0.674537, 0.539629, 0.431704], 'p_i': 40, 'u_i': 3.9048},
        {'id': 3, 'e_m': 4.241467, 'e_o_k': [1.766437, 1.413150, 1.130520, 0.904416, 0.723533], 'p_i': 80, 'u_i': 3.4604},
        {'id': 4, 'e_m': 2.172428, 'e_o_k': [1.246475, 0.997180, 0.797744], 'p_i': 20, 'u_i': 2.2645},
        {'id': 5, 'e_m': 0.735522, 'e_o_k': [0.306322, 0.245057, 0.196046, 0.156837, 0.125469], 'p_i': 10, 'u_i': 4.9290},
    ]
    B_BUDGET = 88.320001
    return processors, tasks, B_BUDGET
