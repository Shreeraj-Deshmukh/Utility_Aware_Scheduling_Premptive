"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440013, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440013, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.245303, 'e_o_k': [0.207551, 0.166040], 'p_i': 10, 'u_i': 2.6844},
        {'id': 1, 'e_m': 3.423067, 'e_o_k': [0.278352, 0.222682, 0.178146, 0.142516, 0.114013, 0.091211], 'p_i': 20, 'u_i': 3.2251},
        {'id': 2, 'e_m': 11.513089, 'e_o_k': [1.415544, 1.132435, 0.905948], 'p_i': 40, 'u_i': 4.0273},
        {'id': 3, 'e_m': 26.072046, 'e_o_k': [3.205579, 2.564464, 2.051571], 'p_i': 80, 'u_i': 2.2476},
        {'id': 4, 'e_m': 8.433429, 'e_o_k': [0.857056, 0.685645, 0.548516, 0.438813], 'p_i': 80, 'u_i': 1.3199},
        {'id': 5, 'e_m': 0.804014, 'e_o_k': [0.065380, 0.052304, 0.041843, 0.033474, 0.026780, 0.021424], 'p_i': 10, 'u_i': 4.7520},
        {'id': 6, 'e_m': 2.309409, 'e_o_k': [0.206099, 0.164879, 0.131903, 0.105523, 0.084418], 'p_i': 20, 'u_i': 3.4892},
        {'id': 7, 'e_m': 3.785978, 'e_o_k': [0.630996, 0.504797], 'p_i': 20, 'u_i': 1.4050},
    ]
    B_BUDGET = 167.440013
    return processors, tasks, B_BUDGET
