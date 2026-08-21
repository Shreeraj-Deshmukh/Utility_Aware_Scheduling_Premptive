"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.020282, 'e_o_k': [1.146130, 0.916904, 0.733523, 0.586819, 0.469455, 0.375564], 'p_i': 10, 'u_i': 2.2803},
        {'id': 1, 'e_m': 0.067315, 'e_o_k': [0.028035, 0.022428, 0.017942, 0.014354, 0.011483], 'p_i': 20, 'u_i': 3.0147},
        {'id': 2, 'e_m': 3.120452, 'e_o_k': [1.479889, 1.183911, 0.947129, 0.757703], 'p_i': 40, 'u_i': 1.8147},
        {'id': 3, 'e_m': 1.327580, 'e_o_k': [0.629611, 0.503689, 0.402951, 0.322361], 'p_i': 80, 'u_i': 2.7697},
    ]
    B_BUDGET = 88.320005
    return processors, tasks, B_BUDGET
