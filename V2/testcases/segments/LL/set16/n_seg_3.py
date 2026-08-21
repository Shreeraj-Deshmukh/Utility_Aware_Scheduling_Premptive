"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199994, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199994, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.536605, 'e_o_k': [0.109960, 0.087968, 0.070374], 'p_i': 10, 'u_i': 3.4396},
        {'id': 1, 'e_m': 1.004911, 'e_o_k': [0.205924, 0.164740, 0.131792], 'p_i': 20, 'u_i': 1.7213},
        {'id': 2, 'e_m': 2.250211, 'e_o_k': [0.461109, 0.368887, 0.295110], 'p_i': 40, 'u_i': 2.3007},
        {'id': 3, 'e_m': 2.587062, 'e_o_k': [0.530136, 0.424108, 0.339287], 'p_i': 80, 'u_i': 2.4667},
        {'id': 4, 'e_m': 2.270607, 'e_o_k': [0.465288, 0.372231, 0.297785], 'p_i': 80, 'u_i': 2.4016},
        {'id': 5, 'e_m': 0.342865, 'e_o_k': [0.070259, 0.056207, 0.044966], 'p_i': 10, 'u_i': 3.4602},
        {'id': 6, 'e_m': 7.548057, 'e_o_k': [1.546733, 1.237386, 0.989909], 'p_i': 80, 'u_i': 3.9709},
        {'id': 7, 'e_m': 4.038448, 'e_o_k': [0.827551, 0.662041, 0.529632], 'p_i': 80, 'u_i': 1.7339},
    ]
    B_BUDGET = 55.199994
    return processors, tasks, B_BUDGET
