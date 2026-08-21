"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.497956, 'e_o_k': [0.859483, 0.687586, 0.550069], 'p_i': 10, 'u_i': 4.6460},
        {'id': 1, 'e_m': 4.003375, 'e_o_k': [1.519192, 1.215354, 0.972283, 0.777826, 0.622261, 0.497809], 'p_i': 20, 'u_i': 1.6535},
        {'id': 2, 'e_m': 1.734763, 'e_o_k': [0.722474, 0.577979, 0.462383, 0.369907, 0.295925], 'p_i': 40, 'u_i': 3.3613},
        {'id': 3, 'e_m': 32.533327, 'e_o_k': [15.429085, 12.343268, 9.874614, 7.899691], 'p_i': 80, 'u_i': 3.4647},
    ]
    B_BUDGET = 176.639999
    return processors, tasks, B_BUDGET
