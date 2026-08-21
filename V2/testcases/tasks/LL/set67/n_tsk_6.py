"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200008, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200008, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.280173, 'e_o_k': [0.386208, 0.308967, 0.247173, 0.197739], 'p_i': 10, 'u_i': 1.8147},
        {'id': 1, 'e_m': 0.059600, 'e_o_k': [0.010095, 0.008076, 0.006461, 0.005169], 'p_i': 20, 'u_i': 2.7697},
        {'id': 2, 'e_m': 2.975935, 'e_o_k': [0.403322, 0.322658, 0.258126, 0.206501, 0.165201, 0.132161], 'p_i': 40, 'u_i': 2.4720},
        {'id': 3, 'e_m': 1.390599, 'e_o_k': [0.386278, 0.309022], 'p_i': 80, 'u_i': 3.3220},
        {'id': 4, 'e_m': 4.200429, 'e_o_k': [1.166786, 0.933429], 'p_i': 80, 'u_i': 2.5309},
        {'id': 5, 'e_m': 0.494329, 'e_o_k': [0.101297, 0.081037, 0.064830], 'p_i': 20, 'u_i': 3.7128},
    ]
    B_BUDGET = 55.200008
    return processors, tasks, B_BUDGET
