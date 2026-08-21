"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.497956, 'e_o_k': [0.306958, 0.245567, 0.196453], 'p_i': 10, 'u_i': 4.6460},
        {'id': 1, 'e_m': 4.003375, 'e_o_k': [0.542569, 0.434055, 0.347244, 0.277795, 0.222236, 0.177789], 'p_i': 20, 'u_i': 1.6535},
        {'id': 2, 'e_m': 1.734763, 'e_o_k': [0.258026, 0.206421, 0.165137, 0.132110, 0.105688], 'p_i': 40, 'u_i': 3.3613},
        {'id': 3, 'e_m': 32.533327, 'e_o_k': [5.510387, 4.408310, 3.526648, 2.821318], 'p_i': 80, 'u_i': 3.4647},
    ]
    B_BUDGET = 110.400005
    return processors, tasks, B_BUDGET
