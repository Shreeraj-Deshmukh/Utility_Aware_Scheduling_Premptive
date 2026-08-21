"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.095169, 'e_o_k': [0.019502, 0.015602, 0.012481], 'p_i': 10, 'u_i': 1.5331},
        {'id': 1, 'e_m': 0.997826, 'e_o_k': [0.204473, 0.163578, 0.130862], 'p_i': 20, 'u_i': 4.3760},
        {'id': 2, 'e_m': 0.022485, 'e_o_k': [0.004608, 0.003686, 0.002949], 'p_i': 40, 'u_i': 3.1042},
        {'id': 3, 'e_m': 2.231053, 'e_o_k': [0.457183, 0.365746, 0.292597], 'p_i': 80, 'u_i': 3.0115},
        {'id': 4, 'e_m': 6.335688, 'e_o_k': [1.298297, 1.038637, 0.830910], 'p_i': 80, 'u_i': 1.0080},
        {'id': 5, 'e_m': 9.200112, 'e_o_k': [1.885269, 1.508215, 1.206572], 'p_i': 80, 'u_i': 3.4234},
        {'id': 6, 'e_m': 6.435349, 'e_o_k': [1.318719, 1.054975, 0.843980], 'p_i': 80, 'u_i': 1.9989},
        {'id': 7, 'e_m': 4.375021, 'e_o_k': [0.896521, 0.717217, 0.573773], 'p_i': 10, 'u_i': 4.9421},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET
