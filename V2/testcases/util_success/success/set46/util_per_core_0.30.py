"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760022, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760022, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.628134, 'e_o_k': [0.077230, 0.061784, 0.049427], 'p_i': 10, 'u_i': 3.9687},
        {'id': 1, 'e_m': 0.375185, 'e_o_k': [0.030509, 0.024407, 0.019526, 0.015621, 0.012496, 0.009997], 'p_i': 20, 'u_i': 2.3030},
        {'id': 2, 'e_m': 7.958521, 'e_o_k': [0.978507, 0.782805, 0.626244], 'p_i': 40, 'u_i': 2.6501},
        {'id': 3, 'e_m': 5.705976, 'e_o_k': [0.509220, 0.407376, 0.325901, 0.260720, 0.208576], 'p_i': 80, 'u_i': 1.7748},
        {'id': 4, 'e_m': 2.119635, 'e_o_k': [0.260611, 0.208489, 0.166791], 'p_i': 20, 'u_i': 3.9815},
        {'id': 5, 'e_m': 0.096790, 'e_o_k': [0.007871, 0.006297, 0.005037, 0.004030, 0.003224, 0.002579], 'p_i': 10, 'u_i': 4.8257},
        {'id': 6, 'e_m': 0.891142, 'e_o_k': [0.079528, 0.063623, 0.050898, 0.040719, 0.032575], 'p_i': 40, 'u_i': 1.0600},
        {'id': 7, 'e_m': 4.408013, 'e_o_k': [0.393385, 0.314708, 0.251767, 0.201413, 0.161131], 'p_i': 40, 'u_i': 2.2764},
    ]
    B_BUDGET = 71.760022
    return processors, tasks, B_BUDGET
