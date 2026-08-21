"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639997, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639997, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.878081, 'e_o_k': [0.503817, 0.403054, 0.322443], 'p_i': 10, 'u_i': 1.3531},
        {'id': 1, 'e_m': 1.760389, 'e_o_k': [1.010059, 0.808047, 0.646438], 'p_i': 20, 'u_i': 2.6488},
        {'id': 2, 'e_m': 15.213605, 'e_o_k': [8.729118, 6.983294, 5.586635], 'p_i': 40, 'u_i': 4.8206},
        {'id': 3, 'e_m': 1.221415, 'e_o_k': [0.700812, 0.560650, 0.448520], 'p_i': 80, 'u_i': 3.3334},
        {'id': 4, 'e_m': 1.867670, 'e_o_k': [1.071614, 0.857291, 0.685833], 'p_i': 20, 'u_i': 2.1081},
        {'id': 5, 'e_m': 1.951144, 'e_o_k': [1.119509, 0.895607, 0.716486], 'p_i': 20, 'u_i': 1.8691},
        {'id': 6, 'e_m': 1.842208, 'e_o_k': [1.057004, 0.845604, 0.676483], 'p_i': 80, 'u_i': 3.0834},
        {'id': 7, 'e_m': 1.167704, 'e_o_k': [0.669994, 0.535995, 0.428796], 'p_i': 80, 'u_i': 3.6806},
    ]
    B_BUDGET = 176.639997
    return processors, tasks, B_BUDGET
