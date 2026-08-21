"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.679884, 'e_o_k': [0.139320, 0.111456, 0.089165], 'p_i': 10, 'u_i': 4.6061},
        {'id': 1, 'e_m': 0.417910, 'e_o_k': [0.062159, 0.049728, 0.039782, 0.031826, 0.025460], 'p_i': 20, 'u_i': 1.8658},
        {'id': 2, 'e_m': 1.347507, 'e_o_k': [0.374307, 0.299446], 'p_i': 40, 'u_i': 4.6317},
        {'id': 3, 'e_m': 3.937087, 'e_o_k': [0.585597, 0.468478, 0.374782, 0.299826, 0.239861], 'p_i': 80, 'u_i': 4.1058},
        {'id': 4, 'e_m': 1.950051, 'e_o_k': [0.399601, 0.319681, 0.255744], 'p_i': 40, 'u_i': 1.5782},
        {'id': 5, 'e_m': 3.589272, 'e_o_k': [0.533864, 0.427091, 0.341673, 0.273338, 0.218671], 'p_i': 20, 'u_i': 1.2072},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
