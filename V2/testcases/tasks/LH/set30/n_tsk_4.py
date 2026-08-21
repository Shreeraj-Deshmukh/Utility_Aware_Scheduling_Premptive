"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.056959, 'e_o_k': [0.032681, 0.026145, 0.020916], 'p_i': 10, 'u_i': 4.7642},
        {'id': 1, 'e_m': 2.740391, 'e_o_k': [1.141286, 0.913029, 0.730423, 0.584338, 0.467471], 'p_i': 20, 'u_i': 4.7668},
        {'id': 2, 'e_m': 4.138949, 'e_o_k': [1.570640, 1.256512, 1.005209, 0.804167, 0.643334, 0.514667], 'p_i': 40, 'u_i': 4.7724},
        {'id': 3, 'e_m': 12.304866, 'e_o_k': [5.124587, 4.099670, 3.279736, 2.623789, 2.099031], 'p_i': 80, 'u_i': 4.0150},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET
