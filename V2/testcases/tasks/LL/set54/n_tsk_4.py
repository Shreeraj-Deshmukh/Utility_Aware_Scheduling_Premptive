"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.19999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.19999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.003191, 'e_o_k': [0.271488, 0.217190, 0.173752, 0.139002, 0.111201, 0.088961], 'p_i': 10, 'u_i': 3.2200},
        {'id': 1, 'e_m': 0.332245, 'e_o_k': [0.068083, 0.054466, 0.043573], 'p_i': 20, 'u_i': 1.6886},
        {'id': 2, 'e_m': 7.300599, 'e_o_k': [1.085882, 0.868705, 0.694964, 0.555971, 0.444777], 'p_i': 40, 'u_i': 4.2653},
        {'id': 3, 'e_m': 0.044298, 'e_o_k': [0.006004, 0.004803, 0.003842, 0.003074, 0.002459, 0.001967], 'p_i': 80, 'u_i': 3.8195},
    ]
    B_BUDGET = 55.199990
    return processors, tasks, B_BUDGET
