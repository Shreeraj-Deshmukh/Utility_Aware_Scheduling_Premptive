"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639993, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639993, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.083295, 'e_o_k': [0.411086, 0.328869, 0.263095, 0.210476, 0.168381, 0.134705], 'p_i': 10, 'u_i': 3.6469},
        {'id': 1, 'e_m': 0.351454, 'e_o_k': [0.146369, 0.117096, 0.093676, 0.074941, 0.059953], 'p_i': 20, 'u_i': 1.4903},
        {'id': 2, 'e_m': 5.041036, 'e_o_k': [2.390735, 1.912588, 1.530071, 1.224056], 'p_i': 40, 'u_i': 2.4704},
        {'id': 3, 'e_m': 2.805236, 'e_o_k': [1.609562, 1.287649, 1.030119], 'p_i': 80, 'u_i': 4.2349},
        {'id': 4, 'e_m': 8.758930, 'e_o_k': [3.323820, 2.659056, 2.127245, 1.701796, 1.361437, 1.089149], 'p_i': 40, 'u_i': 4.1771},
        {'id': 5, 'e_m': 11.761329, 'e_o_k': [5.577866, 4.462293, 3.569834, 2.855867], 'p_i': 40, 'u_i': 4.0903},
    ]
    B_BUDGET = 176.639993
    return processors, tasks, B_BUDGET
