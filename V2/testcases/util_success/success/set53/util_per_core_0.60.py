"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519998, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519998, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.477092, 'e_o_k': [0.079515, 0.063612], 'p_i': 10, 'u_i': 1.8047},
        {'id': 1, 'e_m': 3.656477, 'e_o_k': [0.609413, 0.487530], 'p_i': 20, 'u_i': 1.0945},
        {'id': 2, 'e_m': 2.987376, 'e_o_k': [0.266603, 0.213282, 0.170626, 0.136501, 0.109201], 'p_i': 40, 'u_i': 2.4137},
        {'id': 3, 'e_m': 16.109590, 'e_o_k': [2.684932, 2.147945], 'p_i': 80, 'u_i': 1.6729},
        {'id': 4, 'e_m': 2.755466, 'e_o_k': [0.224065, 0.179252, 0.143402, 0.114721, 0.091777, 0.073422], 'p_i': 40, 'u_i': 2.8481},
        {'id': 5, 'e_m': 2.554389, 'e_o_k': [0.259592, 0.207674, 0.166139, 0.132911], 'p_i': 10, 'u_i': 3.6691},
        {'id': 6, 'e_m': 4.290656, 'e_o_k': [0.436042, 0.348834, 0.279067, 0.223254], 'p_i': 20, 'u_i': 3.0767},
        {'id': 7, 'e_m': 12.364353, 'e_o_k': [1.005428, 0.804343, 0.643474, 0.514779, 0.411823, 0.329459], 'p_i': 80, 'u_i': 1.7471},
    ]
    B_BUDGET = 143.519998
    return processors, tasks, B_BUDGET
