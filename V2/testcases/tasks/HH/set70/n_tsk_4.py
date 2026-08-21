"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.375582, 'e_o_k': [1.126631, 0.901305, 0.721044, 0.576835], 'p_i': 10, 'u_i': 4.7862},
        {'id': 1, 'e_m': 7.872693, 'e_o_k': [4.517119, 3.613695, 2.890956], 'p_i': 20, 'u_i': 1.7928},
        {'id': 2, 'e_m': 6.657481, 'e_o_k': [5.178041, 4.142433], 'p_i': 40, 'u_i': 1.8882},
        {'id': 3, 'e_m': 0.189608, 'e_o_k': [0.078966, 0.063172, 0.050538, 0.040430, 0.032344], 'p_i': 80, 'u_i': 2.0463},
    ]
    B_BUDGET = 176.639995
    return processors, tasks, B_BUDGET
