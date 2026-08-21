"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120005, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120005, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.156372, 'e_o_k': [0.219144, 0.175315, 0.140252, 0.112201], 'p_i': 10, 'u_i': 1.8134},
        {'id': 1, 'e_m': 5.036587, 'e_o_k': [0.839431, 0.671545], 'p_i': 20, 'u_i': 3.0607},
        {'id': 2, 'e_m': 14.762250, 'e_o_k': [1.200417, 0.960334, 0.768267, 0.614614, 0.491691, 0.393353], 'p_i': 40, 'u_i': 3.2825},
        {'id': 3, 'e_m': 25.694717, 'e_o_k': [2.293079, 1.834463, 1.467571, 1.174057, 0.939245], 'p_i': 80, 'u_i': 2.2646},
        {'id': 4, 'e_m': 3.179559, 'e_o_k': [0.258551, 0.206841, 0.165473, 0.132378, 0.105903, 0.084722], 'p_i': 10, 'u_i': 4.1633},
        {'id': 5, 'e_m': 2.399807, 'e_o_k': [0.295058, 0.236047, 0.188837], 'p_i': 10, 'u_i': 1.6770},
        {'id': 6, 'e_m': 1.139356, 'e_o_k': [0.115788, 0.092631, 0.074104, 0.059284], 'p_i': 10, 'u_i': 4.7434},
        {'id': 7, 'e_m': 7.408420, 'e_o_k': [0.910871, 0.728697, 0.582958], 'p_i': 20, 'u_i': 4.2977},
    ]
    B_BUDGET = 263.120005
    return processors, tasks, B_BUDGET
