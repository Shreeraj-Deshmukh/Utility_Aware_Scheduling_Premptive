"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.792640, 'e_o_k': [0.330110, 0.264088, 0.211270, 0.169016, 0.135213], 'p_i': 10, 'u_i': 3.7039},
        {'id': 1, 'e_m': 3.276966, 'e_o_k': [1.243536, 0.994829, 0.795863, 0.636690, 0.509352, 0.407482], 'p_i': 20, 'u_i': 3.4878},
        {'id': 2, 'e_m': 6.056555, 'e_o_k': [2.522363, 2.017891, 1.614313, 1.291450, 1.033160], 'p_i': 40, 'u_i': 4.7761},
        {'id': 3, 'e_m': 0.437906, 'e_o_k': [0.182374, 0.145899, 0.116719, 0.093375, 0.074700], 'p_i': 80, 'u_i': 2.0030},
    ]
    B_BUDGET = 88.320006
    return processors, tasks, B_BUDGET
