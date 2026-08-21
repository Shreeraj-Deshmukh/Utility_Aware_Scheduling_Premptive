"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.219693, 'e_o_k': [0.126053, 0.100843, 0.080674], 'p_i': 10, 'u_i': 3.0447},
        {'id': 1, 'e_m': 1.690611, 'e_o_k': [0.970022, 0.776018, 0.620814], 'p_i': 20, 'u_i': 2.1118},
        {'id': 2, 'e_m': 2.250553, 'e_o_k': [1.291301, 1.033041, 0.826433], 'p_i': 40, 'u_i': 4.2305},
        {'id': 3, 'e_m': 0.648336, 'e_o_k': [0.371996, 0.297597, 0.238078], 'p_i': 80, 'u_i': 2.0791},
        {'id': 4, 'e_m': 7.268970, 'e_o_k': [4.170721, 3.336576, 2.669261], 'p_i': 80, 'u_i': 1.4810},
        {'id': 5, 'e_m': 3.974108, 'e_o_k': [2.280226, 1.824181, 1.459345], 'p_i': 80, 'u_i': 3.5439},
        {'id': 6, 'e_m': 3.618059, 'e_o_k': [2.075936, 1.660748, 1.328599], 'p_i': 80, 'u_i': 1.8113},
        {'id': 7, 'e_m': 0.433679, 'e_o_k': [0.248832, 0.199066, 0.159253], 'p_i': 10, 'u_i': 4.9983},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET
