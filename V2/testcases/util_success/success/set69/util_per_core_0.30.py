"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760008, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760008, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.043277, 'e_o_k': [0.005321, 0.004257, 0.003405], 'p_i': 10, 'u_i': 3.1857},
        {'id': 1, 'e_m': 0.637565, 'e_o_k': [0.106261, 0.085009], 'p_i': 20, 'u_i': 3.0673},
        {'id': 2, 'e_m': 0.557215, 'e_o_k': [0.049728, 0.039782, 0.031826, 0.025461, 0.020368], 'p_i': 40, 'u_i': 1.1608},
        {'id': 3, 'e_m': 5.398571, 'e_o_k': [0.663759, 0.531007, 0.424806], 'p_i': 80, 'u_i': 3.0557},
        {'id': 4, 'e_m': 8.130835, 'e_o_k': [0.725622, 0.580498, 0.464398, 0.371518, 0.297215], 'p_i': 80, 'u_i': 1.7105},
        {'id': 5, 'e_m': 22.757037, 'e_o_k': [2.797996, 2.238397, 1.790718], 'p_i': 80, 'u_i': 2.7562},
        {'id': 6, 'e_m': 0.950615, 'e_o_k': [0.096607, 0.077286, 0.061829, 0.049463], 'p_i': 20, 'u_i': 4.1777},
        {'id': 7, 'e_m': 3.900192, 'e_o_k': [0.650032, 0.520026], 'p_i': 80, 'u_i': 1.3396},
    ]
    B_BUDGET = 71.760008
    return processors, tasks, B_BUDGET
