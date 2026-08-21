"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520015, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520015, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.201423, 'e_o_k': [0.020470, 0.016376, 0.013101, 0.010481], 'p_i': 10, 'u_i': 3.0491},
        {'id': 1, 'e_m': 2.392658, 'e_o_k': [0.213529, 0.170823, 0.136658, 0.109327, 0.087461], 'p_i': 20, 'u_i': 3.9469},
        {'id': 2, 'e_m': 6.130496, 'e_o_k': [0.753750, 0.603000, 0.482400], 'p_i': 40, 'u_i': 1.2331},
        {'id': 3, 'e_m': 15.168361, 'e_o_k': [1.864962, 1.491970, 1.193576], 'p_i': 80, 'u_i': 3.8857},
        {'id': 4, 'e_m': 2.873939, 'e_o_k': [0.478990, 0.383192], 'p_i': 20, 'u_i': 4.4773},
        {'id': 5, 'e_m': 1.508046, 'e_o_k': [0.251341, 0.201073], 'p_i': 10, 'u_i': 2.4546},
        {'id': 6, 'e_m': 1.640248, 'e_o_k': [0.166692, 0.133353, 0.106683, 0.085346], 'p_i': 80, 'u_i': 1.1544},
        {'id': 7, 'e_m': 32.188257, 'e_o_k': [3.957573, 3.166058, 2.532846], 'p_i': 80, 'u_i': 4.0204},
    ]
    B_BUDGET = 143.520015
    return processors, tasks, B_BUDGET
