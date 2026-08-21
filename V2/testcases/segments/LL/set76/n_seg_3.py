"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199997, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199997, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.547418, 'e_o_k': [0.112176, 0.089741, 0.071792], 'p_i': 10, 'u_i': 4.0093},
        {'id': 1, 'e_m': 3.007680, 'e_o_k': [0.616328, 0.493062, 0.394450], 'p_i': 20, 'u_i': 1.1110},
        {'id': 2, 'e_m': 0.682430, 'e_o_k': [0.139842, 0.111874, 0.089499], 'p_i': 40, 'u_i': 1.4549},
        {'id': 3, 'e_m': 0.604649, 'e_o_k': [0.123903, 0.099123, 0.079298], 'p_i': 80, 'u_i': 2.4103},
        {'id': 4, 'e_m': 1.249104, 'e_o_k': [0.255964, 0.204771, 0.163817], 'p_i': 20, 'u_i': 1.7953},
        {'id': 5, 'e_m': 0.444853, 'e_o_k': [0.091158, 0.072927, 0.058341], 'p_i': 20, 'u_i': 3.8298},
        {'id': 6, 'e_m': 0.188448, 'e_o_k': [0.038616, 0.030893, 0.024714], 'p_i': 10, 'u_i': 2.6902},
        {'id': 7, 'e_m': 2.668510, 'e_o_k': [0.546826, 0.437461, 0.349968], 'p_i': 40, 'u_i': 2.7407},
    ]
    B_BUDGET = 55.199997
    return processors, tasks, B_BUDGET
