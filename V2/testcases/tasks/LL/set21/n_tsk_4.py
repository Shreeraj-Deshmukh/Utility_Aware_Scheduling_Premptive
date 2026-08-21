"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.760654, 'e_o_k': [0.128837, 0.103070, 0.082456, 0.065965], 'p_i': 10, 'u_i': 3.1389},
        {'id': 1, 'e_m': 3.743173, 'e_o_k': [0.507304, 0.405843, 0.324675, 0.259740, 0.207792, 0.166233], 'p_i': 20, 'u_i': 2.7195},
        {'id': 2, 'e_m': 4.127417, 'e_o_k': [0.613907, 0.491125, 0.392900, 0.314320, 0.251456], 'p_i': 40, 'u_i': 2.3377},
        {'id': 3, 'e_m': 2.687240, 'e_o_k': [0.746456, 0.597164], 'p_i': 80, 'u_i': 4.2462},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
