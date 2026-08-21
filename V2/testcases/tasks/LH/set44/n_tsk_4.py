"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.289987, 'e_o_k': [0.120771, 0.096616, 0.077293, 0.061835, 0.049468], 'p_i': 10, 'u_i': 4.1808},
        {'id': 1, 'e_m': 2.987330, 'e_o_k': [1.133626, 0.906901, 0.725520, 0.580416, 0.464333, 0.371466], 'p_i': 20, 'u_i': 4.1927},
        {'id': 2, 'e_m': 2.188429, 'e_o_k': [1.255656, 1.004525, 0.803620], 'p_i': 40, 'u_i': 3.7566},
        {'id': 3, 'e_m': 13.353922, 'e_o_k': [7.662086, 6.129669, 4.903735], 'p_i': 80, 'u_i': 3.2050},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
