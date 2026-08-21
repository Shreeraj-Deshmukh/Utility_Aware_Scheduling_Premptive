"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199994, "H": 80, "J": 26, "factor": "n_frq", "n_frq": 2, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "freq", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199994, "H": 80, "J": 26, "factor": "n_frq", "n_frq": 2, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "freq", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 1.0]},
        {'id': 1, 'frequencies': [0.4, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.143220, 'e_o_k': [0.193635, 0.154908, 0.123926, 0.099141], 'p_i': 10, 'u_i': 1.7025},
        {'id': 1, 'e_m': 0.721620, 'e_o_k': [0.107333, 0.085866, 0.068693, 0.054954, 0.043964], 'p_i': 20, 'u_i': 2.0058},
        {'id': 2, 'e_m': 0.561215, 'e_o_k': [0.155893, 0.124714], 'p_i': 40, 'u_i': 3.5722},
        {'id': 3, 'e_m': 9.907138, 'e_o_k': [1.678038, 1.342431, 1.073945, 0.859156], 'p_i': 80, 'u_i': 1.2384},
        {'id': 4, 'e_m': 0.924900, 'e_o_k': [0.256917, 0.205533], 'p_i': 40, 'u_i': 4.5379},
        {'id': 5, 'e_m': 1.311382, 'e_o_k': [0.364273, 0.291418], 'p_i': 20, 'u_i': 1.9982},
        {'id': 6, 'e_m': 0.152759, 'e_o_k': [0.042433, 0.033946], 'p_i': 20, 'u_i': 2.1252},
        {'id': 7, 'e_m': 1.231826, 'e_o_k': [0.208643, 0.166914, 0.133531, 0.106825], 'p_i': 80, 'u_i': 4.2384},
    ]
    B_BUDGET = 55.199994
    return processors, tasks, B_BUDGET
