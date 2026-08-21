"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359993, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359993, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.742787, 'e_o_k': [0.155532, 0.124426, 0.099540, 0.079632, 0.063706], 'p_i': 10, 'u_i': 1.4156},
        {'id': 1, 'e_m': 4.805394, 'e_o_k': [0.800899, 0.640719], 'p_i': 20, 'u_i': 4.7114},
        {'id': 2, 'e_m': 12.705697, 'e_o_k': [1.133897, 0.907118, 0.725694, 0.580555, 0.464444], 'p_i': 40, 'u_i': 3.0006},
        {'id': 3, 'e_m': 18.193035, 'e_o_k': [2.236849, 1.789479, 1.431583], 'p_i': 80, 'u_i': 1.2816},
        {'id': 4, 'e_m': 2.338536, 'e_o_k': [0.237656, 0.190125, 0.152100, 0.121680], 'p_i': 40, 'u_i': 2.2759},
        {'id': 5, 'e_m': 6.959745, 'e_o_k': [0.565943, 0.452755, 0.362204, 0.289763, 0.231810, 0.185448], 'p_i': 20, 'u_i': 1.7983},
        {'id': 6, 'e_m': 0.106085, 'e_o_k': [0.017681, 0.014145], 'p_i': 10, 'u_i': 2.1310},
        {'id': 7, 'e_m': 4.466741, 'e_o_k': [0.363221, 0.290576, 0.232461, 0.185969, 0.148775, 0.119020], 'p_i': 20, 'u_i': 2.4443},
    ]
    B_BUDGET = 191.359993
    return processors, tasks, B_BUDGET
