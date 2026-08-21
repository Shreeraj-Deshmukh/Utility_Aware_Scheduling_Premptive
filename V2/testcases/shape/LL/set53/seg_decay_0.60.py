"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200014, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.200014, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.159031, 'e_o_k': [0.049697, 0.029818], 'p_i': 10, 'u_i': 1.8047},
        {'id': 1, 'e_m': 1.218826, 'e_o_k': [0.380883, 0.228530], 'p_i': 20, 'u_i': 1.0945},
        {'id': 2, 'e_m': 0.995792, 'e_o_k': [0.215951, 0.129570, 0.077742, 0.046645, 0.027987], 'p_i': 40, 'u_i': 2.4137},
        {'id': 3, 'e_m': 5.369863, 'e_o_k': [1.678082, 1.006849], 'p_i': 80, 'u_i': 1.6729},
        {'id': 4, 'e_m': 0.918489, 'e_o_k': [0.192688, 0.115613, 0.069368, 0.041621, 0.024972, 0.014983], 'p_i': 40, 'u_i': 2.8481},
        {'id': 5, 'e_m': 0.851463, 'e_o_k': [0.195649, 0.117389, 0.070434, 0.042260], 'p_i': 10, 'u_i': 3.6691},
        {'id': 6, 'e_m': 1.430219, 'e_o_k': [0.328635, 0.197181, 0.118309, 0.070985], 'p_i': 20, 'u_i': 3.0767},
        {'id': 7, 'e_m': 4.121451, 'e_o_k': [0.864630, 0.518778, 0.311267, 0.186760, 0.112056, 0.067234], 'p_i': 80, 'u_i': 1.7471},
    ]
    B_BUDGET = 55.200014
    return processors, tasks, B_BUDGET
