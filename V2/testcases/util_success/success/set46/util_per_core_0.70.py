"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439986, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439986, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.465645, 'e_o_k': [0.180202, 0.144162, 0.115329], 'p_i': 10, 'u_i': 3.9687},
        {'id': 1, 'e_m': 0.875432, 'e_o_k': [0.071187, 0.056950, 0.045560, 0.036448, 0.029158, 0.023327], 'p_i': 20, 'u_i': 2.3030},
        {'id': 2, 'e_m': 18.569882, 'e_o_k': [2.283182, 1.826546, 1.461237], 'p_i': 40, 'u_i': 2.6501},
        {'id': 3, 'e_m': 13.313943, 'e_o_k': [1.188179, 0.950543, 0.760435, 0.608348, 0.486678], 'p_i': 80, 'u_i': 1.7748},
        {'id': 4, 'e_m': 4.945816, 'e_o_k': [0.608092, 0.486474, 0.389179], 'p_i': 20, 'u_i': 3.9815},
        {'id': 5, 'e_m': 0.225843, 'e_o_k': [0.018365, 0.014692, 0.011753, 0.009403, 0.007522, 0.006018], 'p_i': 10, 'u_i': 4.8257},
        {'id': 6, 'e_m': 2.079331, 'e_o_k': [0.185566, 0.148453, 0.118762, 0.095010, 0.076008], 'p_i': 40, 'u_i': 1.0600},
        {'id': 7, 'e_m': 10.285364, 'e_o_k': [0.917899, 0.734319, 0.587455, 0.469964, 0.375971], 'p_i': 40, 'u_i': 2.2764},
    ]
    B_BUDGET = 167.439986
    return processors, tasks, B_BUDGET
