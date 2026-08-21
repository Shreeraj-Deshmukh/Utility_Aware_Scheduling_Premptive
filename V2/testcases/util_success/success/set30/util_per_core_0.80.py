"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.36, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.36, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.816330, 'e_o_k': [0.162095, 0.129676, 0.103741, 0.082993, 0.066394], 'p_i': 10, 'u_i': 1.6258},
        {'id': 1, 'e_m': 2.106413, 'e_o_k': [0.351069, 0.280855], 'p_i': 20, 'u_i': 4.0171},
        {'id': 2, 'e_m': 8.847097, 'e_o_k': [1.087758, 0.870206, 0.696165], 'p_i': 40, 'u_i': 4.0480},
        {'id': 3, 'e_m': 6.023335, 'e_o_k': [0.740574, 0.592459, 0.473967], 'p_i': 80, 'u_i': 4.2597},
        {'id': 4, 'e_m': 15.128982, 'e_o_k': [1.537498, 1.229999, 0.983999, 0.787199], 'p_i': 40, 'u_i': 1.3375},
        {'id': 5, 'e_m': 6.170583, 'e_o_k': [0.501771, 0.401417, 0.321134, 0.256907, 0.205526, 0.164420], 'p_i': 80, 'u_i': 2.9676},
        {'id': 6, 'e_m': 38.379096, 'e_o_k': [6.396516, 5.117213], 'p_i': 80, 'u_i': 4.7574},
        {'id': 7, 'e_m': 3.259268, 'e_o_k': [0.543211, 0.434569], 'p_i': 40, 'u_i': 2.6642},
    ]
    B_BUDGET = 191.360000
    return processors, tasks, B_BUDGET
