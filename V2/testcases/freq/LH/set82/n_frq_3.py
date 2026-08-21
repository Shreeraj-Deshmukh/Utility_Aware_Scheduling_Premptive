"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319979, "H": 80, "J": 32, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "freq", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319979, "H": 80, "J": 32, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "freq", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.7, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.7, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.844903, 'e_o_k': [0.351875, 0.281500, 0.225200, 0.180160, 0.144128], 'p_i': 10, 'u_i': 3.8434},
        {'id': 1, 'e_m': 0.177585, 'e_o_k': [0.138121, 0.110497], 'p_i': 20, 'u_i': 3.7460},
        {'id': 2, 'e_m': 1.433543, 'e_o_k': [0.679865, 0.543892, 0.435113, 0.348091], 'p_i': 40, 'u_i': 2.3844},
        {'id': 3, 'e_m': 1.748862, 'e_o_k': [1.360226, 1.088181], 'p_i': 80, 'u_i': 3.6397},
        {'id': 4, 'e_m': 6.915032, 'e_o_k': [2.624101, 2.099281, 1.679425, 1.343540, 1.074832, 0.859866], 'p_i': 80, 'u_i': 2.0089},
        {'id': 5, 'e_m': 1.550765, 'e_o_k': [0.735458, 0.588366, 0.470693, 0.376554], 'p_i': 20, 'u_i': 4.2973},
        {'id': 6, 'e_m': 0.111141, 'e_o_k': [0.086443, 0.069154], 'p_i': 10, 'u_i': 3.5880},
        {'id': 7, 'e_m': 1.476817, 'e_o_k': [0.560419, 0.448335, 0.358668, 0.286935, 0.229548, 0.183638], 'p_i': 20, 'u_i': 4.0384},
    ]
    B_BUDGET = 88.319979
    return processors, tasks, B_BUDGET
