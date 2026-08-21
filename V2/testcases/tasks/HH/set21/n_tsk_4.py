"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.521308, 'e_o_k': [0.721488, 0.577190, 0.461752, 0.369402], 'p_i': 10, 'u_i': 3.1389},
        {'id': 1, 'e_m': 7.486346, 'e_o_k': [2.840902, 2.272722, 1.818178, 1.454542, 1.163634, 0.930907], 'p_i': 20, 'u_i': 2.7195},
        {'id': 2, 'e_m': 8.254834, 'e_o_k': [3.437877, 2.750302, 2.200241, 1.760193, 1.408154], 'p_i': 40, 'u_i': 2.3377},
        {'id': 3, 'e_m': 5.374480, 'e_o_k': [4.180151, 3.344121], 'p_i': 80, 'u_i': 4.2462},
    ]
    B_BUDGET = 176.639998
    return processors, tasks, B_BUDGET
