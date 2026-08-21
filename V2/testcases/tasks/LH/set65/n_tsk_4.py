"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.147524, 'e_o_k': [0.069964, 0.055971, 0.044777, 0.035821], 'p_i': 10, 'u_i': 4.6168},
        {'id': 1, 'e_m': 5.000513, 'e_o_k': [1.897584, 1.518067, 1.214454, 0.971563, 0.777250, 0.621800], 'p_i': 20, 'u_i': 1.2568},
        {'id': 2, 'e_m': 0.907188, 'e_o_k': [0.377815, 0.302252, 0.241802, 0.193441, 0.154753], 'p_i': 40, 'u_i': 3.3453},
        {'id': 3, 'e_m': 9.003385, 'e_o_k': [5.165877, 4.132701, 3.306161], 'p_i': 80, 'u_i': 2.8841},
    ]
    B_BUDGET = 88.320007
    return processors, tasks, B_BUDGET
