"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320008, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320008, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.047585, 'e_o_k': [0.027303, 0.021842, 0.017474], 'p_i': 10, 'u_i': 1.5331},
        {'id': 1, 'e_m': 0.498913, 'e_o_k': [0.286262, 0.229009, 0.183207], 'p_i': 20, 'u_i': 4.3760},
        {'id': 2, 'e_m': 0.011242, 'e_o_k': [0.006451, 0.005160, 0.004128], 'p_i': 40, 'u_i': 3.1042},
        {'id': 3, 'e_m': 1.115526, 'e_o_k': [0.640056, 0.512045, 0.409636], 'p_i': 80, 'u_i': 3.0115},
        {'id': 4, 'e_m': 3.167844, 'e_o_k': [1.817616, 1.454092, 1.163274], 'p_i': 80, 'u_i': 1.0080},
        {'id': 5, 'e_m': 4.600056, 'e_o_k': [2.639376, 2.111501, 1.689201], 'p_i': 80, 'u_i': 3.4234},
        {'id': 6, 'e_m': 3.217674, 'e_o_k': [1.846207, 1.476965, 1.181572], 'p_i': 80, 'u_i': 1.9989},
        {'id': 7, 'e_m': 2.187511, 'e_o_k': [1.255129, 1.004103, 0.803283], 'p_i': 10, 'u_i': 4.9421},
    ]
    B_BUDGET = 88.320008
    return processors, tasks, B_BUDGET
