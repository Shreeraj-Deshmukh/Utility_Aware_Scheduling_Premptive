"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.113918, 'e_o_k': [0.065363, 0.052290, 0.041832], 'p_i': 10, 'u_i': 4.7642},
        {'id': 1, 'e_m': 5.480782, 'e_o_k': [2.282572, 1.826058, 1.460846, 1.168677, 0.934942], 'p_i': 20, 'u_i': 4.7668},
        {'id': 2, 'e_m': 8.277898, 'e_o_k': [3.141279, 2.513023, 2.010419, 1.608335, 1.286668, 1.029334], 'p_i': 40, 'u_i': 4.7724},
        {'id': 3, 'e_m': 24.609731, 'e_o_k': [10.249174, 8.199339, 6.559471, 5.247577, 4.198062], 'p_i': 80, 'u_i': 4.0150},
    ]
    B_BUDGET = 176.639998
    return processors, tasks, B_BUDGET
