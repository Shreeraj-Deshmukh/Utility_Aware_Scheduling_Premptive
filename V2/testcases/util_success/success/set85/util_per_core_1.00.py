"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200015, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200015, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.854139, 'e_o_k': [0.809023, 0.647219], 'p_i': 10, 'u_i': 4.6328},
        {'id': 1, 'e_m': 3.530167, 'e_o_k': [0.434037, 0.347230, 0.277784], 'p_i': 20, 'u_i': 2.2077},
        {'id': 2, 'e_m': 2.330442, 'e_o_k': [0.236834, 0.189467, 0.151573, 0.121259], 'p_i': 40, 'u_i': 2.3378},
        {'id': 3, 'e_m': 7.993377, 'e_o_k': [0.713355, 0.570684, 0.456547, 0.365238, 0.292190], 'p_i': 80, 'u_i': 4.9231},
        {'id': 4, 'e_m': 0.708704, 'e_o_k': [0.087136, 0.069709, 0.055767], 'p_i': 10, 'u_i': 2.4450},
        {'id': 5, 'e_m': 4.590136, 'e_o_k': [0.564361, 0.451489, 0.361191], 'p_i': 10, 'u_i': 2.0976},
        {'id': 6, 'e_m': 29.778225, 'e_o_k': [2.421466, 1.937173, 1.549738, 1.239791, 0.991833, 0.793466], 'p_i': 80, 'u_i': 4.8141},
        {'id': 7, 'e_m': 5.555753, 'e_o_k': [0.925959, 0.740767], 'p_i': 20, 'u_i': 4.1139},
    ]
    B_BUDGET = 239.200015
    return processors, tasks, B_BUDGET
