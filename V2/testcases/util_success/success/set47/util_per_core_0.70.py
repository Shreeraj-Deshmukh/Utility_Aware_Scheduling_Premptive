"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439997, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439997, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.258513, 'e_o_k': [0.380043, 0.304035, 0.243228, 0.194582, 0.155666], 'p_i': 10, 'u_i': 3.4259},
        {'id': 1, 'e_m': 2.937663, 'e_o_k': [0.298543, 0.238834, 0.191067, 0.152854], 'p_i': 20, 'u_i': 1.3819},
        {'id': 2, 'e_m': 4.721005, 'e_o_k': [0.786834, 0.629467], 'p_i': 40, 'u_i': 1.7445},
        {'id': 3, 'e_m': 9.770981, 'e_o_k': [0.794544, 0.635635, 0.508508, 0.406806, 0.325445, 0.260356], 'p_i': 80, 'u_i': 3.6642},
        {'id': 4, 'e_m': 1.679941, 'e_o_k': [0.170726, 0.136581, 0.109264, 0.087412], 'p_i': 10, 'u_i': 2.6174},
        {'id': 5, 'e_m': 2.100641, 'e_o_k': [0.187468, 0.149974, 0.119980, 0.095984, 0.076787], 'p_i': 10, 'u_i': 2.3254},
        {'id': 6, 'e_m': 0.341823, 'e_o_k': [0.056971, 0.045576], 'p_i': 10, 'u_i': 3.2626},
        {'id': 7, 'e_m': 6.994502, 'e_o_k': [0.624212, 0.499370, 0.399496, 0.319596, 0.255677], 'p_i': 40, 'u_i': 1.6837},
    ]
    B_BUDGET = 167.439997
    return processors, tasks, B_BUDGET
