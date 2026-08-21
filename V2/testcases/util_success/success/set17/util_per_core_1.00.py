"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199997, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199997, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.568853, 'e_o_k': [0.362688, 0.290151, 0.232121, 0.185696], 'p_i': 10, 'u_i': 1.4287},
        {'id': 1, 'e_m': 9.363598, 'e_o_k': [0.835638, 0.668510, 0.534808, 0.427846, 0.342277], 'p_i': 20, 'u_i': 2.2401},
        {'id': 2, 'e_m': 0.870780, 'e_o_k': [0.145130, 0.116104], 'p_i': 40, 'u_i': 3.5755},
        {'id': 3, 'e_m': 38.233031, 'e_o_k': [6.372172, 5.097737], 'p_i': 80, 'u_i': 3.3250},
        {'id': 4, 'e_m': 3.230600, 'e_o_k': [0.262702, 0.210161, 0.168129, 0.134503, 0.107603, 0.086082], 'p_i': 20, 'u_i': 1.4722},
        {'id': 5, 'e_m': 19.360584, 'e_o_k': [1.967539, 1.574031, 1.259225, 1.007380], 'p_i': 80, 'u_i': 3.1189},
        {'id': 6, 'e_m': 9.340998, 'e_o_k': [0.833621, 0.666897, 0.533517, 0.426814, 0.341451], 'p_i': 80, 'u_i': 2.5886},
        {'id': 7, 'e_m': 12.396209, 'e_o_k': [2.066035, 1.652828], 'p_i': 80, 'u_i': 1.4117},
    ]
    B_BUDGET = 239.199997
    return processors, tasks, B_BUDGET
