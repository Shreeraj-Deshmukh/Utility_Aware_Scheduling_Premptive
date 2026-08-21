"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320017, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.320017, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.547418, 'e_o_k': [0.352199, 0.211319, 0.126792, 0.076075], 'p_i': 10, 'u_i': 4.0093},
        {'id': 1, 'e_m': 3.007680, 'e_o_k': [2.148343, 1.289006, 0.773404], 'p_i': 20, 'u_i': 1.1110},
        {'id': 2, 'e_m': 0.682430, 'e_o_k': [0.400863, 0.240518, 0.144311, 0.086586, 0.051952, 0.031171], 'p_i': 40, 'u_i': 1.1701},
        {'id': 3, 'e_m': 0.604649, 'e_o_k': [0.431892, 0.259135, 0.155481], 'p_i': 80, 'u_i': 4.4848},
        {'id': 4, 'e_m': 1.249104, 'e_o_k': [0.803652, 0.482191, 0.289315, 0.173589], 'p_i': 20, 'u_i': 3.6888},
        {'id': 5, 'e_m': 0.444853, 'e_o_k': [0.317752, 0.190651, 0.114391], 'p_i': 20, 'u_i': 2.1778},
        {'id': 6, 'e_m': 0.188448, 'e_o_k': [0.164892, 0.098935], 'p_i': 10, 'u_i': 3.8298},
        {'id': 7, 'e_m': 2.668510, 'e_o_k': [2.334946, 1.400968], 'p_i': 40, 'u_i': 2.6902},
    ]
    B_BUDGET = 88.320017
    return processors, tasks, B_BUDGET
