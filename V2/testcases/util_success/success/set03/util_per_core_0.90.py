"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279986, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279986, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.237077, 'e_o_k': [0.029149, 0.023319, 0.018655], 'p_i': 10, 'u_i': 1.1011},
        {'id': 1, 'e_m': 0.907657, 'e_o_k': [0.081002, 0.064802, 0.051841, 0.041473, 0.033179], 'p_i': 20, 'u_i': 1.8110},
        {'id': 2, 'e_m': 16.562432, 'e_o_k': [1.683174, 1.346539, 1.077231, 0.861785], 'p_i': 40, 'u_i': 2.7882},
        {'id': 3, 'e_m': 20.179546, 'e_o_k': [2.050767, 1.640613, 1.312491, 1.049993], 'p_i': 80, 'u_i': 1.5962},
        {'id': 4, 'e_m': 8.898888, 'e_o_k': [0.723628, 0.578902, 0.463122, 0.370498, 0.296398, 0.237118], 'p_i': 20, 'u_i': 4.3893},
        {'id': 5, 'e_m': 1.557249, 'e_o_k': [0.138974, 0.111179, 0.088943, 0.071155, 0.056924], 'p_i': 20, 'u_i': 1.3904},
        {'id': 6, 'e_m': 5.914146, 'e_o_k': [0.985691, 0.788553], 'p_i': 20, 'u_i': 3.7533},
        {'id': 7, 'e_m': 9.843603, 'e_o_k': [1.210279, 0.968223, 0.774579], 'p_i': 40, 'u_i': 3.0100},
    ]
    B_BUDGET = 215.279986
    return processors, tasks, B_BUDGET
