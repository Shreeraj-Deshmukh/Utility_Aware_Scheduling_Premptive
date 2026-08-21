"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280001, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280001, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.723846, 'e_o_k': [0.457850, 0.366280, 0.293024], 'p_i': 10, 'u_i': 1.4273},
        {'id': 1, 'e_m': 3.749654, 'e_o_k': [0.304909, 0.243928, 0.195142, 0.156114, 0.124891, 0.099913], 'p_i': 20, 'u_i': 1.3040},
        {'id': 2, 'e_m': 4.871497, 'e_o_k': [0.434748, 0.347798, 0.278239, 0.222591, 0.178073], 'p_i': 40, 'u_i': 4.6760},
        {'id': 3, 'e_m': 15.993121, 'e_o_k': [2.665520, 2.132416], 'p_i': 80, 'u_i': 3.1592},
        {'id': 4, 'e_m': 5.396305, 'e_o_k': [0.899384, 0.719507], 'p_i': 40, 'u_i': 4.3140},
        {'id': 5, 'e_m': 9.687604, 'e_o_k': [0.787764, 0.630211, 0.504169, 0.403335, 0.322668, 0.258134], 'p_i': 20, 'u_i': 4.5760},
        {'id': 6, 'e_m': 0.215671, 'e_o_k': [0.026517, 0.021214, 0.016971], 'p_i': 20, 'u_i': 2.9798},
        {'id': 7, 'e_m': 23.068788, 'e_o_k': [3.844798, 3.075838], 'p_i': 80, 'u_i': 3.8735},
    ]
    B_BUDGET = 215.280001
    return processors, tasks, B_BUDGET
