"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.259839, 'e_o_k': [0.941151, 0.752921, 0.602337, 0.481870, 0.385496], 'p_i': 10, 'u_i': 3.3453},
        {'id': 1, 'e_m': 6.374227, 'e_o_k': [3.657343, 2.925874, 2.340700], 'p_i': 20, 'u_i': 2.8841},
        {'id': 2, 'e_m': 9.556570, 'e_o_k': [5.483278, 4.386622, 3.509298], 'p_i': 40, 'u_i': 2.2513},
        {'id': 3, 'e_m': 1.311243, 'e_o_k': [0.621863, 0.497491, 0.397992, 0.318394], 'p_i': 80, 'u_i': 1.5109},
    ]
    B_BUDGET = 176.640008
    return processors, tasks, B_BUDGET
