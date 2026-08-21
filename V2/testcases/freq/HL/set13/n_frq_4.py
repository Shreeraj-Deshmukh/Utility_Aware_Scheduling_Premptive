"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399997, "H": 80, "J": 33, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "freq", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399997, "H": 80, "J": 33, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "freq", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.112614, 'e_o_k': [0.023077, 0.018461, 0.014769], 'p_i': 10, 'u_i': 4.5768},
        {'id': 1, 'e_m': 0.686888, 'e_o_k': [0.190802, 0.152642], 'p_i': 20, 'u_i': 3.5463},
        {'id': 2, 'e_m': 2.172776, 'e_o_k': [0.603549, 0.482839], 'p_i': 40, 'u_i': 3.4252},
        {'id': 3, 'e_m': 4.314900, 'e_o_k': [0.730844, 0.584675, 0.467740, 0.374192], 'p_i': 80, 'u_i': 1.2792},
        {'id': 4, 'e_m': 0.380745, 'e_o_k': [0.064489, 0.051591, 0.041273, 0.033019], 'p_i': 10, 'u_i': 2.1862},
        {'id': 5, 'e_m': 8.014622, 'e_o_k': [1.642341, 1.313872, 1.051098], 'p_i': 80, 'u_i': 2.5645},
        {'id': 6, 'e_m': 2.193961, 'e_o_k': [0.371606, 0.297285, 0.237828, 0.190262], 'p_i': 10, 'u_i': 2.2998},
        {'id': 7, 'e_m': 23.078811, 'e_o_k': [4.729265, 3.783412, 3.026729], 'p_i': 80, 'u_i': 1.4896},
    ]
    B_BUDGET = 110.399997
    return processors, tasks, B_BUDGET
