"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279987, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279987, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.988619, 'e_o_k': [0.080391, 0.064313, 0.051450, 0.041160, 0.032928, 0.026343], 'p_i': 10, 'u_i': 3.3901},
        {'id': 1, 'e_m': 7.607748, 'e_o_k': [0.618637, 0.494909, 0.395928, 0.316742, 0.253394, 0.202715], 'p_i': 20, 'u_i': 2.3217},
        {'id': 2, 'e_m': 10.127491, 'e_o_k': [1.029217, 0.823373, 0.658699, 0.526959], 'p_i': 40, 'u_i': 2.1118},
        {'id': 3, 'e_m': 2.917513, 'e_o_k': [0.296495, 0.237196, 0.189757, 0.151806], 'p_i': 80, 'u_i': 4.2305},
        {'id': 4, 'e_m': 32.710365, 'e_o_k': [5.451728, 4.361382], 'p_i': 80, 'u_i': 2.0791},
        {'id': 5, 'e_m': 17.883486, 'e_o_k': [2.980581, 2.384465], 'p_i': 80, 'u_i': 1.4810},
        {'id': 6, 'e_m': 16.281266, 'e_o_k': [2.713544, 2.170835], 'p_i': 80, 'u_i': 3.5439},
        {'id': 7, 'e_m': 1.951555, 'e_o_k': [0.158694, 0.126955, 0.101564, 0.081251, 0.065001, 0.052001], 'p_i': 10, 'u_i': 4.1958},
    ]
    B_BUDGET = 215.279987
    return processors, tasks, B_BUDGET
