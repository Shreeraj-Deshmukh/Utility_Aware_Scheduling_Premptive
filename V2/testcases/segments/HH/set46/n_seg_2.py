"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639995, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.639995, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.837512, 'e_o_k': [0.651398, 0.521118], 'p_i': 10, 'u_i': 3.9687},
        {'id': 1, 'e_m': 0.500247, 'e_o_k': [0.389081, 0.311265], 'p_i': 20, 'u_i': 3.3202},
        {'id': 2, 'e_m': 10.611361, 'e_o_k': [8.253281, 6.602625], 'p_i': 40, 'u_i': 4.3833},
        {'id': 3, 'e_m': 7.607968, 'e_o_k': [5.917308, 4.733846], 'p_i': 80, 'u_i': 1.8853},
        {'id': 4, 'e_m': 2.826180, 'e_o_k': [2.198140, 1.758512], 'p_i': 20, 'u_i': 2.6679},
        {'id': 5, 'e_m': 0.129053, 'e_o_k': [0.100375, 0.080300], 'p_i': 10, 'u_i': 2.8390},
        {'id': 6, 'e_m': 1.188189, 'e_o_k': [0.924147, 0.739318], 'p_i': 40, 'u_i': 3.5794},
        {'id': 7, 'e_m': 5.877351, 'e_o_k': [4.571273, 3.657018], 'p_i': 40, 'u_i': 4.0478},
    ]
    B_BUDGET = 176.639995
    return processors, tasks, B_BUDGET
