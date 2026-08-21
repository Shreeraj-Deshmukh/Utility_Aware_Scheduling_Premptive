"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519994, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519994, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.073533, 'e_o_k': [0.009041, 0.007233, 0.005786], 'p_i': 10, 'u_i': 1.0223},
        {'id': 1, 'e_m': 3.164103, 'e_o_k': [0.257294, 0.205835, 0.164668, 0.131735, 0.105388, 0.084310], 'p_i': 20, 'u_i': 1.5905},
        {'id': 2, 'e_m': 4.045720, 'e_o_k': [0.674287, 0.539429], 'p_i': 40, 'u_i': 4.0467},
        {'id': 3, 'e_m': 7.489467, 'e_o_k': [0.761125, 0.608900, 0.487120, 0.389696], 'p_i': 80, 'u_i': 4.3793},
        {'id': 4, 'e_m': 28.649321, 'e_o_k': [2.911516, 2.329213, 1.863370, 1.490696], 'p_i': 80, 'u_i': 2.7000},
        {'id': 5, 'e_m': 0.124480, 'e_o_k': [0.012650, 0.010120, 0.008096, 0.006477], 'p_i': 10, 'u_i': 2.7208},
        {'id': 6, 'e_m': 2.188110, 'e_o_k': [0.222369, 0.177895, 0.142316, 0.113853], 'p_i': 80, 'u_i': 2.5904},
        {'id': 7, 'e_m': 8.835287, 'e_o_k': [1.086306, 0.869045, 0.695236], 'p_i': 20, 'u_i': 1.1735},
    ]
    B_BUDGET = 143.519994
    return processors, tasks, B_BUDGET
