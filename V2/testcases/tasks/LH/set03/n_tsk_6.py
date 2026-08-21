"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.521509, 'e_o_k': [0.405618, 0.324494], 'p_i': 10, 'u_i': 2.9022},
        {'id': 1, 'e_m': 1.568163, 'e_o_k': [0.653090, 0.522472, 0.417978, 0.334382, 0.267506], 'p_i': 20, 'u_i': 3.0103},
        {'id': 2, 'e_m': 1.108635, 'e_o_k': [0.525775, 0.420620, 0.336496, 0.269197], 'p_i': 40, 'u_i': 4.4931},
        {'id': 3, 'e_m': 6.413023, 'e_o_k': [2.433600, 1.946880, 1.557504, 1.246003, 0.996803, 0.797442], 'p_i': 80, 'u_i': 4.6084},
        {'id': 4, 'e_m': 0.883165, 'e_o_k': [0.686906, 0.549525], 'p_i': 10, 'u_i': 3.5739},
        {'id': 5, 'e_m': 2.929834, 'e_o_k': [1.111807, 0.889446, 0.711556, 0.569245, 0.455396, 0.364317], 'p_i': 40, 'u_i': 3.1864},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET
