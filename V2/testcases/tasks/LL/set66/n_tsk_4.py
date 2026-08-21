"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199987, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199987, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.154912, 'e_o_k': [0.023041, 0.018433, 0.014747, 0.011797, 0.009438], 'p_i': 10, 'u_i': 3.6728},
        {'id': 1, 'e_m': 2.110085, 'e_o_k': [0.285975, 0.228780, 0.183024, 0.146419, 0.117135, 0.093708], 'p_i': 20, 'u_i': 2.1630},
        {'id': 2, 'e_m': 6.047745, 'e_o_k': [0.819638, 0.655710, 0.524568, 0.419654, 0.335724, 0.268579], 'p_i': 40, 'u_i': 4.2465},
        {'id': 3, 'e_m': 10.224870, 'e_o_k': [1.385754, 1.108603, 0.886883, 0.709506, 0.567605, 0.454084], 'p_i': 80, 'u_i': 1.5896},
    ]
    B_BUDGET = 55.199987
    return processors, tasks, B_BUDGET
