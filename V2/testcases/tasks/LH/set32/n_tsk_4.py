"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.085725, 'e_o_k': [0.514910, 0.411928, 0.329542, 0.263634], 'p_i': 10, 'u_i': 1.8534},
        {'id': 1, 'e_m': 1.519635, 'e_o_k': [0.720694, 0.576555, 0.461244, 0.368995], 'p_i': 20, 'u_i': 3.8693},
        {'id': 2, 'e_m': 1.882901, 'e_o_k': [1.464479, 1.171583], 'p_i': 40, 'u_i': 4.5509},
        {'id': 3, 'e_m': 13.469859, 'e_o_k': [10.476557, 8.381246], 'p_i': 80, 'u_i': 1.7636},
    ]
    B_BUDGET = 88.319991
    return processors, tasks, B_BUDGET
