"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.001779, 'e_o_k': [0.380153, 0.304122, 0.243298, 0.194638, 0.155711, 0.124569], 'p_i': 10, 'u_i': 3.5500},
        {'id': 1, 'e_m': 0.072069, 'e_o_k': [0.041351, 0.033081, 0.026465], 'p_i': 20, 'u_i': 2.3662},
        {'id': 2, 'e_m': 4.582147, 'e_o_k': [3.563892, 2.851114], 'p_i': 40, 'u_i': 3.8013},
        {'id': 3, 'e_m': 14.533199, 'e_o_k': [8.338721, 6.670977, 5.336781], 'p_i': 80, 'u_i': 4.3808},
    ]
    B_BUDGET = 88.320009
    return processors, tasks, B_BUDGET
