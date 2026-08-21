"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640013, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640013, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.488440, 'e_o_k': [0.280253, 0.224202, 0.179362], 'p_i': 10, 'u_i': 1.2408},
        {'id': 1, 'e_m': 0.924655, 'e_o_k': [0.530540, 0.424432, 0.339546], 'p_i': 20, 'u_i': 2.7274},
        {'id': 2, 'e_m': 2.288327, 'e_o_k': [1.312974, 1.050379, 0.840304], 'p_i': 40, 'u_i': 3.7398},
        {'id': 3, 'e_m': 4.657210, 'e_o_k': [2.672170, 2.137736, 1.710189], 'p_i': 80, 'u_i': 1.4758},
        {'id': 4, 'e_m': 0.144768, 'e_o_k': [0.083063, 0.066451, 0.053161], 'p_i': 10, 'u_i': 4.3036},
        {'id': 5, 'e_m': 0.140954, 'e_o_k': [0.080875, 0.064700, 0.051760], 'p_i': 40, 'u_i': 3.9596},
        {'id': 6, 'e_m': 4.924673, 'e_o_k': [2.825632, 2.260506, 1.808404], 'p_i': 20, 'u_i': 3.9830},
        {'id': 7, 'e_m': 3.252657, 'e_o_k': [1.866278, 1.493023, 1.194418], 'p_i': 10, 'u_i': 3.3191},
    ]
    B_BUDGET = 176.640013
    return processors, tasks, B_BUDGET
