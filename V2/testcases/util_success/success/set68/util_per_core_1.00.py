"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199974, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199974, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.037238, 'e_o_k': [0.127529, 0.102023, 0.081619], 'p_i': 10, 'u_i': 1.1616},
        {'id': 1, 'e_m': 3.962705, 'e_o_k': [0.487218, 0.389774, 0.311819], 'p_i': 20, 'u_i': 1.7018},
        {'id': 2, 'e_m': 17.513689, 'e_o_k': [2.153322, 1.722658, 1.378126], 'p_i': 40, 'u_i': 3.8642},
        {'id': 3, 'e_m': 18.180420, 'e_o_k': [3.030070, 2.424056], 'p_i': 80, 'u_i': 1.2777},
        {'id': 4, 'e_m': 5.991028, 'e_o_k': [0.608844, 0.487075, 0.389660, 0.311728], 'p_i': 20, 'u_i': 4.6633},
        {'id': 5, 'e_m': 5.752177, 'e_o_k': [0.584571, 0.467657, 0.374125, 0.299300], 'p_i': 20, 'u_i': 1.0039},
        {'id': 6, 'e_m': 0.186500, 'e_o_k': [0.022930, 0.018344, 0.014675], 'p_i': 10, 'u_i': 3.4899},
        {'id': 7, 'e_m': 34.178656, 'e_o_k': [5.696443, 4.557154], 'p_i': 80, 'u_i': 3.2831},
    ]
    B_BUDGET = 239.199974
    return processors, tasks, B_BUDGET
