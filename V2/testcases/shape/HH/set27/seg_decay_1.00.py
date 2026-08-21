"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640016, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 176.640016, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.415674, 'e_o_k': [1.195486, 1.195486, 1.195486, 1.195486], 'p_i': 10, 'u_i': 3.9517},
        {'id': 1, 'e_m': 0.148832, 'e_o_k': [0.041673, 0.041673, 0.041673, 0.041673, 0.041673], 'p_i': 20, 'u_i': 3.7467},
        {'id': 2, 'e_m': 2.086145, 'e_o_k': [0.584121, 0.584121, 0.584121, 0.584121, 0.584121], 'p_i': 40, 'u_i': 4.6120},
        {'id': 3, 'e_m': 0.844474, 'e_o_k': [0.591132, 0.591132], 'p_i': 80, 'u_i': 4.9202},
        {'id': 4, 'e_m': 1.893474, 'e_o_k': [1.325432, 1.325432], 'p_i': 80, 'u_i': 4.2451},
        {'id': 5, 'e_m': 1.089996, 'e_o_k': [0.762997, 0.762997], 'p_i': 10, 'u_i': 4.7909},
        {'id': 6, 'e_m': 2.548948, 'e_o_k': [0.892132, 0.892132, 0.892132, 0.892132], 'p_i': 10, 'u_i': 3.3523},
        {'id': 7, 'e_m': 0.028745, 'e_o_k': [0.010061, 0.010061, 0.010061, 0.010061], 'p_i': 40, 'u_i': 1.0347},
    ]
    B_BUDGET = 176.640016
    return processors, tasks, B_BUDGET
