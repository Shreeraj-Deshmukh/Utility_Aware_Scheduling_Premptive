"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639998, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639998, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.145778, 'e_o_k': [0.893649, 0.714919, 0.571935, 0.457548, 0.366039], 'p_i': 10, 'u_i': 4.5978},
        {'id': 1, 'e_m': 6.335860, 'e_o_k': [3.635330, 2.908264, 2.326611], 'p_i': 20, 'u_i': 3.9895},
        {'id': 2, 'e_m': 3.211158, 'e_o_k': [2.497568, 1.998054], 'p_i': 40, 'u_i': 3.6989},
        {'id': 3, 'e_m': 7.854319, 'e_o_k': [3.724948, 2.979958, 2.383967, 1.907173], 'p_i': 80, 'u_i': 3.2467},
        {'id': 4, 'e_m': 2.331101, 'e_o_k': [1.337517, 1.070014, 0.856011], 'p_i': 80, 'u_i': 4.5958},
        {'id': 5, 'e_m': 2.441297, 'e_o_k': [1.157797, 0.926237, 0.740990, 0.592792], 'p_i': 40, 'u_i': 4.0042},
    ]
    B_BUDGET = 176.639998
    return processors, tasks, B_BUDGET
