"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320008, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320008, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.726786, 'e_o_k': [0.417008, 0.333607, 0.266885], 'p_i': 10, 'u_i': 1.4749},
        {'id': 1, 'e_m': 3.804665, 'e_o_k': [1.804380, 1.443504, 1.154804, 0.923843], 'p_i': 20, 'u_i': 4.2682},
        {'id': 2, 'e_m': 2.401938, 'e_o_k': [1.000331, 0.800265, 0.640212, 0.512170, 0.409736], 'p_i': 40, 'u_i': 4.6830},
        {'id': 3, 'e_m': 2.065129, 'e_o_k': [1.606212, 1.284969], 'p_i': 80, 'u_i': 2.4027},
        {'id': 4, 'e_m': 0.885724, 'e_o_k': [0.688896, 0.551117], 'p_i': 80, 'u_i': 2.7203},
        {'id': 5, 'e_m': 1.606163, 'e_o_k': [0.609503, 0.487603, 0.390082, 0.312066, 0.249653, 0.199722], 'p_i': 40, 'u_i': 2.4000},
    ]
    B_BUDGET = 88.320008
    return processors, tasks, B_BUDGET
