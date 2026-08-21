"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.047585, 'e_o_k': [0.037010, 0.029608], 'p_i': 10, 'u_i': 1.5331},
        {'id': 1, 'e_m': 0.498913, 'e_o_k': [0.388043, 0.310435], 'p_i': 20, 'u_i': 4.3760},
        {'id': 2, 'e_m': 0.011242, 'e_o_k': [0.008744, 0.006995], 'p_i': 40, 'u_i': 3.1042},
        {'id': 3, 'e_m': 1.115526, 'e_o_k': [0.867632, 0.694105], 'p_i': 80, 'u_i': 3.0115},
        {'id': 4, 'e_m': 3.167844, 'e_o_k': [2.463879, 1.971103], 'p_i': 80, 'u_i': 1.0080},
        {'id': 5, 'e_m': 4.600056, 'e_o_k': [3.577821, 2.862257], 'p_i': 80, 'u_i': 3.4234},
        {'id': 6, 'e_m': 3.217674, 'e_o_k': [2.502636, 2.002108], 'p_i': 80, 'u_i': 1.9989},
        {'id': 7, 'e_m': 2.187511, 'e_o_k': [1.701397, 1.361118], 'p_i': 10, 'u_i': 4.9421},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
