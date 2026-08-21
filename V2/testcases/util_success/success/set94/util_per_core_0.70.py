"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439993, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439993, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.168357, 'e_o_k': [0.118735, 0.094988, 0.075991, 0.060793], 'p_i': 10, 'u_i': 1.6879},
        {'id': 1, 'e_m': 1.789909, 'e_o_k': [0.181901, 0.145521, 0.116417, 0.093133], 'p_i': 20, 'u_i': 2.2588},
        {'id': 2, 'e_m': 8.667150, 'e_o_k': [1.444525, 1.155620], 'p_i': 40, 'u_i': 4.0829},
        {'id': 3, 'e_m': 13.173302, 'e_o_k': [1.619668, 1.295735, 1.036588], 'p_i': 80, 'u_i': 1.6866},
        {'id': 4, 'e_m': 0.920365, 'e_o_k': [0.113160, 0.090528, 0.072422], 'p_i': 40, 'u_i': 3.5950},
        {'id': 5, 'e_m': 27.477554, 'e_o_k': [4.579592, 3.663674], 'p_i': 80, 'u_i': 4.2025},
        {'id': 6, 'e_m': 10.856350, 'e_o_k': [1.809392, 1.447513], 'p_i': 40, 'u_i': 3.6883},
        {'id': 7, 'e_m': 13.954919, 'e_o_k': [2.325820, 1.860656], 'p_i': 80, 'u_i': 1.6967},
    ]
    B_BUDGET = 167.439993
    return processors, tasks, B_BUDGET
