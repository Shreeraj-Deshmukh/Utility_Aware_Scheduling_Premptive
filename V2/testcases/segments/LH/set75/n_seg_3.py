"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320014, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320014, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.446887, 'e_o_k': [0.256410, 0.205128, 0.164103], 'p_i': 10, 'u_i': 4.1325},
        {'id': 1, 'e_m': 0.001026, 'e_o_k': [0.000588, 0.000471, 0.000377], 'p_i': 20, 'u_i': 2.4718},
        {'id': 2, 'e_m': 6.562599, 'e_o_k': [3.765426, 3.012341, 2.409873], 'p_i': 40, 'u_i': 2.6491},
        {'id': 3, 'e_m': 2.341741, 'e_o_k': [1.343622, 1.074897, 0.859918], 'p_i': 80, 'u_i': 3.7785},
        {'id': 4, 'e_m': 0.177678, 'e_o_k': [0.101946, 0.081557, 0.065246], 'p_i': 10, 'u_i': 2.0110},
        {'id': 5, 'e_m': 0.341853, 'e_o_k': [0.196145, 0.156916, 0.125533], 'p_i': 10, 'u_i': 2.7392},
        {'id': 6, 'e_m': 6.037977, 'e_o_k': [3.464413, 2.771530, 2.217224], 'p_i': 80, 'u_i': 4.5700},
        {'id': 7, 'e_m': 0.689911, 'e_o_k': [0.395851, 0.316681, 0.253344], 'p_i': 20, 'u_i': 2.3393},
    ]
    B_BUDGET = 88.320014
    return processors, tasks, B_BUDGET
