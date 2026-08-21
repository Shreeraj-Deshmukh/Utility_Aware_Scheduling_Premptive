"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519984, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519984, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.208984, 'e_o_k': [0.018650, 0.014920, 0.011936, 0.009549, 0.007639], 'p_i': 10, 'u_i': 1.7922},
        {'id': 1, 'e_m': 4.773908, 'e_o_k': [0.485153, 0.388123, 0.310498, 0.248398], 'p_i': 20, 'u_i': 4.9529},
        {'id': 2, 'e_m': 6.660217, 'e_o_k': [1.110036, 0.888029], 'p_i': 40, 'u_i': 2.3587},
        {'id': 3, 'e_m': 2.631008, 'e_o_k': [0.438501, 0.350801], 'p_i': 80, 'u_i': 4.5300},
        {'id': 4, 'e_m': 1.168749, 'e_o_k': [0.095039, 0.076031, 0.060825, 0.048660, 0.038928, 0.031142], 'p_i': 80, 'u_i': 3.1308},
        {'id': 5, 'e_m': 13.845560, 'e_o_k': [1.125875, 0.900700, 0.720560, 0.576448, 0.461158, 0.368927], 'p_i': 40, 'u_i': 2.3635},
        {'id': 6, 'e_m': 22.115817, 'e_o_k': [2.719158, 2.175326, 1.740261], 'p_i': 80, 'u_i': 1.8340},
        {'id': 7, 'e_m': 1.038171, 'e_o_k': [0.084421, 0.067536, 0.054029, 0.043223, 0.034579, 0.027663], 'p_i': 10, 'u_i': 2.0052},
    ]
    B_BUDGET = 143.519984
    return processors, tasks, B_BUDGET
