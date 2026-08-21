"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200023, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.200023, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.067141, 'e_o_k': [0.008393, 0.008393, 0.008393, 0.008393], 'p_i': 10, 'u_i': 3.0491},
        {'id': 1, 'e_m': 0.797553, 'e_o_k': [0.079755, 0.079755, 0.079755, 0.079755, 0.079755], 'p_i': 20, 'u_i': 3.9469},
        {'id': 2, 'e_m': 2.043499, 'e_o_k': [0.340583, 0.340583, 0.340583], 'p_i': 40, 'u_i': 1.2331},
        {'id': 3, 'e_m': 5.056120, 'e_o_k': [0.842687, 0.842687, 0.842687], 'p_i': 80, 'u_i': 3.8857},
        {'id': 4, 'e_m': 0.957980, 'e_o_k': [0.239495, 0.239495], 'p_i': 20, 'u_i': 4.4773},
        {'id': 5, 'e_m': 0.502682, 'e_o_k': [0.125671, 0.125671], 'p_i': 10, 'u_i': 2.4546},
        {'id': 6, 'e_m': 0.546749, 'e_o_k': [0.068344, 0.068344, 0.068344, 0.068344], 'p_i': 80, 'u_i': 1.1544},
        {'id': 7, 'e_m': 10.729419, 'e_o_k': [1.788237, 1.788237, 1.788237], 'p_i': 80, 'u_i': 4.0204},
    ]
    B_BUDGET = 55.200023
    return processors, tasks, B_BUDGET
