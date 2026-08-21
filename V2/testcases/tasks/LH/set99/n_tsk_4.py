"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319992, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319992, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.042066, 'e_o_k': [0.597907, 0.478325, 0.382660], 'p_i': 10, 'u_i': 2.9415},
        {'id': 1, 'e_m': 2.975949, 'e_o_k': [2.314627, 1.851702], 'p_i': 20, 'u_i': 4.1135},
        {'id': 2, 'e_m': 1.326184, 'e_o_k': [0.503258, 0.402606, 0.322085, 0.257668, 0.206134, 0.164907], 'p_i': 40, 'u_i': 3.4980},
        {'id': 3, 'e_m': 9.107305, 'e_o_k': [7.083460, 5.666768], 'p_i': 80, 'u_i': 2.1751},
    ]
    B_BUDGET = 88.319992
    return processors, tasks, B_BUDGET
