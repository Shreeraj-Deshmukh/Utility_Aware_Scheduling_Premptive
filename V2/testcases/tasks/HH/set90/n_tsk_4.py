"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640011, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640011, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.856431, 'e_o_k': [1.443891, 1.155113], 'p_i': 10, 'u_i': 3.9192},
        {'id': 1, 'e_m': 4.589354, 'e_o_k': [3.569497, 2.855598], 'p_i': 20, 'u_i': 2.9693},
        {'id': 2, 'e_m': 4.882850, 'e_o_k': [1.852933, 1.482347, 1.185877, 0.948702, 0.758961, 0.607169], 'p_i': 40, 'u_i': 2.3800},
        {'id': 3, 'e_m': 21.025440, 'e_o_k': [9.971415, 7.977132, 6.381705, 5.105364], 'p_i': 80, 'u_i': 3.7938},
    ]
    B_BUDGET = 176.640011
    return processors, tasks, B_BUDGET
