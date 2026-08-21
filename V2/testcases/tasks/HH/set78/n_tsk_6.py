"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640008, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640008, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.006173, 'e_o_k': [1.425692, 1.140553, 0.912443, 0.729954], 'p_i': 10, 'u_i': 1.9112},
        {'id': 1, 'e_m': 1.831089, 'e_o_k': [0.762591, 0.610073, 0.488058, 0.390446, 0.312357], 'p_i': 20, 'u_i': 4.0850},
        {'id': 2, 'e_m': 1.499507, 'e_o_k': [0.711148, 0.568919, 0.455135, 0.364108], 'p_i': 40, 'u_i': 1.7025},
        {'id': 3, 'e_m': 22.962509, 'e_o_k': [9.563158, 7.650527, 6.120421, 4.896337, 3.917070], 'p_i': 80, 'u_i': 2.0058},
        {'id': 4, 'e_m': 0.417577, 'e_o_k': [0.324782, 0.259826], 'p_i': 10, 'u_i': 3.5722},
        {'id': 5, 'e_m': 3.324123, 'e_o_k': [1.576481, 1.261185, 1.008948, 0.807158], 'p_i': 80, 'u_i': 1.2384},
    ]
    B_BUDGET = 176.640008
    return processors, tasks, B_BUDGET
