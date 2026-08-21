"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.421301, 'e_o_k': [1.148313, 0.918651, 0.734921, 0.587936], 'p_i': 10, 'u_i': 4.8908},
        {'id': 1, 'e_m': 2.540034, 'e_o_k': [1.057844, 0.846275, 0.677020, 0.541616, 0.433293], 'p_i': 20, 'u_i': 3.7143},
        {'id': 2, 'e_m': 4.920392, 'e_o_k': [2.049187, 1.639350, 1.311480, 1.049184, 0.839347], 'p_i': 40, 'u_i': 4.3200},
        {'id': 3, 'e_m': 24.628672, 'e_o_k': [9.346035, 7.476828, 5.981463, 4.785170, 3.828136, 3.062509], 'p_i': 80, 'u_i': 3.1069},
    ]
    B_BUDGET = 176.639997
    return processors, tasks, B_BUDGET
