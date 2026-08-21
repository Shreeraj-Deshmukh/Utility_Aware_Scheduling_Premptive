"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.212074, 'e_o_k': [1.720502, 1.376402], 'p_i': 10, 'u_i': 4.4310},
        {'id': 1, 'e_m': 2.099648, 'e_o_k': [1.633060, 1.306448], 'p_i': 20, 'u_i': 4.5357},
        {'id': 2, 'e_m': 0.255502, 'e_o_k': [0.198724, 0.158979], 'p_i': 40, 'u_i': 3.5135},
        {'id': 3, 'e_m': 6.162213, 'e_o_k': [4.792832, 3.834266], 'p_i': 80, 'u_i': 3.8723},
        {'id': 4, 'e_m': 3.257255, 'e_o_k': [2.533421, 2.026737], 'p_i': 80, 'u_i': 1.1816},
        {'id': 5, 'e_m': 1.792700, 'e_o_k': [1.394322, 1.115458], 'p_i': 40, 'u_i': 3.3631},
        {'id': 6, 'e_m': 14.597411, 'e_o_k': [11.353542, 9.082834], 'p_i': 80, 'u_i': 2.0216},
        {'id': 7, 'e_m': 1.223941, 'e_o_k': [0.951954, 0.761564], 'p_i': 10, 'u_i': 3.3728},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET
