"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400011, "H": 80, "J": 20, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400011, "H": 80, "J": 20, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.722458, 'e_o_k': [0.148045, 0.118436, 0.094749], 'p_i': 10, 'u_i': 1.0216},
        {'id': 1, 'e_m': 3.086888, 'e_o_k': [0.632559, 0.506047, 0.404838], 'p_i': 20, 'u_i': 4.0085},
        {'id': 2, 'e_m': 11.212672, 'e_o_k': [2.297679, 1.838143, 1.470514], 'p_i': 40, 'u_i': 1.9931},
        {'id': 3, 'e_m': 4.466066, 'e_o_k': [0.915177, 0.732142, 0.585714], 'p_i': 80, 'u_i': 2.4773},
        {'id': 4, 'e_m': 0.168840, 'e_o_k': [0.034598, 0.027679, 0.022143], 'p_i': 80, 'u_i': 3.1022},
        {'id': 5, 'e_m': 1.988081, 'e_o_k': [0.407394, 0.325915, 0.260732], 'p_i': 40, 'u_i': 1.7440},
        {'id': 6, 'e_m': 7.911221, 'e_o_k': [1.621152, 1.296922, 1.037537], 'p_i': 80, 'u_i': 1.2190},
        {'id': 7, 'e_m': 6.925151, 'e_o_k': [1.419088, 1.135271, 0.908217], 'p_i': 80, 'u_i': 2.8489},
    ]
    B_BUDGET = 110.400011
    return processors, tasks, B_BUDGET
