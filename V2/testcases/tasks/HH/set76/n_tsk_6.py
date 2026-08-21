"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639993, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639993, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.489600, 'e_o_k': [0.565270, 0.452216, 0.361773, 0.289418, 0.231535, 0.185228], 'p_i': 10, 'u_i': 3.7891},
        {'id': 1, 'e_m': 7.499350, 'e_o_k': [4.302906, 3.442324, 2.753860], 'p_i': 20, 'u_i': 1.3517},
        {'id': 2, 'e_m': 1.563803, 'e_o_k': [0.741641, 0.593313, 0.474650, 0.379720], 'p_i': 40, 'u_i': 4.0093},
        {'id': 3, 'e_m': 1.577415, 'e_o_k': [0.905074, 0.724059, 0.579247], 'p_i': 80, 'u_i': 1.1110},
        {'id': 4, 'e_m': 12.968885, 'e_o_k': [4.921405, 3.937124, 3.149699, 2.519759, 2.015807, 1.612646], 'p_i': 80, 'u_i': 1.1701},
        {'id': 5, 'e_m': 1.102973, 'e_o_k': [0.632853, 0.506283, 0.405026], 'p_i': 20, 'u_i': 4.4848},
    ]
    B_BUDGET = 176.639993
    return processors, tasks, B_BUDGET
