"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200011, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.200011, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.350656, 'e_o_k': [0.035066, 0.035066, 0.035066, 0.035066, 0.035066], 'p_i': 10, 'u_i': 4.4298},
        {'id': 1, 'e_m': 3.430445, 'e_o_k': [0.571741, 0.571741, 0.571741], 'p_i': 20, 'u_i': 1.5050},
        {'id': 2, 'e_m': 0.207300, 'e_o_k': [0.051825, 0.051825], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 1.714842, 'e_o_k': [0.142903, 0.142903, 0.142903, 0.142903, 0.142903, 0.142903], 'p_i': 80, 'u_i': 4.0993},
        {'id': 4, 'e_m': 0.699429, 'e_o_k': [0.174857, 0.174857], 'p_i': 20, 'u_i': 2.5958},
        {'id': 5, 'e_m': 2.747339, 'e_o_k': [0.457890, 0.457890, 0.457890], 'p_i': 80, 'u_i': 1.3643},
        {'id': 6, 'e_m': 2.551296, 'e_o_k': [0.212608, 0.212608, 0.212608, 0.212608, 0.212608, 0.212608], 'p_i': 40, 'u_i': 1.6218},
        {'id': 7, 'e_m': 2.695881, 'e_o_k': [0.336985, 0.336985, 0.336985, 0.336985], 'p_i': 80, 'u_i': 1.2955},
    ]
    B_BUDGET = 55.200011
    return processors, tasks, B_BUDGET
