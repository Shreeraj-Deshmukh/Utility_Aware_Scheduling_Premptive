"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.579975, 'e_o_k': [0.241541, 0.193233, 0.154586, 0.123669, 0.098935], 'p_i': 10, 'u_i': 4.1808},
        {'id': 1, 'e_m': 5.974661, 'e_o_k': [2.267251, 1.813801, 1.451041, 1.160833, 0.928666, 0.742933], 'p_i': 20, 'u_i': 4.1927},
        {'id': 2, 'e_m': 4.376857, 'e_o_k': [2.511312, 2.009049, 1.607239], 'p_i': 40, 'u_i': 3.7566},
        {'id': 3, 'e_m': 26.707844, 'e_o_k': [15.324173, 12.259338, 9.807470], 'p_i': 80, 'u_i': 3.2050},
    ]
    B_BUDGET = 176.639994
    return processors, tasks, B_BUDGET
