"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199992, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199992, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.075032, 'e_o_k': [0.298620, 0.238896], 'p_i': 10, 'u_i': 4.6321},
        {'id': 1, 'e_m': 0.138443, 'e_o_k': [0.038456, 0.030765], 'p_i': 20, 'u_i': 3.6983},
        {'id': 2, 'e_m': 0.518452, 'e_o_k': [0.144014, 0.115211], 'p_i': 40, 'u_i': 3.0670},
        {'id': 3, 'e_m': 0.130830, 'e_o_k': [0.036342, 0.029073], 'p_i': 80, 'u_i': 2.2547},
        {'id': 4, 'e_m': 6.327178, 'e_o_k': [1.757549, 1.406040], 'p_i': 80, 'u_i': 3.3628},
        {'id': 5, 'e_m': 0.084400, 'e_o_k': [0.023444, 0.018755], 'p_i': 10, 'u_i': 1.9431},
        {'id': 6, 'e_m': 1.306253, 'e_o_k': [0.362848, 0.290278], 'p_i': 80, 'u_i': 4.2381},
        {'id': 7, 'e_m': 1.671201, 'e_o_k': [0.464223, 0.371378], 'p_i': 10, 'u_i': 1.5683},
    ]
    B_BUDGET = 55.199992
    return processors, tasks, B_BUDGET
