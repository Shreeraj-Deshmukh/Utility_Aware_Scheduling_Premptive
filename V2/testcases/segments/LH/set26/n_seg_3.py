"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319979, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319979, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.630729, 'e_o_k': [0.935664, 0.748531, 0.598825], 'p_i': 10, 'u_i': 2.1780},
        {'id': 1, 'e_m': 0.554446, 'e_o_k': [0.318125, 0.254500, 0.203600], 'p_i': 20, 'u_i': 3.8388},
        {'id': 2, 'e_m': 1.443928, 'e_o_k': [0.828483, 0.662787, 0.530229], 'p_i': 40, 'u_i': 1.0041},
        {'id': 3, 'e_m': 3.915968, 'e_o_k': [2.246867, 1.797493, 1.437995], 'p_i': 80, 'u_i': 4.1994},
        {'id': 4, 'e_m': 0.833670, 'e_o_k': [0.478335, 0.382668, 0.306135], 'p_i': 40, 'u_i': 2.3676},
        {'id': 5, 'e_m': 0.367491, 'e_o_k': [0.210855, 0.168684, 0.134947], 'p_i': 10, 'u_i': 3.7622},
        {'id': 6, 'e_m': 0.185253, 'e_o_k': [0.106293, 0.085034, 0.068027], 'p_i': 10, 'u_i': 1.6504},
        {'id': 7, 'e_m': 3.843267, 'e_o_k': [2.205153, 1.764123, 1.411298], 'p_i': 80, 'u_i': 2.4020},
    ]
    B_BUDGET = 88.319979
    return processors, tasks, B_BUDGET
