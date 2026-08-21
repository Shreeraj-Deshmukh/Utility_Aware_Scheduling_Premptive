"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520009, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520009, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.646848, 'e_o_k': [0.167363, 0.133890, 0.107112, 0.085690], 'p_i': 10, 'u_i': 3.8216},
        {'id': 1, 'e_m': 1.583832, 'e_o_k': [0.194734, 0.155787, 0.124629], 'p_i': 20, 'u_i': 4.3612},
        {'id': 2, 'e_m': 13.873994, 'e_o_k': [1.409959, 1.127967, 0.902374, 0.721899], 'p_i': 40, 'u_i': 2.3108},
        {'id': 3, 'e_m': 7.485740, 'e_o_k': [0.760746, 0.608597, 0.486877, 0.389502], 'p_i': 80, 'u_i': 1.0383},
        {'id': 4, 'e_m': 0.738210, 'e_o_k': [0.123035, 0.098428], 'p_i': 20, 'u_i': 2.0614},
        {'id': 5, 'e_m': 2.383812, 'e_o_k': [0.242257, 0.193806, 0.155045, 0.124036], 'p_i': 10, 'u_i': 4.6739},
        {'id': 6, 'e_m': 0.194043, 'e_o_k': [0.019720, 0.015776, 0.012621, 0.010097], 'p_i': 10, 'u_i': 3.1717},
        {'id': 7, 'e_m': 4.420118, 'e_o_k': [0.359429, 0.287543, 0.230035, 0.184028, 0.147222, 0.117778], 'p_i': 20, 'u_i': 4.1313},
    ]
    B_BUDGET = 143.520009
    return processors, tasks, B_BUDGET
