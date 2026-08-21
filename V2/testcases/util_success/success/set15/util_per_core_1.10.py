"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119987, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119987, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.235048, 'e_o_k': [0.100430, 0.080344, 0.064275, 0.051420, 0.041136, 0.032909], 'p_i': 10, 'u_i': 1.5997},
        {'id': 1, 'e_m': 3.495703, 'e_o_k': [0.582617, 0.466094], 'p_i': 20, 'u_i': 4.7941},
        {'id': 2, 'e_m': 15.199826, 'e_o_k': [1.544698, 1.235758, 0.988607, 0.790885], 'p_i': 40, 'u_i': 3.5328},
        {'id': 3, 'e_m': 22.646079, 'e_o_k': [1.841504, 1.473203, 1.178563, 0.942850, 0.754280, 0.603424], 'p_i': 80, 'u_i': 3.7747},
        {'id': 4, 'e_m': 10.454112, 'e_o_k': [0.932959, 0.746367, 0.597094, 0.477675, 0.382140], 'p_i': 40, 'u_i': 3.0844},
        {'id': 5, 'e_m': 18.468325, 'e_o_k': [1.501783, 1.201426, 0.961141, 0.768913, 0.615130, 0.492104], 'p_i': 40, 'u_i': 1.4908},
        {'id': 6, 'e_m': 35.973434, 'e_o_k': [5.995572, 4.796458], 'p_i': 80, 'u_i': 2.9455},
        {'id': 7, 'e_m': 0.659095, 'e_o_k': [0.109849, 0.087879], 'p_i': 10, 'u_i': 4.7629},
    ]
    B_BUDGET = 263.119987
    return processors, tasks, B_BUDGET
