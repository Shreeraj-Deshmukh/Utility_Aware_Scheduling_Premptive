"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119991, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119991, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.393261, 'e_o_k': [0.171303, 0.137042, 0.109634], 'p_i': 10, 'u_i': 2.2059},
        {'id': 1, 'e_m': 4.453557, 'e_o_k': [0.452597, 0.362078, 0.289662, 0.231730], 'p_i': 20, 'u_i': 4.0638},
        {'id': 2, 'e_m': 14.590838, 'e_o_k': [1.302133, 1.041707, 0.833365, 0.666692, 0.533354], 'p_i': 40, 'u_i': 4.2047},
        {'id': 3, 'e_m': 27.375088, 'e_o_k': [4.562515, 3.650012], 'p_i': 80, 'u_i': 3.2452},
        {'id': 4, 'e_m': 7.606440, 'e_o_k': [0.618530, 0.494824, 0.395859, 0.316688, 0.253350, 0.202680], 'p_i': 20, 'u_i': 3.8255},
        {'id': 5, 'e_m': 7.514956, 'e_o_k': [1.252493, 1.001994], 'p_i': 80, 'u_i': 2.9448},
        {'id': 6, 'e_m': 3.425467, 'e_o_k': [0.278548, 0.222838, 0.178270, 0.142616, 0.114093, 0.091274], 'p_i': 10, 'u_i': 2.8728},
        {'id': 7, 'e_m': 6.284617, 'e_o_k': [0.560859, 0.448688, 0.358950, 0.287160, 0.229728], 'p_i': 20, 'u_i': 3.0771},
    ]
    B_BUDGET = 263.119991
    return processors, tasks, B_BUDGET
