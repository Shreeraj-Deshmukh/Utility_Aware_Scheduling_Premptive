"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320016, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.320016, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.355801, 'e_o_k': [0.311326, 0.186795], 'p_i': 10, 'u_i': 2.6844},
        {'id': 1, 'e_m': 0.978019, 'e_o_k': [0.574494, 0.344697, 0.206818, 0.124091, 0.074454, 0.044673], 'p_i': 20, 'u_i': 3.2251},
        {'id': 2, 'e_m': 3.289454, 'e_o_k': [2.349610, 1.409766, 0.845860], 'p_i': 40, 'u_i': 4.0273},
        {'id': 3, 'e_m': 7.449156, 'e_o_k': [5.320826, 3.192495, 1.915497], 'p_i': 80, 'u_i': 2.2476},
        {'id': 4, 'e_m': 2.409551, 'e_o_k': [1.550263, 0.930158, 0.558095, 0.334857], 'p_i': 80, 'u_i': 1.3199},
        {'id': 5, 'e_m': 0.229718, 'e_o_k': [0.134938, 0.080963, 0.048578, 0.029147, 0.017488, 0.010493], 'p_i': 10, 'u_i': 4.7520},
        {'id': 6, 'e_m': 0.659831, 'e_o_k': [0.400661, 0.240396, 0.144238, 0.086543, 0.051926], 'p_i': 20, 'u_i': 3.4892},
        {'id': 7, 'e_m': 1.081708, 'e_o_k': [0.946494, 0.567897], 'p_i': 20, 'u_i': 1.4050},
    ]
    B_BUDGET = 88.320016
    return processors, tasks, B_BUDGET
