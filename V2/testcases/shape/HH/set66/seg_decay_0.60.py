"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639997, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.639997, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.134282, 'e_o_k': [0.086395, 0.051837, 0.031102, 0.018661], 'p_i': 10, 'u_i': 3.0491},
        {'id': 1, 'e_m': 1.595105, 'e_o_k': [0.968575, 0.581145, 0.348687, 0.209212, 0.125527], 'p_i': 20, 'u_i': 3.9469},
        {'id': 2, 'e_m': 4.086998, 'e_o_k': [2.919284, 1.751570, 1.050942], 'p_i': 40, 'u_i': 1.2331},
        {'id': 3, 'e_m': 10.112241, 'e_o_k': [7.223029, 4.333817, 2.600290], 'p_i': 80, 'u_i': 3.8857},
        {'id': 4, 'e_m': 1.915959, 'e_o_k': [1.676465, 1.005879], 'p_i': 20, 'u_i': 4.4773},
        {'id': 5, 'e_m': 1.005364, 'e_o_k': [0.879694, 0.527816], 'p_i': 10, 'u_i': 2.4546},
        {'id': 6, 'e_m': 1.093498, 'e_o_k': [0.703538, 0.422123, 0.253274, 0.151964], 'p_i': 80, 'u_i': 1.1544},
        {'id': 7, 'e_m': 21.458838, 'e_o_k': [15.327741, 9.196645, 5.517987], 'p_i': 80, 'u_i': 4.0204},
    ]
    B_BUDGET = 176.639997
    return processors, tasks, B_BUDGET
