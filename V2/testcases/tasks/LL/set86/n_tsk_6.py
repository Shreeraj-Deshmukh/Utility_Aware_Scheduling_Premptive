"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.070133, 'e_o_k': [0.009505, 0.007604, 0.006083, 0.004867, 0.003893, 0.003115], 'p_i': 10, 'u_i': 3.8731},
        {'id': 1, 'e_m': 0.306792, 'e_o_k': [0.062867, 0.050294, 0.040235], 'p_i': 20, 'u_i': 4.5676},
        {'id': 2, 'e_m': 1.897257, 'e_o_k': [0.321351, 0.257081, 0.205665, 0.164532], 'p_i': 40, 'u_i': 2.8991},
        {'id': 3, 'e_m': 11.381869, 'e_o_k': [1.692924, 1.354339, 1.083472, 0.866777, 0.693422], 'p_i': 80, 'u_i': 1.9490},
        {'id': 4, 'e_m': 1.044862, 'e_o_k': [0.290239, 0.232192], 'p_i': 20, 'u_i': 1.1516},
        {'id': 5, 'e_m': 5.427967, 'e_o_k': [1.112288, 0.889831, 0.711865], 'p_i': 40, 'u_i': 2.6742},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
