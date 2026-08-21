"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.32001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.361280, 'e_o_k': [0.171339, 0.137071, 0.109657, 0.087725], 'p_i': 10, 'u_i': 3.6067},
        {'id': 1, 'e_m': 2.943416, 'e_o_k': [1.688845, 1.351076, 1.080861], 'p_i': 20, 'u_i': 2.3971},
        {'id': 2, 'e_m': 2.862493, 'e_o_k': [1.192138, 0.953710, 0.762968, 0.610375, 0.488300], 'p_i': 40, 'u_i': 3.3740},
        {'id': 3, 'e_m': 11.611114, 'e_o_k': [9.030866, 7.224693], 'p_i': 80, 'u_i': 3.0150},
    ]
    B_BUDGET = 88.320010
    return processors, tasks, B_BUDGET
