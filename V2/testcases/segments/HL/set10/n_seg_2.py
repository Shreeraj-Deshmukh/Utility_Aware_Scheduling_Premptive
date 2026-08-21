"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400008, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400008, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.443224, 'e_o_k': [0.123118, 0.098494], 'p_i': 10, 'u_i': 2.5678},
        {'id': 1, 'e_m': 0.385037, 'e_o_k': [0.106955, 0.085564], 'p_i': 20, 'u_i': 3.0744},
        {'id': 2, 'e_m': 7.186952, 'e_o_k': [1.996375, 1.597100], 'p_i': 40, 'u_i': 3.1102},
        {'id': 3, 'e_m': 20.620712, 'e_o_k': [5.727975, 4.582380], 'p_i': 80, 'u_i': 3.9862},
        {'id': 4, 'e_m': 1.451540, 'e_o_k': [0.403206, 0.322564], 'p_i': 20, 'u_i': 1.5757},
        {'id': 5, 'e_m': 1.346300, 'e_o_k': [0.373972, 0.299178], 'p_i': 10, 'u_i': 4.9941},
        {'id': 6, 'e_m': 2.067937, 'e_o_k': [0.574427, 0.459542], 'p_i': 40, 'u_i': 1.7632},
        {'id': 7, 'e_m': 1.603507, 'e_o_k': [0.445419, 0.356335], 'p_i': 40, 'u_i': 1.4284},
    ]
    B_BUDGET = 110.400008
    return processors, tasks, B_BUDGET
