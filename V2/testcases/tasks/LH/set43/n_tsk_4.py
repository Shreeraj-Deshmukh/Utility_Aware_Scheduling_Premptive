"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.059988, 'e_o_k': [0.034419, 0.027536, 0.022028], 'p_i': 10, 'u_i': 4.5752},
        {'id': 1, 'e_m': 3.128087, 'e_o_k': [1.483510, 1.186808, 0.949446, 0.759557], 'p_i': 20, 'u_i': 3.6570},
        {'id': 2, 'e_m': 5.020593, 'e_o_k': [2.381040, 1.904832, 1.523866, 1.219092], 'p_i': 40, 'u_i': 3.9951},
        {'id': 3, 'e_m': 8.966561, 'e_o_k': [5.144748, 4.115798, 3.292639], 'p_i': 80, 'u_i': 2.8657},
    ]
    B_BUDGET = 88.319991
    return processors, tasks, B_BUDGET
