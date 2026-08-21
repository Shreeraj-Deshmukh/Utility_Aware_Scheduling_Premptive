"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320005, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.320005, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.844903, 'e_o_k': [0.657147, 0.525718], 'p_i': 10, 'u_i': 3.8434},
        {'id': 1, 'e_m': 0.177585, 'e_o_k': [0.138121, 0.110497], 'p_i': 20, 'u_i': 3.7460},
        {'id': 2, 'e_m': 1.433543, 'e_o_k': [1.114978, 0.891982], 'p_i': 40, 'u_i': 2.3844},
        {'id': 3, 'e_m': 1.748862, 'e_o_k': [1.360226, 1.088181], 'p_i': 80, 'u_i': 3.6397},
        {'id': 4, 'e_m': 6.915032, 'e_o_k': [5.378358, 4.302687], 'p_i': 80, 'u_i': 2.3882},
        {'id': 5, 'e_m': 1.550765, 'e_o_k': [1.206151, 0.964921], 'p_i': 20, 'u_i': 4.1284},
        {'id': 6, 'e_m': 0.111141, 'e_o_k': [0.086443, 0.069154], 'p_i': 10, 'u_i': 3.5880},
        {'id': 7, 'e_m': 1.476817, 'e_o_k': [1.148636, 0.918908], 'p_i': 20, 'u_i': 3.2846},
    ]
    B_BUDGET = 88.320005
    return processors, tasks, B_BUDGET
