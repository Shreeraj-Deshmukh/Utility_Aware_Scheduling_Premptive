"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.963605, 'e_o_k': [1.405504, 1.124403, 0.899523, 0.719618], 'p_i': 10, 'u_i': 2.9572},
        {'id': 1, 'e_m': 4.069868, 'e_o_k': [1.930154, 1.544123, 1.235299, 0.988239], 'p_i': 20, 'u_i': 4.0373},
        {'id': 2, 'e_m': 0.778980, 'e_o_k': [0.324420, 0.259536, 0.207629, 0.166103, 0.132883], 'p_i': 40, 'u_i': 2.8937},
        {'id': 3, 'e_m': 22.453726, 'e_o_k': [10.648786, 8.519029, 6.815223, 5.452179], 'p_i': 80, 'u_i': 3.5048},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET
