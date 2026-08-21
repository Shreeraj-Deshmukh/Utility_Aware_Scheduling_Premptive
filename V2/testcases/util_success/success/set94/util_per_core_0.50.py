"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600007, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600007, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.834541, 'e_o_k': [0.084811, 0.067849, 0.054279, 0.043423], 'p_i': 10, 'u_i': 1.6879},
        {'id': 1, 'e_m': 1.278507, 'e_o_k': [0.129930, 0.103944, 0.083155, 0.066524], 'p_i': 20, 'u_i': 2.2588},
        {'id': 2, 'e_m': 6.190821, 'e_o_k': [1.031804, 0.825443], 'p_i': 40, 'u_i': 4.0829},
        {'id': 3, 'e_m': 9.409501, 'e_o_k': [1.156906, 0.925525, 0.740420], 'p_i': 80, 'u_i': 1.6866},
        {'id': 4, 'e_m': 0.657404, 'e_o_k': [0.080828, 0.064663, 0.051730], 'p_i': 40, 'u_i': 3.5950},
        {'id': 5, 'e_m': 19.626824, 'e_o_k': [3.271137, 2.616910], 'p_i': 80, 'u_i': 4.2025},
        {'id': 6, 'e_m': 7.754536, 'e_o_k': [1.292423, 1.033938], 'p_i': 40, 'u_i': 3.6883},
        {'id': 7, 'e_m': 9.967799, 'e_o_k': [1.661300, 1.329040], 'p_i': 80, 'u_i': 1.6967},
    ]
    B_BUDGET = 119.600007
    return processors, tasks, B_BUDGET
