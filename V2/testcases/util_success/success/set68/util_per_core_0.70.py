"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439994, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439994, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.628607, 'e_o_k': [0.271435, 0.217148], 'p_i': 10, 'u_i': 3.1458},
        {'id': 1, 'e_m': 5.712488, 'e_o_k': [0.580537, 0.464430, 0.371544, 0.297235], 'p_i': 20, 'u_i': 4.9683},
        {'id': 2, 'e_m': 4.859977, 'e_o_k': [0.809996, 0.647997], 'p_i': 40, 'u_i': 2.4718},
        {'id': 3, 'e_m': 14.462492, 'e_o_k': [1.176042, 0.940833, 0.752667, 0.602133, 0.481707, 0.385365], 'p_i': 80, 'u_i': 4.0774},
        {'id': 4, 'e_m': 5.248028, 'e_o_k': [0.426752, 0.341402, 0.273121, 0.218497, 0.174798, 0.139838], 'p_i': 80, 'u_i': 2.9703},
        {'id': 5, 'e_m': 0.691888, 'e_o_k': [0.061746, 0.049397, 0.039518, 0.031614, 0.025291], 'p_i': 40, 'u_i': 3.9269},
        {'id': 6, 'e_m': 4.455067, 'e_o_k': [0.742511, 0.594009], 'p_i': 10, 'u_i': 3.4836},
        {'id': 7, 'e_m': 4.833201, 'e_o_k': [0.431330, 0.345064, 0.276051, 0.220841, 0.176673], 'p_i': 40, 'u_i': 2.8974},
    ]
    B_BUDGET = 167.439994
    return processors, tasks, B_BUDGET
