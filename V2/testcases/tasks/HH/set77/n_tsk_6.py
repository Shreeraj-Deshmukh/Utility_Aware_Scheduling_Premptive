"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.608308, 'e_o_k': [0.349029, 0.279223, 0.223379], 'p_i': 10, 'u_i': 2.5184},
        {'id': 1, 'e_m': 4.670017, 'e_o_k': [1.944914, 1.555931, 1.244745, 0.995796, 0.796637], 'p_i': 20, 'u_i': 4.2996},
        {'id': 2, 'e_m': 6.040063, 'e_o_k': [2.292070, 1.833656, 1.466925, 1.173540, 0.938832, 0.751066], 'p_i': 40, 'u_i': 3.3901},
        {'id': 3, 'e_m': 1.905406, 'e_o_k': [0.723060, 0.578448, 0.462758, 0.370206, 0.296165, 0.236932], 'p_i': 80, 'u_i': 2.3217},
        {'id': 4, 'e_m': 20.651648, 'e_o_k': [9.794142, 7.835314, 6.268251, 5.014601], 'p_i': 80, 'u_i': 2.1118},
        {'id': 5, 'e_m': 5.816289, 'e_o_k': [2.758403, 2.206722, 1.765378, 1.412302], 'p_i': 80, 'u_i': 4.2305},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET
