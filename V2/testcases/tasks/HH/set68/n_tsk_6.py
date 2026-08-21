"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639997, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639997, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.271833, 'e_o_k': [0.603173, 0.482538, 0.386031, 0.308825], 'p_i': 10, 'u_i': 4.9351},
        {'id': 1, 'e_m': 4.379754, 'e_o_k': [1.824029, 1.459223, 1.167378, 0.933903, 0.747122], 'p_i': 20, 'u_i': 4.9277},
        {'id': 2, 'e_m': 3.696436, 'e_o_k': [1.753052, 1.402442, 1.121953, 0.897563], 'p_i': 40, 'u_i': 1.3099},
        {'id': 3, 'e_m': 11.223342, 'e_o_k': [5.322723, 4.258179, 3.406543, 2.725234], 'p_i': 80, 'u_i': 1.1502},
        {'id': 4, 'e_m': 0.604848, 'e_o_k': [0.347044, 0.277635, 0.222108], 'p_i': 10, 'u_i': 2.1747},
        {'id': 5, 'e_m': 3.212830, 'e_o_k': [2.498868, 1.999094], 'p_i': 20, 'u_i': 4.4262},
    ]
    B_BUDGET = 176.639997
    return processors, tasks, B_BUDGET
