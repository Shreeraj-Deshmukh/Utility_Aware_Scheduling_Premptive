"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.533877, 'e_o_k': [0.090426, 0.072341, 0.057873, 0.046298], 'p_i': 10, 'u_i': 2.4700},
        {'id': 1, 'e_m': 1.248730, 'e_o_k': [0.185735, 0.148588, 0.118870, 0.095096, 0.076077], 'p_i': 20, 'u_i': 2.1021},
        {'id': 2, 'e_m': 0.016411, 'e_o_k': [0.002224, 0.001779, 0.001423, 0.001139, 0.000911, 0.000729], 'p_i': 40, 'u_i': 2.0660},
        {'id': 3, 'e_m': 7.953863, 'e_o_k': [2.209406, 1.767525], 'p_i': 80, 'u_i': 3.5059},
        {'id': 4, 'e_m': 14.714138, 'e_o_k': [3.015192, 2.412154, 1.929723], 'p_i': 80, 'u_i': 1.7742},
        {'id': 5, 'e_m': 0.016621, 'e_o_k': [0.003406, 0.002725, 0.002180], 'p_i': 40, 'u_i': 1.4108},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
