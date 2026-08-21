"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.31998, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.31998, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.543832, 'e_o_k': [0.380682, 0.380682], 'p_i': 10, 'u_i': 2.8418},
        {'id': 1, 'e_m': 0.195966, 'e_o_k': [0.068588, 0.068588, 0.068588, 0.068588], 'p_i': 20, 'u_i': 1.5566},
        {'id': 2, 'e_m': 6.548072, 'e_o_k': [2.291825, 2.291825, 2.291825, 2.291825], 'p_i': 40, 'u_i': 3.2695},
        {'id': 3, 'e_m': 3.827555, 'e_o_k': [2.679289, 2.679289], 'p_i': 80, 'u_i': 3.8342},
        {'id': 4, 'e_m': 0.151912, 'e_o_k': [0.035446, 0.035446, 0.035446, 0.035446, 0.035446, 0.035446], 'p_i': 20, 'u_i': 4.3734},
        {'id': 5, 'e_m': 0.377358, 'e_o_k': [0.132075, 0.132075, 0.132075, 0.132075], 'p_i': 20, 'u_i': 3.3497},
        {'id': 6, 'e_m': 2.516575, 'e_o_k': [0.880801, 0.880801, 0.880801, 0.880801], 'p_i': 40, 'u_i': 4.2042},
        {'id': 7, 'e_m': 1.395776, 'e_o_k': [0.651362, 0.651362, 0.651362], 'p_i': 40, 'u_i': 1.0373},
    ]
    B_BUDGET = 88.319980
    return processors, tasks, B_BUDGET
