"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640009, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640009, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.699031, 'e_o_k': [0.291124, 0.232900, 0.186320, 0.149056, 0.119245], 'p_i': 10, 'u_i': 3.1382},
        {'id': 1, 'e_m': 0.284346, 'e_o_k': [0.118421, 0.094737, 0.075790, 0.060632, 0.048505], 'p_i': 20, 'u_i': 3.0103},
        {'id': 2, 'e_m': 14.461026, 'e_o_k': [8.297310, 6.637848, 5.310278], 'p_i': 40, 'u_i': 3.7408},
        {'id': 3, 'e_m': 8.776006, 'e_o_k': [6.825782, 5.460626], 'p_i': 80, 'u_i': 2.8589},
        {'id': 4, 'e_m': 8.970280, 'e_o_k': [5.146882, 4.117506, 3.294005], 'p_i': 40, 'u_i': 2.7598},
        {'id': 5, 'e_m': 0.203968, 'e_o_k': [0.158642, 0.126914], 'p_i': 10, 'u_i': 2.0735},
    ]
    B_BUDGET = 176.640009
    return processors, tasks, B_BUDGET
