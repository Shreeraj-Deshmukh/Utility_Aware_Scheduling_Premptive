"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.830835, 'e_o_k': [0.346016, 0.276813, 0.221451, 0.177160, 0.141728], 'p_i': 10, 'u_i': 3.1570},
        {'id': 1, 'e_m': 2.535383, 'e_o_k': [1.055907, 0.844725, 0.675780, 0.540624, 0.432499], 'p_i': 20, 'u_i': 1.1037},
        {'id': 2, 'e_m': 2.113969, 'e_o_k': [1.002560, 0.802048, 0.641638, 0.513311], 'p_i': 40, 'u_i': 1.2642},
        {'id': 3, 'e_m': 10.983853, 'e_o_k': [4.168129, 3.334503, 2.667602, 2.134082, 1.707265, 1.365812], 'p_i': 80, 'u_i': 2.8053},
    ]
    B_BUDGET = 88.319993
    return processors, tasks, B_BUDGET
