"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.379864, 'e_o_k': [0.077841, 0.062273, 0.049818], 'p_i': 10, 'u_i': 3.3255},
        {'id': 1, 'e_m': 1.133617, 'e_o_k': [0.232299, 0.185839, 0.148671], 'p_i': 20, 'u_i': 3.5739},
        {'id': 2, 'e_m': 0.770090, 'e_o_k': [0.157805, 0.126244, 0.100995], 'p_i': 40, 'u_i': 2.2786},
        {'id': 3, 'e_m': 4.175854, 'e_o_k': [0.855708, 0.684566, 0.547653], 'p_i': 80, 'u_i': 1.5604},
        {'id': 4, 'e_m': 4.336894, 'e_o_k': [0.888708, 0.710966, 0.568773], 'p_i': 80, 'u_i': 1.1253},
        {'id': 5, 'e_m': 12.059321, 'e_o_k': [2.471172, 1.976938, 1.581550], 'p_i': 80, 'u_i': 3.7966},
        {'id': 6, 'e_m': 0.192411, 'e_o_k': [0.039428, 0.031543, 0.025234], 'p_i': 10, 'u_i': 1.2428},
        {'id': 7, 'e_m': 0.387543, 'e_o_k': [0.079415, 0.063532, 0.050825], 'p_i': 40, 'u_i': 4.6455},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
