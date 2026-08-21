"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.485314, 'e_o_k': [0.048531, 0.048531, 0.048531, 0.048531, 0.048531], 'p_i': 10, 'u_i': 1.8657},
        {'id': 1, 'e_m': 1.461505, 'e_o_k': [0.146151, 0.146151, 0.146151, 0.146151, 0.146151], 'p_i': 20, 'u_i': 1.6547},
        {'id': 2, 'e_m': 0.554952, 'e_o_k': [0.069369, 0.069369, 0.069369, 0.069369], 'p_i': 40, 'u_i': 3.2690},
        {'id': 3, 'e_m': 1.824306, 'e_o_k': [0.304051, 0.304051, 0.304051], 'p_i': 80, 'u_i': 2.0883},
        {'id': 4, 'e_m': 0.517558, 'e_o_k': [0.086260, 0.086260, 0.086260], 'p_i': 10, 'u_i': 2.4453},
        {'id': 5, 'e_m': 5.062609, 'e_o_k': [0.506261, 0.506261, 0.506261, 0.506261, 0.506261], 'p_i': 40, 'u_i': 4.4841},
        {'id': 6, 'e_m': 2.445941, 'e_o_k': [0.407657, 0.407657, 0.407657], 'p_i': 40, 'u_i': 2.2759},
        {'id': 7, 'e_m': 0.179690, 'e_o_k': [0.044923, 0.044923], 'p_i': 80, 'u_i': 4.2544},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
