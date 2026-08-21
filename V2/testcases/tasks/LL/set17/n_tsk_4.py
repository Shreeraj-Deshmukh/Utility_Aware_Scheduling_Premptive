"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.865247, 'e_o_k': [0.240346, 0.192277], 'p_i': 10, 'u_i': 2.4127},
        {'id': 1, 'e_m': 1.272744, 'e_o_k': [0.353540, 0.282832], 'p_i': 20, 'u_i': 2.1691},
        {'id': 2, 'e_m': 8.086986, 'e_o_k': [2.246385, 1.797108], 'p_i': 40, 'u_i': 3.6581},
        {'id': 3, 'e_m': 3.813078, 'e_o_k': [0.567152, 0.453722, 0.362977, 0.290382, 0.232306], 'p_i': 80, 'u_i': 4.4037},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
