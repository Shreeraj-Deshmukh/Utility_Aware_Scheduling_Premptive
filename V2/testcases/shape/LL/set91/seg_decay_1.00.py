"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.543832, 'e_o_k': [0.135958, 0.135958], 'p_i': 10, 'u_i': 2.8418},
        {'id': 1, 'e_m': 0.195966, 'e_o_k': [0.024496, 0.024496, 0.024496, 0.024496], 'p_i': 20, 'u_i': 1.5566},
        {'id': 2, 'e_m': 6.548072, 'e_o_k': [0.818509, 0.818509, 0.818509, 0.818509], 'p_i': 40, 'u_i': 3.2695},
        {'id': 3, 'e_m': 3.827555, 'e_o_k': [0.956889, 0.956889], 'p_i': 80, 'u_i': 3.8342},
        {'id': 4, 'e_m': 0.151912, 'e_o_k': [0.012659, 0.012659, 0.012659, 0.012659, 0.012659, 0.012659], 'p_i': 20, 'u_i': 4.3734},
        {'id': 5, 'e_m': 0.377358, 'e_o_k': [0.047170, 0.047170, 0.047170, 0.047170], 'p_i': 20, 'u_i': 3.3497},
        {'id': 6, 'e_m': 2.516575, 'e_o_k': [0.314572, 0.314572, 0.314572, 0.314572], 'p_i': 40, 'u_i': 4.2042},
        {'id': 7, 'e_m': 1.395776, 'e_o_k': [0.232629, 0.232629, 0.232629], 'p_i': 40, 'u_i': 1.0373},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
