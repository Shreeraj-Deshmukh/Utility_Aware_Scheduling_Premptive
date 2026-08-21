"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.191048, 'e_o_k': [0.564860, 0.451888, 0.361511, 0.289208], 'p_i': 10, 'u_i': 4.3067},
        {'id': 1, 'e_m': 4.049834, 'e_o_k': [1.536822, 1.229458, 0.983566, 0.786853, 0.629482, 0.503586], 'p_i': 20, 'u_i': 4.0634},
        {'id': 2, 'e_m': 8.671761, 'e_o_k': [4.975600, 3.980480, 3.184384], 'p_i': 40, 'u_i': 4.9615},
        {'id': 3, 'e_m': 20.928759, 'e_o_k': [7.942000, 6.353600, 5.082880, 4.066304, 3.253043, 2.602435], 'p_i': 80, 'u_i': 2.0301},
    ]
    B_BUDGET = 176.639994
    return processors, tasks, B_BUDGET
