"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760014, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760014, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.190436, 'e_o_k': [0.015486, 0.012388, 0.009911, 0.007929, 0.006343, 0.005074], 'p_i': 10, 'u_i': 1.0975},
        {'id': 1, 'e_m': 1.833373, 'e_o_k': [0.186318, 0.149055, 0.119244, 0.095395], 'p_i': 20, 'u_i': 4.1970},
        {'id': 2, 'e_m': 1.078801, 'e_o_k': [0.087725, 0.070180, 0.056144, 0.044915, 0.035932, 0.028746], 'p_i': 40, 'u_i': 1.7417},
        {'id': 3, 'e_m': 6.755179, 'e_o_k': [0.602854, 0.482283, 0.385827, 0.308661, 0.246929], 'p_i': 80, 'u_i': 3.7063},
        {'id': 4, 'e_m': 0.710567, 'e_o_k': [0.087365, 0.069892, 0.055913], 'p_i': 20, 'u_i': 3.7708},
        {'id': 5, 'e_m': 0.729825, 'e_o_k': [0.074169, 0.059335, 0.047468, 0.037975], 'p_i': 20, 'u_i': 3.9372},
        {'id': 6, 'e_m': 0.784725, 'e_o_k': [0.096483, 0.077186, 0.061749], 'p_i': 20, 'u_i': 1.6580},
        {'id': 7, 'e_m': 21.329776, 'e_o_k': [2.622513, 2.098011, 1.678409], 'p_i': 80, 'u_i': 4.1894},
    ]
    B_BUDGET = 71.760014
    return processors, tasks, B_BUDGET
