"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680014, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680014, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.127808, 'e_o_k': [0.012989, 0.010391, 0.008313, 0.006650], 'p_i': 10, 'u_i': 3.7146},
        {'id': 1, 'e_m': 4.638287, 'e_o_k': [0.570281, 0.456225, 0.364980], 'p_i': 20, 'u_i': 2.7971},
        {'id': 2, 'e_m': 0.800790, 'e_o_k': [0.098458, 0.078766, 0.063013], 'p_i': 40, 'u_i': 1.6396},
        {'id': 3, 'e_m': 9.437860, 'e_o_k': [1.160393, 0.928314, 0.742651], 'p_i': 80, 'u_i': 4.1445},
        {'id': 4, 'e_m': 3.483129, 'e_o_k': [0.353977, 0.283181, 0.226545, 0.181236], 'p_i': 20, 'u_i': 4.6205},
        {'id': 5, 'e_m': 14.523637, 'e_o_k': [1.181014, 0.944811, 0.755849, 0.604679, 0.483743, 0.386995], 'p_i': 80, 'u_i': 1.3665},
        {'id': 6, 'e_m': 0.073356, 'e_o_k': [0.007455, 0.005964, 0.004771, 0.003817], 'p_i': 20, 'u_i': 3.3652},
        {'id': 7, 'e_m': 1.158844, 'e_o_k': [0.103419, 0.082735, 0.066188, 0.052951, 0.042360], 'p_i': 20, 'u_i': 2.1692},
    ]
    B_BUDGET = 95.680014
    return processors, tasks, B_BUDGET
