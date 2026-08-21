"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639994, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639994, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.178357, 'e_o_k': [0.074280, 0.059424, 0.047539, 0.038031, 0.030425], 'p_i': 10, 'u_i': 3.3453},
        {'id': 1, 'e_m': 6.375379, 'e_o_k': [3.658004, 2.926403, 2.341123], 'p_i': 20, 'u_i': 2.8841},
        {'id': 2, 'e_m': 1.100311, 'e_o_k': [0.631326, 0.505061, 0.404049], 'p_i': 40, 'u_i': 2.2513},
        {'id': 3, 'e_m': 13.676876, 'e_o_k': [6.486323, 5.189058, 4.151247, 3.320997], 'p_i': 80, 'u_i': 1.5109},
        {'id': 4, 'e_m': 2.125189, 'e_o_k': [1.219371, 0.975497, 0.780397], 'p_i': 10, 'u_i': 1.6396},
        {'id': 5, 'e_m': 1.048155, 'e_o_k': [0.601400, 0.481120, 0.384896], 'p_i': 20, 'u_i': 4.1445},
    ]
    B_BUDGET = 176.639994
    return processors, tasks, B_BUDGET
