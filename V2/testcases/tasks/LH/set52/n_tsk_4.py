"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.083997, 'e_o_k': [0.048195, 0.038556, 0.030845], 'p_i': 10, 'u_i': 2.9413},
        {'id': 1, 'e_m': 1.581251, 'e_o_k': [0.907275, 0.725820, 0.580656], 'p_i': 20, 'u_i': 2.0448},
        {'id': 2, 'e_m': 10.971554, 'e_o_k': [4.569305, 3.655444, 2.924355, 2.339484, 1.871587], 'p_i': 40, 'u_i': 1.6984},
        {'id': 3, 'e_m': 3.059915, 'e_o_k': [1.451179, 1.160943, 0.928755, 0.743004], 'p_i': 80, 'u_i': 3.4597},
    ]
    B_BUDGET = 88.320007
    return processors, tasks, B_BUDGET
