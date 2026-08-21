"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200006, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200006, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.877722, 'e_o_k': [0.243812, 0.195049], 'p_i': 10, 'u_i': 2.2749},
        {'id': 1, 'e_m': 0.626081, 'e_o_k': [0.173911, 0.139129], 'p_i': 20, 'u_i': 4.9536},
        {'id': 2, 'e_m': 2.383329, 'e_o_k': [0.662036, 0.529629], 'p_i': 40, 'u_i': 2.9112},
        {'id': 3, 'e_m': 0.098499, 'e_o_k': [0.027361, 0.021889], 'p_i': 80, 'u_i': 2.1467},
        {'id': 4, 'e_m': 0.036647, 'e_o_k': [0.010180, 0.008144], 'p_i': 10, 'u_i': 3.3563},
        {'id': 5, 'e_m': 5.989060, 'e_o_k': [1.663628, 1.330902], 'p_i': 80, 'u_i': 2.2972},
        {'id': 6, 'e_m': 0.258182, 'e_o_k': [0.071717, 0.057374], 'p_i': 10, 'u_i': 3.3121},
        {'id': 7, 'e_m': 4.630526, 'e_o_k': [1.286257, 1.029006], 'p_i': 40, 'u_i': 4.6359},
    ]
    B_BUDGET = 55.200006
    return processors, tasks, B_BUDGET
