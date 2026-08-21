"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519999, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519999, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.001449, 'e_o_k': [0.101773, 0.081419, 0.065135, 0.052108], 'p_i': 10, 'u_i': 1.6879},
        {'id': 1, 'e_m': 1.534208, 'e_o_k': [0.155915, 0.124732, 0.099786, 0.079829], 'p_i': 20, 'u_i': 2.2588},
        {'id': 2, 'e_m': 7.428985, 'e_o_k': [1.238164, 0.990531], 'p_i': 40, 'u_i': 4.0829},
        {'id': 3, 'e_m': 11.291401, 'e_o_k': [1.388287, 1.110630, 0.888504], 'p_i': 80, 'u_i': 1.6866},
        {'id': 4, 'e_m': 0.788885, 'e_o_k': [0.096994, 0.077595, 0.062076], 'p_i': 40, 'u_i': 3.5950},
        {'id': 5, 'e_m': 23.552189, 'e_o_k': [3.925365, 3.140292], 'p_i': 80, 'u_i': 4.2025},
        {'id': 6, 'e_m': 9.305443, 'e_o_k': [1.550907, 1.240726], 'p_i': 40, 'u_i': 3.6883},
        {'id': 7, 'e_m': 11.961359, 'e_o_k': [1.993560, 1.594848], 'p_i': 80, 'u_i': 1.6967},
    ]
    B_BUDGET = 143.519999
    return processors, tasks, B_BUDGET
