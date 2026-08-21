"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199997, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199997, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.547418, 'e_o_k': [0.152060, 0.121648], 'p_i': 10, 'u_i': 4.0093},
        {'id': 1, 'e_m': 3.007680, 'e_o_k': [0.835467, 0.668373], 'p_i': 20, 'u_i': 1.1110},
        {'id': 2, 'e_m': 0.682430, 'e_o_k': [0.189564, 0.151651], 'p_i': 40, 'u_i': 1.4549},
        {'id': 3, 'e_m': 0.604649, 'e_o_k': [0.167958, 0.134366], 'p_i': 80, 'u_i': 2.4103},
        {'id': 4, 'e_m': 1.249104, 'e_o_k': [0.346973, 0.277579], 'p_i': 20, 'u_i': 1.7953},
        {'id': 5, 'e_m': 0.444853, 'e_o_k': [0.123570, 0.098856], 'p_i': 20, 'u_i': 3.8298},
        {'id': 6, 'e_m': 0.188448, 'e_o_k': [0.052347, 0.041877], 'p_i': 10, 'u_i': 2.6902},
        {'id': 7, 'e_m': 2.668510, 'e_o_k': [0.741253, 0.593002], 'p_i': 40, 'u_i': 2.7407},
    ]
    B_BUDGET = 55.199997
    return processors, tasks, B_BUDGET
