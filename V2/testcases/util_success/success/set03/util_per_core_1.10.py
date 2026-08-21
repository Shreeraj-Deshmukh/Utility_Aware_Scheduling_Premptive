"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119992, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119992, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.316256, 'e_o_k': [0.133766, 0.107013, 0.085610, 0.068488], 'p_i': 10, 'u_i': 4.7590},
        {'id': 1, 'e_m': 7.102456, 'e_o_k': [0.577548, 0.462039, 0.369631, 0.295705, 0.236564, 0.189251], 'p_i': 20, 'u_i': 3.5697},
        {'id': 2, 'e_m': 0.723601, 'e_o_k': [0.120600, 0.096480], 'p_i': 40, 'u_i': 4.9097},
        {'id': 3, 'e_m': 39.163429, 'e_o_k': [3.980023, 3.184019, 2.547215, 2.037772], 'p_i': 80, 'u_i': 2.3699},
        {'id': 4, 'e_m': 32.721839, 'e_o_k': [2.920202, 2.336162, 1.868929, 1.495144, 1.196115], 'p_i': 80, 'u_i': 2.8455},
        {'id': 5, 'e_m': 2.580354, 'e_o_k': [0.430059, 0.344047], 'p_i': 40, 'u_i': 4.6019},
        {'id': 6, 'e_m': 3.872568, 'e_o_k': [0.345600, 0.276480, 0.221184, 0.176947, 0.141558], 'p_i': 10, 'u_i': 3.8575},
        {'id': 7, 'e_m': 27.586405, 'e_o_k': [2.243235, 1.794588, 1.435670, 1.148536, 0.918829, 0.735063], 'p_i': 80, 'u_i': 4.2775},
    ]
    B_BUDGET = 263.119992
    return processors, tasks, B_BUDGET
