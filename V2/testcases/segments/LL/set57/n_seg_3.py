"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199987, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199987, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.100744, 'e_o_k': [0.020644, 0.016515, 0.013212], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 0.720915, 'e_o_k': [0.147728, 0.118183, 0.094546], 'p_i': 20, 'u_i': 1.1969},
        {'id': 2, 'e_m': 4.330945, 'e_o_k': [0.887489, 0.709991, 0.567993], 'p_i': 40, 'u_i': 4.6056},
        {'id': 3, 'e_m': 4.451086, 'e_o_k': [0.912108, 0.729686, 0.583749], 'p_i': 80, 'u_i': 2.0280},
        {'id': 4, 'e_m': 2.996813, 'e_o_k': [0.614101, 0.491281, 0.393025], 'p_i': 40, 'u_i': 3.8591},
        {'id': 5, 'e_m': 2.171206, 'e_o_k': [0.444919, 0.355935, 0.284748], 'p_i': 80, 'u_i': 4.1547},
        {'id': 6, 'e_m': 0.650677, 'e_o_k': [0.133335, 0.106668, 0.085335], 'p_i': 10, 'u_i': 4.9057},
        {'id': 7, 'e_m': 1.827166, 'e_o_k': [0.374419, 0.299535, 0.239628], 'p_i': 80, 'u_i': 4.2009},
    ]
    B_BUDGET = 55.199987
    return processors, tasks, B_BUDGET
