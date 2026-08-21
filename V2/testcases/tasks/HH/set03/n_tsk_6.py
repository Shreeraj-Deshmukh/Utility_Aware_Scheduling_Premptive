"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639998, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639998, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.043017, 'e_o_k': [0.811236, 0.648989], 'p_i': 10, 'u_i': 2.9022},
        {'id': 1, 'e_m': 3.136325, 'e_o_k': [1.306180, 1.044944, 0.835955, 0.668764, 0.535011], 'p_i': 20, 'u_i': 3.0103},
        {'id': 2, 'e_m': 2.217270, 'e_o_k': [1.051551, 0.841241, 0.672992, 0.538394], 'p_i': 40, 'u_i': 4.4931},
        {'id': 3, 'e_m': 12.826047, 'e_o_k': [4.867201, 3.893760, 3.115008, 2.492007, 1.993605, 1.594884], 'p_i': 80, 'u_i': 4.6084},
        {'id': 4, 'e_m': 1.766330, 'e_o_k': [1.373812, 1.099050], 'p_i': 10, 'u_i': 3.5739},
        {'id': 5, 'e_m': 5.859667, 'e_o_k': [2.223614, 1.778891, 1.423113, 1.138490, 0.910792, 0.728634], 'p_i': 40, 'u_i': 3.1864},
    ]
    B_BUDGET = 176.639998
    return processors, tasks, B_BUDGET
