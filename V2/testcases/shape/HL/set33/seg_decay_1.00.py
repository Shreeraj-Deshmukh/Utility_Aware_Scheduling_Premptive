"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400006, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.400006, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.048193, 'e_o_k': [0.008032, 0.008032, 0.008032], 'p_i': 10, 'u_i': 4.1859},
        {'id': 1, 'e_m': 3.648051, 'e_o_k': [0.608009, 0.608009, 0.608009], 'p_i': 20, 'u_i': 1.3758},
        {'id': 2, 'e_m': 5.612216, 'e_o_k': [0.935369, 0.935369, 0.935369], 'p_i': 40, 'u_i': 3.6848},
        {'id': 3, 'e_m': 0.963244, 'e_o_k': [0.240811, 0.240811], 'p_i': 80, 'u_i': 1.6851},
        {'id': 4, 'e_m': 5.443451, 'e_o_k': [0.544345, 0.544345, 0.544345, 0.544345, 0.544345], 'p_i': 20, 'u_i': 1.3700},
        {'id': 5, 'e_m': 1.362619, 'e_o_k': [0.136262, 0.136262, 0.136262, 0.136262, 0.136262], 'p_i': 10, 'u_i': 3.3252},
        {'id': 6, 'e_m': 1.225919, 'e_o_k': [0.306480, 0.306480], 'p_i': 80, 'u_i': 4.3008},
        {'id': 7, 'e_m': 2.933902, 'e_o_k': [0.366738, 0.366738, 0.366738, 0.366738], 'p_i': 80, 'u_i': 2.2362},
    ]
    B_BUDGET = 110.400006
    return processors, tasks, B_BUDGET
