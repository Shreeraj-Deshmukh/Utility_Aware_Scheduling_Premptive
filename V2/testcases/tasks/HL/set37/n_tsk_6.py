"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400003, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400003, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.122217, 'e_o_k': [0.639799, 0.511839, 0.409471], 'p_i': 10, 'u_i': 4.5515},
        {'id': 1, 'e_m': 0.920288, 'e_o_k': [0.255636, 0.204509], 'p_i': 20, 'u_i': 3.0521},
        {'id': 2, 'e_m': 2.267160, 'e_o_k': [0.384004, 0.307203, 0.245763, 0.196610], 'p_i': 40, 'u_i': 1.1668},
        {'id': 3, 'e_m': 24.228175, 'e_o_k': [6.730049, 5.384039], 'p_i': 80, 'u_i': 2.3448},
        {'id': 4, 'e_m': 2.129859, 'e_o_k': [0.316792, 0.253434, 0.202747, 0.162198, 0.129758], 'p_i': 40, 'u_i': 3.9461},
        {'id': 5, 'e_m': 0.579724, 'e_o_k': [0.098192, 0.078553, 0.062843, 0.050274], 'p_i': 20, 'u_i': 2.2173},
    ]
    B_BUDGET = 110.400003
    return processors, tasks, B_BUDGET
