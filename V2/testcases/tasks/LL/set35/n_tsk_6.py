"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199994, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199994, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.212980, 'e_o_k': [0.028865, 0.023092, 0.018473, 0.014779, 0.011823, 0.009458], 'p_i': 10, 'u_i': 3.7793},
        {'id': 1, 'e_m': 0.218042, 'e_o_k': [0.036931, 0.029545, 0.023636, 0.018909], 'p_i': 20, 'u_i': 1.9533},
        {'id': 2, 'e_m': 3.500668, 'e_o_k': [0.592932, 0.474345, 0.379476, 0.303581], 'p_i': 40, 'u_i': 2.6246},
        {'id': 3, 'e_m': 10.920079, 'e_o_k': [1.479974, 1.183979, 0.947184, 0.757747, 0.606197, 0.484958], 'p_i': 80, 'u_i': 2.3478},
        {'id': 4, 'e_m': 10.673673, 'e_o_k': [2.187228, 1.749782, 1.399826], 'p_i': 80, 'u_i': 2.5491},
        {'id': 5, 'e_m': 0.103613, 'e_o_k': [0.015411, 0.012329, 0.009863, 0.007891, 0.006312], 'p_i': 10, 'u_i': 2.9783},
    ]
    B_BUDGET = 55.199994
    return processors, tasks, B_BUDGET
