"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519994, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519994, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.141761, 'e_o_k': [0.012651, 0.010121, 0.008097, 0.006477, 0.005182], 'p_i': 10, 'u_i': 1.6627},
        {'id': 1, 'e_m': 5.807050, 'e_o_k': [0.967842, 0.774273], 'p_i': 20, 'u_i': 3.5149},
        {'id': 2, 'e_m': 0.376276, 'e_o_k': [0.033580, 0.026864, 0.021491, 0.017193, 0.013754], 'p_i': 40, 'u_i': 4.5839},
        {'id': 3, 'e_m': 24.546684, 'e_o_k': [1.996055, 1.596844, 1.277475, 1.021980, 0.817584, 0.654067], 'p_i': 80, 'u_i': 2.6459},
        {'id': 4, 'e_m': 1.942528, 'e_o_k': [0.197411, 0.157929, 0.126343, 0.101075], 'p_i': 20, 'u_i': 4.0652},
        {'id': 5, 'e_m': 0.792830, 'e_o_k': [0.080572, 0.064458, 0.051566, 0.041253], 'p_i': 10, 'u_i': 1.7567},
        {'id': 6, 'e_m': 15.590727, 'e_o_k': [1.267786, 1.014229, 0.811383, 0.649107, 0.519285, 0.415428], 'p_i': 40, 'u_i': 2.4418},
        {'id': 7, 'e_m': 0.130534, 'e_o_k': [0.013266, 0.010612, 0.008490, 0.006792], 'p_i': 10, 'u_i': 4.3648},
    ]
    B_BUDGET = 143.519994
    return processors, tasks, B_BUDGET
