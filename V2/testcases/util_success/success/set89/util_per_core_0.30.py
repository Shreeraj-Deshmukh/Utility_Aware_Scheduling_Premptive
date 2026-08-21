"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760029, "H": 80, "J": 47, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760029, "H": 80, "J": 47, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.918347, 'e_o_k': [0.074677, 0.059742, 0.047793, 0.038235, 0.030588, 0.024470], 'p_i': 10, 'u_i': 1.1682},
        {'id': 1, 'e_m': 1.228081, 'e_o_k': [0.099863, 0.079891, 0.063913, 0.051130, 0.040904, 0.032723], 'p_i': 20, 'u_i': 1.7372},
        {'id': 2, 'e_m': 1.695830, 'e_o_k': [0.137899, 0.110319, 0.088256, 0.070604, 0.056484, 0.045187], 'p_i': 40, 'u_i': 1.2016},
        {'id': 3, 'e_m': 0.020596, 'e_o_k': [0.003433, 0.002746], 'p_i': 80, 'u_i': 4.7805},
        {'id': 4, 'e_m': 1.215071, 'e_o_k': [0.149394, 0.119515, 0.095612], 'p_i': 10, 'u_i': 3.7064},
        {'id': 5, 'e_m': 2.180153, 'e_o_k': [0.363359, 0.290687], 'p_i': 10, 'u_i': 4.7396},
        {'id': 6, 'e_m': 0.046028, 'e_o_k': [0.007671, 0.006137], 'p_i': 10, 'u_i': 4.0832},
        {'id': 7, 'e_m': 0.599830, 'e_o_k': [0.053531, 0.042825, 0.034260, 0.027408, 0.021926], 'p_i': 10, 'u_i': 1.4400},
    ]
    B_BUDGET = 71.760029
    return processors, tasks, B_BUDGET
