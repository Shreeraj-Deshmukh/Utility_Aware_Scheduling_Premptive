"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.740709, 'e_o_k': [0.235914, 0.188732, 0.150985, 0.120788, 0.096631, 0.077304], 'p_i': 10, 'u_i': 2.9138},
        {'id': 1, 'e_m': 1.364099, 'e_o_k': [0.279529, 0.223623, 0.178898], 'p_i': 20, 'u_i': 3.0119},
        {'id': 2, 'e_m': 5.819442, 'e_o_k': [1.192509, 0.954007, 0.763205], 'p_i': 40, 'u_i': 1.8562},
        {'id': 3, 'e_m': 0.979047, 'e_o_k': [0.271957, 0.217566], 'p_i': 80, 'u_i': 1.1264},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET
