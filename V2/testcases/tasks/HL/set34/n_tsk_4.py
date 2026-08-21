"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.171934, 'e_o_k': [0.445068, 0.356055, 0.284844], 'p_i': 10, 'u_i': 1.7419},
        {'id': 1, 'e_m': 6.026758, 'e_o_k': [1.020792, 0.816634, 0.653307, 0.522646], 'p_i': 20, 'u_i': 1.0689},
        {'id': 2, 'e_m': 6.980869, 'e_o_k': [1.939130, 1.551304], 'p_i': 40, 'u_i': 2.1386},
        {'id': 3, 'e_m': 8.555761, 'e_o_k': [1.272573, 1.018058, 0.814447, 0.651557, 0.521246], 'p_i': 80, 'u_i': 3.8785},
    ]
    B_BUDGET = 110.400005
    return processors, tasks, B_BUDGET
