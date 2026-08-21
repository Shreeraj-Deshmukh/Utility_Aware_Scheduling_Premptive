"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200023, "H": 80, "J": 35, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.200023, "H": 80, "J": 35, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.217662, 'e_o_k': [0.054416, 0.054416], 'p_i': 10, 'u_i': 1.4412},
        {'id': 1, 'e_m': 1.846208, 'e_o_k': [0.230776, 0.230776, 0.230776, 0.230776], 'p_i': 20, 'u_i': 3.7136},
        {'id': 2, 'e_m': 0.830898, 'e_o_k': [0.069241, 0.069241, 0.069241, 0.069241, 0.069241, 0.069241], 'p_i': 40, 'u_i': 3.0715},
        {'id': 3, 'e_m': 10.940022, 'e_o_k': [0.911669, 0.911669, 0.911669, 0.911669, 0.911669, 0.911669], 'p_i': 80, 'u_i': 2.1053},
        {'id': 4, 'e_m': 0.087893, 'e_o_k': [0.021973, 0.021973], 'p_i': 20, 'u_i': 3.9261},
        {'id': 5, 'e_m': 0.266000, 'e_o_k': [0.066500, 0.066500], 'p_i': 20, 'u_i': 2.2961},
        {'id': 6, 'e_m': 0.085726, 'e_o_k': [0.008573, 0.008573, 0.008573, 0.008573, 0.008573], 'p_i': 10, 'u_i': 1.3761},
        {'id': 7, 'e_m': 2.042668, 'e_o_k': [0.340445, 0.340445, 0.340445], 'p_i': 20, 'u_i': 2.1930},
    ]
    B_BUDGET = 55.200023
    return processors, tasks, B_BUDGET
