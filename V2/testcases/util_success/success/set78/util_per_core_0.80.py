"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359992, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359992, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.572880, 'e_o_k': [0.464724, 0.371779, 0.297423, 0.237938], 'p_i': 10, 'u_i': 1.7025},
        {'id': 1, 'e_m': 2.886481, 'e_o_k': [0.257599, 0.206079, 0.164863, 0.131891, 0.105512], 'p_i': 20, 'u_i': 2.0058},
        {'id': 2, 'e_m': 2.244860, 'e_o_k': [0.374143, 0.299315], 'p_i': 40, 'u_i': 3.5722},
        {'id': 3, 'e_m': 39.628553, 'e_o_k': [4.027292, 3.221834, 2.577467, 2.061973], 'p_i': 80, 'u_i': 1.2384},
        {'id': 4, 'e_m': 3.699601, 'e_o_k': [0.616600, 0.493280], 'p_i': 40, 'u_i': 4.5379},
        {'id': 5, 'e_m': 5.245527, 'e_o_k': [0.874255, 0.699404], 'p_i': 20, 'u_i': 1.9982},
        {'id': 6, 'e_m': 0.611036, 'e_o_k': [0.101839, 0.081471], 'p_i': 20, 'u_i': 2.1252},
        {'id': 7, 'e_m': 4.927305, 'e_o_k': [0.500742, 0.400594, 0.320475, 0.256380], 'p_i': 80, 'u_i': 4.2384},
    ]
    B_BUDGET = 191.359992
    return processors, tasks, B_BUDGET
