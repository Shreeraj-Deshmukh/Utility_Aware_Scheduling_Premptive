"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400014, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400014, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.244203, 'e_o_k': [0.254960, 0.203968, 0.163174], 'p_i': 10, 'u_i': 2.0434},
        {'id': 1, 'e_m': 3.938746, 'e_o_k': [0.533810, 0.427048, 0.341638, 0.273311, 0.218648, 0.174919], 'p_i': 20, 'u_i': 3.8464},
        {'id': 2, 'e_m': 14.279143, 'e_o_k': [1.935221, 1.548177, 1.238541, 0.990833, 0.792666, 0.634133], 'p_i': 40, 'u_i': 4.9550},
        {'id': 3, 'e_m': 9.733109, 'e_o_k': [1.447690, 1.158152, 0.926522, 0.741217, 0.592974], 'p_i': 80, 'u_i': 4.5167},
    ]
    B_BUDGET = 110.400014
    return processors, tasks, B_BUDGET
