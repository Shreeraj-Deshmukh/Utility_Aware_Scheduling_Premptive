"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520002, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520002, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.020245, 'e_o_k': [0.091050, 0.072840, 0.058272, 0.046618, 0.037294], 'p_i': 10, 'u_i': 4.9110},
        {'id': 1, 'e_m': 2.534780, 'e_o_k': [0.206120, 0.164896, 0.131917, 0.105533, 0.084427, 0.067541], 'p_i': 20, 'u_i': 1.5555},
        {'id': 2, 'e_m': 0.779423, 'e_o_k': [0.095831, 0.076665, 0.061332], 'p_i': 40, 'u_i': 1.9189},
        {'id': 3, 'e_m': 27.141692, 'e_o_k': [4.523615, 3.618892], 'p_i': 80, 'u_i': 3.1608},
        {'id': 4, 'e_m': 7.514691, 'e_o_k': [1.252448, 1.001959], 'p_i': 80, 'u_i': 1.3239},
        {'id': 5, 'e_m': 2.933897, 'e_o_k': [0.298160, 0.238528, 0.190823, 0.152658], 'p_i': 80, 'u_i': 4.3282},
        {'id': 6, 'e_m': 16.125768, 'e_o_k': [2.687628, 2.150102], 'p_i': 40, 'u_i': 3.0285},
        {'id': 7, 'e_m': 6.298256, 'e_o_k': [0.640067, 0.512053, 0.409643, 0.327714], 'p_i': 80, 'u_i': 4.7214},
    ]
    B_BUDGET = 143.520002
    return processors, tasks, B_BUDGET
