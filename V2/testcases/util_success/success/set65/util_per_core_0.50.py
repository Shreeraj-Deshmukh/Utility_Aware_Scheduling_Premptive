"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600009, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600009, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.159759, 'e_o_k': [0.016236, 0.012989, 0.010391, 0.008313], 'p_i': 10, 'u_i': 3.7146},
        {'id': 1, 'e_m': 5.797859, 'e_o_k': [0.712851, 0.570281, 0.456225], 'p_i': 20, 'u_i': 2.7971},
        {'id': 2, 'e_m': 1.000988, 'e_o_k': [0.123072, 0.098458, 0.078766], 'p_i': 40, 'u_i': 1.6396},
        {'id': 3, 'e_m': 11.797325, 'e_o_k': [1.450491, 1.160393, 0.928314], 'p_i': 80, 'u_i': 4.1445},
        {'id': 4, 'e_m': 4.353911, 'e_o_k': [0.442471, 0.353977, 0.283181, 0.226545], 'p_i': 20, 'u_i': 4.6205},
        {'id': 5, 'e_m': 18.154546, 'e_o_k': [1.476267, 1.181014, 0.944811, 0.755849, 0.604679, 0.483743], 'p_i': 80, 'u_i': 1.3665},
        {'id': 6, 'e_m': 0.091694, 'e_o_k': [0.009319, 0.007455, 0.005964, 0.004771], 'p_i': 20, 'u_i': 3.3652},
        {'id': 7, 'e_m': 1.448555, 'e_o_k': [0.129274, 0.103419, 0.082735, 0.066188, 0.052951], 'p_i': 20, 'u_i': 2.1692},
    ]
    B_BUDGET = 119.600009
    return processors, tasks, B_BUDGET
