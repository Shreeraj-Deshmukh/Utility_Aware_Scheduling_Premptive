"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.20001, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.20001, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.547418, 'e_o_k': [0.125785, 0.075471, 0.045283, 0.027170], 'p_i': 10, 'u_i': 4.0093},
        {'id': 1, 'e_m': 3.007680, 'e_o_k': [0.767265, 0.460359, 0.276216], 'p_i': 20, 'u_i': 1.1110},
        {'id': 2, 'e_m': 0.682430, 'e_o_k': [0.143165, 0.085899, 0.051540, 0.030924, 0.018554, 0.011133], 'p_i': 40, 'u_i': 1.1701},
        {'id': 3, 'e_m': 0.604649, 'e_o_k': [0.154247, 0.092548, 0.055529], 'p_i': 80, 'u_i': 4.4848},
        {'id': 4, 'e_m': 1.249104, 'e_o_k': [0.287018, 0.172211, 0.103327, 0.061996], 'p_i': 20, 'u_i': 3.6888},
        {'id': 5, 'e_m': 0.444853, 'e_o_k': [0.113483, 0.068090, 0.040854], 'p_i': 20, 'u_i': 2.1778},
        {'id': 6, 'e_m': 0.188448, 'e_o_k': [0.058890, 0.035334], 'p_i': 10, 'u_i': 3.8298},
        {'id': 7, 'e_m': 2.668510, 'e_o_k': [0.833909, 0.500346], 'p_i': 40, 'u_i': 2.6902},
    ]
    B_BUDGET = 55.200010
    return processors, tasks, B_BUDGET
