"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639986, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639986, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.111464, 'e_o_k': [1.295826, 1.036661, 0.829329, 0.663463, 0.530770], 'p_i': 10, 'u_i': 2.5478},
        {'id': 1, 'e_m': 1.077629, 'e_o_k': [0.511071, 0.408857, 0.327085, 0.261668], 'p_i': 20, 'u_i': 1.9017},
        {'id': 2, 'e_m': 12.270583, 'e_o_k': [9.543787, 7.635029], 'p_i': 40, 'u_i': 4.1004},
        {'id': 3, 'e_m': 10.256603, 'e_o_k': [4.864242, 3.891394, 3.113115, 2.490492], 'p_i': 80, 'u_i': 2.6358},
    ]
    B_BUDGET = 176.639986
    return processors, tasks, B_BUDGET
