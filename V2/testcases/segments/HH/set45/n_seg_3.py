"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639977, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639977, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.095169, 'e_o_k': [0.054605, 0.043684, 0.034947], 'p_i': 10, 'u_i': 1.5331},
        {'id': 1, 'e_m': 0.997826, 'e_o_k': [0.572523, 0.458018, 0.366415], 'p_i': 20, 'u_i': 4.3760},
        {'id': 2, 'e_m': 0.022485, 'e_o_k': [0.012901, 0.010321, 0.008257], 'p_i': 40, 'u_i': 3.1042},
        {'id': 3, 'e_m': 2.231053, 'e_o_k': [1.280112, 1.024090, 0.819272], 'p_i': 80, 'u_i': 3.0115},
        {'id': 4, 'e_m': 6.335688, 'e_o_k': [3.635231, 2.908185, 2.326548], 'p_i': 80, 'u_i': 1.0080},
        {'id': 5, 'e_m': 9.200112, 'e_o_k': [5.278753, 4.223002, 3.378402], 'p_i': 80, 'u_i': 3.4234},
        {'id': 6, 'e_m': 6.435349, 'e_o_k': [3.692413, 2.953930, 2.363144], 'p_i': 80, 'u_i': 1.9989},
        {'id': 7, 'e_m': 4.375021, 'e_o_k': [2.510258, 2.008206, 1.606565], 'p_i': 10, 'u_i': 4.9421},
    ]
    B_BUDGET = 176.639977
    return processors, tasks, B_BUDGET
