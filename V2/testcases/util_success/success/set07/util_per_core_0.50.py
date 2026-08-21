"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600014, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600014, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.034378, 'e_o_k': [0.005730, 0.004584], 'p_i': 10, 'u_i': 3.6748},
        {'id': 1, 'e_m': 1.458207, 'e_o_k': [0.243034, 0.194428], 'p_i': 20, 'u_i': 4.5666},
        {'id': 2, 'e_m': 4.068514, 'e_o_k': [0.363087, 0.290470, 0.232376, 0.185901, 0.148721], 'p_i': 40, 'u_i': 2.1776},
        {'id': 3, 'e_m': 12.008754, 'e_o_k': [1.476486, 1.181189, 0.944951], 'p_i': 80, 'u_i': 3.5354},
        {'id': 4, 'e_m': 18.444500, 'e_o_k': [1.874441, 1.499553, 1.199642, 0.959714], 'p_i': 80, 'u_i': 3.2835},
        {'id': 5, 'e_m': 0.443652, 'e_o_k': [0.073942, 0.059154], 'p_i': 20, 'u_i': 1.9722},
        {'id': 6, 'e_m': 8.107854, 'e_o_k': [1.351309, 1.081047], 'p_i': 20, 'u_i': 1.1966},
        {'id': 7, 'e_m': 0.136980, 'e_o_k': [0.012225, 0.009780, 0.007824, 0.006259, 0.005007], 'p_i': 10, 'u_i': 1.4854},
    ]
    B_BUDGET = 119.600014
    return processors, tasks, B_BUDGET
