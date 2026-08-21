"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400007, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400007, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.425961, 'e_o_k': [0.057730, 0.046184, 0.036947, 0.029558, 0.023646, 0.018917], 'p_i': 10, 'u_i': 3.7793},
        {'id': 1, 'e_m': 0.436083, 'e_o_k': [0.073862, 0.059090, 0.047272, 0.037818], 'p_i': 20, 'u_i': 1.9533},
        {'id': 2, 'e_m': 7.001336, 'e_o_k': [1.185863, 0.948691, 0.758952, 0.607162], 'p_i': 40, 'u_i': 2.6246},
        {'id': 3, 'e_m': 21.840159, 'e_o_k': [2.959949, 2.367959, 1.894367, 1.515494, 1.212395, 0.969916], 'p_i': 80, 'u_i': 2.3478},
        {'id': 4, 'e_m': 21.347346, 'e_o_k': [4.374456, 3.499565, 2.799652], 'p_i': 80, 'u_i': 2.5491},
        {'id': 5, 'e_m': 0.207225, 'e_o_k': [0.030822, 0.024658, 0.019726, 0.015781, 0.012625], 'p_i': 10, 'u_i': 2.9783},
    ]
    B_BUDGET = 110.400007
    return processors, tasks, B_BUDGET
