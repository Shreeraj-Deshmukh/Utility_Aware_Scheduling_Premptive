"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639998, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639998, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.691442, 'e_o_k': [0.396729, 0.317383, 0.253907], 'p_i': 10, 'u_i': 2.6945},
        {'id': 1, 'e_m': 3.651177, 'e_o_k': [2.094938, 1.675950, 1.340760], 'p_i': 20, 'u_i': 2.2851},
        {'id': 2, 'e_m': 5.369710, 'e_o_k': [3.080981, 2.464785, 1.971828], 'p_i': 40, 'u_i': 1.9156},
        {'id': 3, 'e_m': 9.653701, 'e_o_k': [5.539009, 4.431207, 3.544966], 'p_i': 80, 'u_i': 2.3867},
        {'id': 4, 'e_m': 0.756812, 'e_o_k': [0.434237, 0.347389, 0.277911], 'p_i': 10, 'u_i': 1.9527},
        {'id': 5, 'e_m': 0.749641, 'e_o_k': [0.430122, 0.344097, 0.275278], 'p_i': 10, 'u_i': 2.5555},
        {'id': 6, 'e_m': 6.748626, 'e_o_k': [3.872163, 3.097730, 2.478184], 'p_i': 80, 'u_i': 2.5749},
        {'id': 7, 'e_m': 2.335192, 'e_o_k': [1.339864, 1.071891, 0.857513], 'p_i': 40, 'u_i': 4.5972},
    ]
    B_BUDGET = 176.639998
    return processors, tasks, B_BUDGET
