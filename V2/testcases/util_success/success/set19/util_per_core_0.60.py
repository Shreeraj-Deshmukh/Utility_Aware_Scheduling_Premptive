"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519998, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519998, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.589131, 'e_o_k': [0.466375, 0.373100, 0.298480, 0.238784], 'p_i': 10, 'u_i': 1.9017},
        {'id': 1, 'e_m': 3.357036, 'e_o_k': [0.559506, 0.447605], 'p_i': 20, 'u_i': 4.1004},
        {'id': 2, 'e_m': 1.125955, 'e_o_k': [0.114426, 0.091541, 0.073233, 0.058586], 'p_i': 40, 'u_i': 2.6358},
        {'id': 3, 'e_m': 7.959752, 'e_o_k': [0.978658, 0.782926, 0.626341], 'p_i': 80, 'u_i': 4.3577},
        {'id': 4, 'e_m': 0.083889, 'e_o_k': [0.008525, 0.006820, 0.005456, 0.004365], 'p_i': 40, 'u_i': 4.2383},
        {'id': 5, 'e_m': 0.136514, 'e_o_k': [0.012183, 0.009746, 0.007797, 0.006238, 0.004990], 'p_i': 80, 'u_i': 1.1754},
        {'id': 6, 'e_m': 27.278529, 'e_o_k': [4.546421, 3.637137], 'p_i': 80, 'u_i': 2.9766},
        {'id': 7, 'e_m': 4.032163, 'e_o_k': [0.327882, 0.262306, 0.209845, 0.167876, 0.134301, 0.107440], 'p_i': 40, 'u_i': 4.8798},
    ]
    B_BUDGET = 143.519998
    return processors, tasks, B_BUDGET
