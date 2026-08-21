"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.616783, 'e_o_k': [0.443222, 0.354578, 0.283662, 0.226930], 'p_i': 10, 'u_i': 4.9199},
        {'id': 1, 'e_m': 2.666317, 'e_o_k': [0.451612, 0.361290, 0.289032, 0.231225], 'p_i': 20, 'u_i': 1.0213},
        {'id': 2, 'e_m': 12.394015, 'e_o_k': [2.099257, 1.679406, 1.343525, 1.074820], 'p_i': 40, 'u_i': 3.4352},
        {'id': 3, 'e_m': 7.612437, 'e_o_k': [1.289369, 1.031496, 0.825196, 0.660157], 'p_i': 80, 'u_i': 3.4020},
    ]
    B_BUDGET = 110.400006
    return processors, tasks, B_BUDGET
