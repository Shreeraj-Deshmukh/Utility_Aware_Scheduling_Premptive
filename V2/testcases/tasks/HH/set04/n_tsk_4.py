"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.003558, 'e_o_k': [0.760306, 0.608245, 0.486596, 0.389277, 0.311421, 0.249137], 'p_i': 10, 'u_i': 3.5500},
        {'id': 1, 'e_m': 0.144137, 'e_o_k': [0.082702, 0.066161, 0.052929], 'p_i': 20, 'u_i': 2.3662},
        {'id': 2, 'e_m': 9.164294, 'e_o_k': [7.127784, 5.702227], 'p_i': 40, 'u_i': 3.8013},
        {'id': 3, 'e_m': 29.066399, 'e_o_k': [16.677442, 13.341953, 10.673563], 'p_i': 80, 'u_i': 4.3808},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
