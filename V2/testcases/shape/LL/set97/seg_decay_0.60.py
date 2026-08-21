"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.350656, 'e_o_k': [0.076044, 0.045627, 0.027376, 0.016426, 0.009855], 'p_i': 10, 'u_i': 4.4298},
        {'id': 1, 'e_m': 3.430445, 'e_o_k': [0.875114, 0.525068, 0.315041], 'p_i': 20, 'u_i': 1.5050},
        {'id': 2, 'e_m': 0.207300, 'e_o_k': [0.064781, 0.038869], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 1.714842, 'e_o_k': [0.359753, 0.215852, 0.129511, 0.077707, 0.046624, 0.027974], 'p_i': 80, 'u_i': 4.0993},
        {'id': 4, 'e_m': 0.699429, 'e_o_k': [0.218571, 0.131143], 'p_i': 20, 'u_i': 2.5958},
        {'id': 5, 'e_m': 2.747339, 'e_o_k': [0.700852, 0.420511, 0.252307], 'p_i': 80, 'u_i': 1.3643},
        {'id': 6, 'e_m': 2.551296, 'e_o_k': [0.535231, 0.321139, 0.192683, 0.115610, 0.069366, 0.041620], 'p_i': 40, 'u_i': 1.6218},
        {'id': 7, 'e_m': 2.695881, 'e_o_k': [0.619458, 0.371675, 0.223005, 0.133803], 'p_i': 80, 'u_i': 1.2955},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
