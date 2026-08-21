"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.20002, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.20002, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.335308, 'e_o_k': [0.045444, 0.036355, 0.029084, 0.023267, 0.018614, 0.014891], 'p_i': 10, 'u_i': 3.3883},
        {'id': 1, 'e_m': 0.532174, 'e_o_k': [0.079155, 0.063324, 0.050659, 0.040527, 0.032422], 'p_i': 20, 'u_i': 2.1673},
        {'id': 2, 'e_m': 3.423766, 'e_o_k': [0.464016, 0.371212, 0.296970, 0.237576, 0.190061, 0.152049], 'p_i': 40, 'u_i': 3.4649},
        {'id': 3, 'e_m': 2.134665, 'e_o_k': [0.361562, 0.289250, 0.231400, 0.185120], 'p_i': 80, 'u_i': 2.8434},
        {'id': 4, 'e_m': 0.350071, 'e_o_k': [0.071736, 0.057389, 0.045911], 'p_i': 20, 'u_i': 4.3788},
        {'id': 5, 'e_m': 2.100795, 'e_o_k': [0.355826, 0.284661, 0.227728, 0.182183], 'p_i': 10, 'u_i': 3.2500},
    ]
    B_BUDGET = 55.200020
    return processors, tasks, B_BUDGET
