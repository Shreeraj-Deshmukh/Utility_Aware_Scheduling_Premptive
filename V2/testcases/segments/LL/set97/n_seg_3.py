"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.350656, 'e_o_k': [0.071856, 0.057485, 0.045988], 'p_i': 10, 'u_i': 4.4298},
        {'id': 1, 'e_m': 3.430445, 'e_o_k': [0.702960, 0.562368, 0.449894], 'p_i': 20, 'u_i': 1.5050},
        {'id': 2, 'e_m': 0.207300, 'e_o_k': [0.042479, 0.033984, 0.027187], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 1.714842, 'e_o_k': [0.351402, 0.281122, 0.224897], 'p_i': 80, 'u_i': 2.5958},
        {'id': 4, 'e_m': 0.699429, 'e_o_k': [0.143326, 0.114660, 0.091728], 'p_i': 20, 'u_i': 1.3643},
        {'id': 5, 'e_m': 2.747339, 'e_o_k': [0.562979, 0.450383, 0.360307], 'p_i': 80, 'u_i': 4.2904},
        {'id': 6, 'e_m': 2.551296, 'e_o_k': [0.522807, 0.418245, 0.334596], 'p_i': 40, 'u_i': 4.4714},
        {'id': 7, 'e_m': 2.695881, 'e_o_k': [0.552435, 0.441948, 0.353558], 'p_i': 80, 'u_i': 4.7028},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
