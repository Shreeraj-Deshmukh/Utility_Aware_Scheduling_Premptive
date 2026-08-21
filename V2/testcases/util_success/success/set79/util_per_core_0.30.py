"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.76, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.76, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.510123, 'e_o_k': [0.045525, 0.036420, 0.029136, 0.023309, 0.018647], 'p_i': 10, 'u_i': 4.9110},
        {'id': 1, 'e_m': 1.267390, 'e_o_k': [0.103060, 0.082448, 0.065958, 0.052767, 0.042213, 0.033771], 'p_i': 20, 'u_i': 1.5555},
        {'id': 2, 'e_m': 0.389711, 'e_o_k': [0.047915, 0.038332, 0.030666], 'p_i': 40, 'u_i': 1.9189},
        {'id': 3, 'e_m': 13.570846, 'e_o_k': [2.261808, 1.809446], 'p_i': 80, 'u_i': 3.1608},
        {'id': 4, 'e_m': 3.757345, 'e_o_k': [0.626224, 0.500979], 'p_i': 80, 'u_i': 1.3239},
        {'id': 5, 'e_m': 1.466948, 'e_o_k': [0.149080, 0.119264, 0.095411, 0.076329], 'p_i': 80, 'u_i': 4.3282},
        {'id': 6, 'e_m': 8.062884, 'e_o_k': [1.343814, 1.075051], 'p_i': 40, 'u_i': 3.0285},
        {'id': 7, 'e_m': 3.149128, 'e_o_k': [0.320033, 0.256027, 0.204821, 0.163857], 'p_i': 80, 'u_i': 4.7214},
    ]
    B_BUDGET = 71.760000
    return processors, tasks, B_BUDGET
