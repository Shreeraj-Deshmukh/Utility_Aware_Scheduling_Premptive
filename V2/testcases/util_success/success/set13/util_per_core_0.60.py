"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519984, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519984, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.168922, 'e_o_k': [0.020769, 0.016615, 0.013292], 'p_i': 10, 'u_i': 4.5768},
        {'id': 1, 'e_m': 1.030332, 'e_o_k': [0.171722, 0.137378], 'p_i': 20, 'u_i': 3.5463},
        {'id': 2, 'e_m': 3.259164, 'e_o_k': [0.543194, 0.434555], 'p_i': 40, 'u_i': 3.4252},
        {'id': 3, 'e_m': 6.472350, 'e_o_k': [0.657759, 0.526207, 0.420966, 0.336773], 'p_i': 80, 'u_i': 1.2792},
        {'id': 4, 'e_m': 0.571117, 'e_o_k': [0.058040, 0.046432, 0.037146, 0.029717], 'p_i': 10, 'u_i': 2.1862},
        {'id': 5, 'e_m': 12.021933, 'e_o_k': [1.478107, 1.182485, 0.945988], 'p_i': 80, 'u_i': 2.5645},
        {'id': 6, 'e_m': 3.290941, 'e_o_k': [0.334445, 0.267556, 0.214045, 0.171236], 'p_i': 10, 'u_i': 2.2998},
        {'id': 7, 'e_m': 34.618216, 'e_o_k': [4.256338, 3.405070, 2.724056], 'p_i': 80, 'u_i': 1.4896},
    ]
    B_BUDGET = 143.519984
    return processors, tasks, B_BUDGET
