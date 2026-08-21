"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.547418, 'e_o_k': [0.425769, 0.340615], 'p_i': 10, 'u_i': 4.0093},
        {'id': 1, 'e_m': 3.007680, 'e_o_k': [2.339307, 1.871446], 'p_i': 20, 'u_i': 1.1110},
        {'id': 2, 'e_m': 0.682430, 'e_o_k': [0.530779, 0.424623], 'p_i': 40, 'u_i': 1.4549},
        {'id': 3, 'e_m': 0.604649, 'e_o_k': [0.470282, 0.376226], 'p_i': 80, 'u_i': 2.4103},
        {'id': 4, 'e_m': 1.249104, 'e_o_k': [0.971526, 0.777220], 'p_i': 20, 'u_i': 1.7953},
        {'id': 5, 'e_m': 0.444853, 'e_o_k': [0.345997, 0.276797], 'p_i': 20, 'u_i': 3.8298},
        {'id': 6, 'e_m': 0.188448, 'e_o_k': [0.146570, 0.117256], 'p_i': 10, 'u_i': 2.6902},
        {'id': 7, 'e_m': 2.668510, 'e_o_k': [2.075507, 1.660406], 'p_i': 40, 'u_i': 2.7407},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET
