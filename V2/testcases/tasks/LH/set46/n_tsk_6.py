"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320015, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320015, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.573715, 'e_o_k': [0.446223, 0.356978], 'p_i': 10, 'u_i': 2.0200},
        {'id': 1, 'e_m': 0.355799, 'e_o_k': [0.204147, 0.163318, 0.130654], 'p_i': 20, 'u_i': 3.9687},
        {'id': 2, 'e_m': 7.195452, 'e_o_k': [2.730514, 2.184412, 1.747529, 1.398023, 1.118419, 0.894735], 'p_i': 40, 'u_i': 2.3030},
        {'id': 3, 'e_m': 4.599977, 'e_o_k': [2.639331, 2.111465, 1.689172], 'p_i': 80, 'u_i': 2.6501},
        {'id': 4, 'e_m': 0.710090, 'e_o_k': [0.295730, 0.236584, 0.189267, 0.151414, 0.121131], 'p_i': 10, 'u_i': 1.7748},
        {'id': 5, 'e_m': 0.328872, 'e_o_k': [0.188697, 0.150958, 0.120766], 'p_i': 20, 'u_i': 3.9815},
    ]
    B_BUDGET = 88.320015
    return processors, tasks, B_BUDGET
