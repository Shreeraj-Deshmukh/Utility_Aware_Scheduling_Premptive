"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639992, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639992, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.080666, 'e_o_k': [0.030611, 0.024489, 0.019591, 0.015673, 0.012538, 0.010031], 'p_i': 10, 'u_i': 1.7448},
        {'id': 1, 'e_m': 1.254278, 'e_o_k': [0.522367, 0.417894, 0.334315, 0.267452, 0.213962], 'p_i': 20, 'u_i': 2.9486},
        {'id': 2, 'e_m': 1.191263, 'e_o_k': [0.496123, 0.396899, 0.317519, 0.254015, 0.203212], 'p_i': 40, 'u_i': 1.5908},
        {'id': 3, 'e_m': 12.891421, 'e_o_k': [5.368869, 4.295095, 3.436076, 2.748861, 2.199089], 'p_i': 80, 'u_i': 1.2188},
        {'id': 4, 'e_m': 2.735946, 'e_o_k': [1.569805, 1.255844, 1.004675], 'p_i': 10, 'u_i': 2.5958},
        {'id': 5, 'e_m': 2.647005, 'e_o_k': [1.518773, 1.215019, 0.972015], 'p_i': 10, 'u_i': 3.0557},
    ]
    B_BUDGET = 176.639992
    return processors, tasks, B_BUDGET
