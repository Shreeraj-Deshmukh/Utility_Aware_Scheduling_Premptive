"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.028401, 'e_o_k': [1.577645, 1.262116], 'p_i': 10, 'u_i': 1.1535},
        {'id': 1, 'e_m': 1.732749, 'e_o_k': [0.821765, 0.657412, 0.525929, 0.420743], 'p_i': 20, 'u_i': 2.8332},
        {'id': 2, 'e_m': 2.718634, 'e_o_k': [2.114493, 1.691595], 'p_i': 40, 'u_i': 2.4233},
        {'id': 3, 'e_m': 35.404529, 'e_o_k': [13.435234, 10.748187, 8.598550, 6.878840, 5.503072, 4.402458], 'p_i': 80, 'u_i': 4.2523},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
