"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119979, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119979, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.965836, 'e_o_k': [0.353924, 0.283139, 0.226511, 0.181209, 0.144967], 'p_i': 10, 'u_i': 1.0447},
        {'id': 1, 'e_m': 6.330156, 'e_o_k': [0.643309, 0.514647, 0.411717, 0.329374], 'p_i': 20, 'u_i': 4.8543},
        {'id': 2, 'e_m': 9.774794, 'e_o_k': [0.794854, 0.635883, 0.508706, 0.406965, 0.325572, 0.260458], 'p_i': 40, 'u_i': 3.5208},
        {'id': 3, 'e_m': 35.370051, 'e_o_k': [4.348777, 3.479021, 2.783217], 'p_i': 80, 'u_i': 2.2132},
        {'id': 4, 'e_m': 2.165172, 'e_o_k': [0.266210, 0.212968, 0.170374], 'p_i': 10, 'u_i': 1.3402},
        {'id': 5, 'e_m': 6.009838, 'e_o_k': [1.001640, 0.801312], 'p_i': 80, 'u_i': 1.7290},
        {'id': 6, 'e_m': 3.956588, 'e_o_k': [0.659431, 0.527545], 'p_i': 10, 'u_i': 2.1135},
        {'id': 7, 'e_m': 4.524561, 'e_o_k': [0.754093, 0.603275], 'p_i': 40, 'u_i': 1.2097},
    ]
    B_BUDGET = 263.119979
    return processors, tasks, B_BUDGET
