"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200002, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200002, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.460174, 'e_o_k': [0.405604, 0.324483], 'p_i': 10, 'u_i': 1.9752},
        {'id': 1, 'e_m': 0.417207, 'e_o_k': [0.115891, 0.092713], 'p_i': 20, 'u_i': 3.9662},
        {'id': 2, 'e_m': 2.317386, 'e_o_k': [0.643718, 0.514975], 'p_i': 40, 'u_i': 1.9890},
        {'id': 3, 'e_m': 0.317304, 'e_o_k': [0.088140, 0.070512], 'p_i': 80, 'u_i': 3.3639},
        {'id': 4, 'e_m': 1.728593, 'e_o_k': [0.480165, 0.384132], 'p_i': 40, 'u_i': 4.7869},
        {'id': 5, 'e_m': 0.210554, 'e_o_k': [0.058487, 0.046790], 'p_i': 10, 'u_i': 2.7944},
        {'id': 6, 'e_m': 0.207004, 'e_o_k': [0.057501, 0.046001], 'p_i': 10, 'u_i': 4.7769},
        {'id': 7, 'e_m': 0.862507, 'e_o_k': [0.239585, 0.191668], 'p_i': 10, 'u_i': 1.3167},
    ]
    B_BUDGET = 55.200002
    return processors, tasks, B_BUDGET
