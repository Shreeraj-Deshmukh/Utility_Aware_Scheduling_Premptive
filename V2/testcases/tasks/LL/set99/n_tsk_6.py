"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.20001, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.20001, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.662532, 'e_o_k': [0.089792, 0.071833, 0.057467, 0.045973, 0.036779, 0.029423], 'p_i': 10, 'u_i': 3.4980},
        {'id': 1, 'e_m': 1.969439, 'e_o_k': [0.547066, 0.437653], 'p_i': 20, 'u_i': 2.1751},
        {'id': 2, 'e_m': 0.768607, 'e_o_k': [0.114322, 0.091457, 0.073166, 0.058533, 0.046826], 'p_i': 40, 'u_i': 4.1688},
        {'id': 3, 'e_m': 2.851730, 'e_o_k': [0.584371, 0.467497, 0.373997], 'p_i': 80, 'u_i': 2.2140},
        {'id': 4, 'e_m': 0.928463, 'e_o_k': [0.190259, 0.152207, 0.121766], 'p_i': 10, 'u_i': 3.2266},
        {'id': 5, 'e_m': 0.875668, 'e_o_k': [0.118677, 0.094942, 0.075953, 0.060763, 0.048610, 0.038888], 'p_i': 10, 'u_i': 3.3398},
    ]
    B_BUDGET = 55.200010
    return processors, tasks, B_BUDGET
