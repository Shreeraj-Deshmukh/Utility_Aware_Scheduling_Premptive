"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199993, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199993, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.694529, 'e_o_k': [0.449088, 0.359271], 'p_i': 10, 'u_i': 4.8534},
        {'id': 1, 'e_m': 8.579653, 'e_o_k': [0.871916, 0.697533, 0.558026, 0.446421], 'p_i': 20, 'u_i': 2.9672},
        {'id': 2, 'e_m': 2.628322, 'e_o_k': [0.213726, 0.170981, 0.136785, 0.109428, 0.087542, 0.070034], 'p_i': 40, 'u_i': 1.4615},
        {'id': 3, 'e_m': 26.872890, 'e_o_k': [2.730985, 2.184788, 1.747830, 1.398264], 'p_i': 80, 'u_i': 3.8621},
        {'id': 4, 'e_m': 8.619621, 'e_o_k': [0.700919, 0.560735, 0.448588, 0.358870, 0.287096, 0.229677], 'p_i': 80, 'u_i': 3.9454},
        {'id': 5, 'e_m': 2.901562, 'e_o_k': [0.356749, 0.285400, 0.228320], 'p_i': 20, 'u_i': 3.6493},
        {'id': 6, 'e_m': 9.303917, 'e_o_k': [1.143924, 0.915139, 0.732112], 'p_i': 20, 'u_i': 1.5799},
        {'id': 7, 'e_m': 14.554079, 'e_o_k': [1.298853, 1.039082, 0.831266, 0.665013, 0.532010], 'p_i': 80, 'u_i': 3.4745},
    ]
    B_BUDGET = 239.199993
    return processors, tasks, B_BUDGET
