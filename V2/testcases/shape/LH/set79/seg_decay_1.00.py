"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320024, "H": 80, "J": 20, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.320024, "H": 80, "J": 20, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.340082, 'e_o_k': [0.095223, 0.095223, 0.095223, 0.095223, 0.095223], 'p_i': 10, 'u_i': 4.9110},
        {'id': 1, 'e_m': 0.844927, 'e_o_k': [0.197150, 0.197150, 0.197150, 0.197150, 0.197150, 0.197150], 'p_i': 20, 'u_i': 1.5555},
        {'id': 2, 'e_m': 0.259808, 'e_o_k': [0.121244, 0.121244, 0.121244], 'p_i': 40, 'u_i': 1.9189},
        {'id': 3, 'e_m': 9.047231, 'e_o_k': [6.333062, 6.333062], 'p_i': 80, 'u_i': 3.1608},
        {'id': 4, 'e_m': 2.504897, 'e_o_k': [1.753428, 1.753428], 'p_i': 80, 'u_i': 1.3239},
        {'id': 5, 'e_m': 0.977966, 'e_o_k': [0.342288, 0.342288, 0.342288, 0.342288], 'p_i': 80, 'u_i': 4.3282},
        {'id': 6, 'e_m': 5.375256, 'e_o_k': [3.762679, 3.762679], 'p_i': 40, 'u_i': 3.0285},
        {'id': 7, 'e_m': 2.099419, 'e_o_k': [0.734796, 0.734796, 0.734796, 0.734796], 'p_i': 80, 'u_i': 4.7214},
    ]
    B_BUDGET = 88.320024
    return processors, tasks, B_BUDGET
