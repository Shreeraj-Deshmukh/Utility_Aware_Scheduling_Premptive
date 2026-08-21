"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.20001, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.20001, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.067141, 'e_o_k': [0.015428, 0.009257, 0.005554, 0.003332], 'p_i': 10, 'u_i': 3.0491},
        {'id': 1, 'e_m': 0.797553, 'e_o_k': [0.172960, 0.103776, 0.062266, 0.037359, 0.022416], 'p_i': 20, 'u_i': 3.9469},
        {'id': 2, 'e_m': 2.043499, 'e_o_k': [0.521301, 0.312780, 0.187668], 'p_i': 40, 'u_i': 1.2331},
        {'id': 3, 'e_m': 5.056120, 'e_o_k': [1.289827, 0.773896, 0.464338], 'p_i': 80, 'u_i': 3.8857},
        {'id': 4, 'e_m': 0.957980, 'e_o_k': [0.299369, 0.179621], 'p_i': 20, 'u_i': 4.4773},
        {'id': 5, 'e_m': 0.502682, 'e_o_k': [0.157088, 0.094253], 'p_i': 10, 'u_i': 2.4546},
        {'id': 6, 'e_m': 0.546749, 'e_o_k': [0.125632, 0.075379, 0.045227, 0.027136], 'p_i': 80, 'u_i': 1.1544},
        {'id': 7, 'e_m': 10.729419, 'e_o_k': [2.737097, 1.642258, 0.985355], 'p_i': 80, 'u_i': 4.0204},
    ]
    B_BUDGET = 55.200010
    return processors, tasks, B_BUDGET
