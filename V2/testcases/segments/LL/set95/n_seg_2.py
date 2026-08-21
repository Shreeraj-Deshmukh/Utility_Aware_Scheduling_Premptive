"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199997, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199997, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.791911, 'e_o_k': [0.219975, 0.175980], 'p_i': 10, 'u_i': 1.9313},
        {'id': 1, 'e_m': 1.455094, 'e_o_k': [0.404193, 0.323354], 'p_i': 20, 'u_i': 4.0147},
        {'id': 2, 'e_m': 3.411616, 'e_o_k': [0.947671, 0.758137], 'p_i': 40, 'u_i': 4.3076},
        {'id': 3, 'e_m': 1.509835, 'e_o_k': [0.419399, 0.335519], 'p_i': 80, 'u_i': 2.0651},
        {'id': 4, 'e_m': 1.958205, 'e_o_k': [0.543946, 0.435157], 'p_i': 80, 'u_i': 2.7475},
        {'id': 5, 'e_m': 1.353233, 'e_o_k': [0.375898, 0.300718], 'p_i': 40, 'u_i': 2.9584},
        {'id': 6, 'e_m': 4.115647, 'e_o_k': [1.143235, 0.914588], 'p_i': 80, 'u_i': 3.8181},
        {'id': 7, 'e_m': 0.682738, 'e_o_k': [0.189649, 0.151720], 'p_i': 20, 'u_i': 3.4213},
    ]
    B_BUDGET = 55.199997
    return processors, tasks, B_BUDGET
