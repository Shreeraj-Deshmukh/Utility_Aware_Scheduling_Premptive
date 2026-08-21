"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400003, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.400003, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.255086, 'e_o_k': [0.055319, 0.033191, 0.019915, 0.011949, 0.007169], 'p_i': 10, 'u_i': 1.4092},
        {'id': 1, 'e_m': 1.766930, 'e_o_k': [0.450747, 0.270448, 0.162269], 'p_i': 20, 'u_i': 2.7448},
        {'id': 2, 'e_m': 4.717796, 'e_o_k': [1.023117, 0.613870, 0.368322, 0.220993, 0.132596], 'p_i': 40, 'u_i': 3.9391},
        {'id': 3, 'e_m': 2.076602, 'e_o_k': [0.477160, 0.286296, 0.171778, 0.103067], 'p_i': 80, 'u_i': 3.4662},
        {'id': 4, 'e_m': 0.980401, 'e_o_k': [0.205676, 0.123406, 0.074043, 0.044426, 0.026656, 0.015993], 'p_i': 40, 'u_i': 1.3531},
        {'id': 5, 'e_m': 28.292425, 'e_o_k': [8.841383, 5.304830], 'p_i': 80, 'u_i': 3.5457},
        {'id': 6, 'e_m': 0.799254, 'e_o_k': [0.249767, 0.149860], 'p_i': 10, 'u_i': 1.4096},
        {'id': 7, 'e_m': 1.683036, 'e_o_k': [0.386727, 0.232036, 0.139222, 0.083533], 'p_i': 20, 'u_i': 4.8654},
    ]
    B_BUDGET = 110.400003
    return processors, tasks, B_BUDGET
