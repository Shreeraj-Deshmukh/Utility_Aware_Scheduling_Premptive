"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.481418, 'e_o_k': [1.321121, 1.056897, 0.845517, 0.676414, 0.541131, 0.432905], 'p_i': 10, 'u_i': 2.9138},
        {'id': 1, 'e_m': 2.728199, 'e_o_k': [1.565360, 1.252288, 1.001830], 'p_i': 20, 'u_i': 3.0119},
        {'id': 2, 'e_m': 11.638883, 'e_o_k': [6.678048, 5.342438, 4.273951], 'p_i': 40, 'u_i': 1.8562},
        {'id': 3, 'e_m': 1.958093, 'e_o_k': [1.522961, 1.218369], 'p_i': 80, 'u_i': 1.1264},
    ]
    B_BUDGET = 176.639994
    return processors, tasks, B_BUDGET
