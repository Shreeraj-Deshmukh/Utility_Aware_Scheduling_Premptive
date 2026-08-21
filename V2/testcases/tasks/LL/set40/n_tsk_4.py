"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200013, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200013, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.308392, 'e_o_k': [0.221611, 0.177289, 0.141831, 0.113465], 'p_i': 10, 'u_i': 4.9199},
        {'id': 1, 'e_m': 1.333159, 'e_o_k': [0.225806, 0.180645, 0.144516, 0.115613], 'p_i': 20, 'u_i': 1.0213},
        {'id': 2, 'e_m': 6.197007, 'e_o_k': [1.049629, 0.839703, 0.671762, 0.537410], 'p_i': 40, 'u_i': 3.4352},
        {'id': 3, 'e_m': 3.806219, 'e_o_k': [0.644685, 0.515748, 0.412598, 0.330079], 'p_i': 80, 'u_i': 3.4020},
    ]
    B_BUDGET = 55.200013
    return processors, tasks, B_BUDGET
