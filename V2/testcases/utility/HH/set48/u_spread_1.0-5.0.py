"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 29, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "utility", "util_per_core": 0.4, "value": "1.0-5.0"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 29, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "utility", "util_per_core": 0.4, "value": "1.0-5.0"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.372012, 'e_o_k': [1.067120, 0.853696], 'p_i': 10, 'u_i': 2.6470},
        {'id': 1, 'e_m': 3.488332, 'e_o_k': [2.001502, 1.601202, 1.280961], 'p_i': 20, 'u_i': 4.9479},
        {'id': 2, 'e_m': 0.095964, 'e_o_k': [0.055062, 0.044049, 0.035239], 'p_i': 40, 'u_i': 2.1346},
        {'id': 3, 'e_m': 3.859529, 'e_o_k': [3.001856, 2.401485], 'p_i': 80, 'u_i': 1.3827},
        {'id': 4, 'e_m': 11.637726, 'e_o_k': [9.051564, 7.241252], 'p_i': 80, 'u_i': 3.9576},
        {'id': 5, 'e_m': 2.185253, 'e_o_k': [0.910089, 0.728071, 0.582457, 0.465966, 0.372772], 'p_i': 20, 'u_i': 4.9670},
        {'id': 6, 'e_m': 1.684152, 'e_o_k': [0.701396, 0.561117, 0.448894, 0.359115, 0.287292], 'p_i': 10, 'u_i': 4.5958},
        {'id': 7, 'e_m': 1.167163, 'e_o_k': [0.486086, 0.388869, 0.311095, 0.248876, 0.199101], 'p_i': 80, 'u_i': 1.9552},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
