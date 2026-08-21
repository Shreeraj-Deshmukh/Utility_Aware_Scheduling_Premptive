"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.543082, 'e_o_k': [0.080777, 0.064622, 0.051697, 0.041358, 0.033086], 'p_i': 10, 'u_i': 4.6924},
        {'id': 1, 'e_m': 0.967555, 'e_o_k': [0.131131, 0.104904, 0.083924, 0.067139, 0.053711, 0.042969], 'p_i': 20, 'u_i': 3.7468},
        {'id': 2, 'e_m': 6.912441, 'e_o_k': [1.920123, 1.536098], 'p_i': 40, 'u_i': 3.5829},
        {'id': 3, 'e_m': 9.960244, 'e_o_k': [1.349890, 1.079912, 0.863930, 0.691144, 0.552915, 0.442332], 'p_i': 80, 'u_i': 3.3883},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
