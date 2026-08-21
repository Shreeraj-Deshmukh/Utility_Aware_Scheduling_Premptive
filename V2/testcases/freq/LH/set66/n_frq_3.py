"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 29, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "freq", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 29, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "freq", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.7, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.7, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.067141, 'e_o_k': [0.031842, 0.025474, 0.020379, 0.016303], 'p_i': 10, 'u_i': 3.0491},
        {'id': 1, 'e_m': 0.797553, 'e_o_k': [0.332155, 0.265724, 0.212579, 0.170064, 0.136051], 'p_i': 20, 'u_i': 3.9469},
        {'id': 2, 'e_m': 2.043499, 'e_o_k': [1.172499, 0.937999, 0.750400], 'p_i': 40, 'u_i': 1.2331},
        {'id': 3, 'e_m': 5.056120, 'e_o_k': [2.901053, 2.320842, 1.856674], 'p_i': 80, 'u_i': 3.8857},
        {'id': 4, 'e_m': 0.957980, 'e_o_k': [0.745095, 0.596076], 'p_i': 20, 'u_i': 4.4773},
        {'id': 5, 'e_m': 0.502682, 'e_o_k': [0.390975, 0.312780], 'p_i': 10, 'u_i': 2.4546},
        {'id': 6, 'e_m': 0.546749, 'e_o_k': [0.259298, 0.207439, 0.165951, 0.132761], 'p_i': 80, 'u_i': 1.1544},
        {'id': 7, 'e_m': 10.729419, 'e_o_k': [6.156224, 4.924979, 3.939983], 'p_i': 80, 'u_i': 4.0204},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET
