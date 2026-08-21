"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359984, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359984, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.518161, 'e_o_k': [0.204768, 0.163815, 0.131052, 0.104841, 0.083873, 0.067099], 'p_i': 10, 'u_i': 4.1820},
        {'id': 1, 'e_m': 7.821304, 'e_o_k': [1.303551, 1.042841], 'p_i': 20, 'u_i': 2.8729},
        {'id': 2, 'e_m': 1.110669, 'e_o_k': [0.136558, 0.109246, 0.087397], 'p_i': 40, 'u_i': 4.4646},
        {'id': 3, 'e_m': 10.234723, 'e_o_k': [1.705787, 1.364630], 'p_i': 80, 'u_i': 2.8456},
        {'id': 4, 'e_m': 1.661945, 'e_o_k': [0.168897, 0.135117, 0.108094, 0.086475], 'p_i': 10, 'u_i': 4.6357},
        {'id': 5, 'e_m': 27.994968, 'e_o_k': [4.665828, 3.732662], 'p_i': 80, 'u_i': 3.1275},
        {'id': 6, 'e_m': 2.654171, 'e_o_k': [0.269733, 0.215786, 0.172629, 0.138103], 'p_i': 10, 'u_i': 2.7677},
        {'id': 7, 'e_m': 0.198692, 'e_o_k': [0.020192, 0.016154, 0.012923, 0.010338], 'p_i': 10, 'u_i': 2.2237},
    ]
    B_BUDGET = 191.359984
    return processors, tasks, B_BUDGET
