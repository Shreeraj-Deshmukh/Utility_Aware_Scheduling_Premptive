"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.072889, 'e_o_k': [0.446824, 0.357460, 0.285968, 0.228774, 0.183019], 'p_i': 10, 'u_i': 4.5978},
        {'id': 1, 'e_m': 3.167930, 'e_o_k': [1.817665, 1.454132, 1.163306], 'p_i': 20, 'u_i': 3.9895},
        {'id': 2, 'e_m': 1.605579, 'e_o_k': [1.248784, 0.999027], 'p_i': 40, 'u_i': 3.6989},
        {'id': 3, 'e_m': 3.927160, 'e_o_k': [1.862474, 1.489979, 1.191983, 0.953587], 'p_i': 80, 'u_i': 3.2467},
        {'id': 4, 'e_m': 1.165551, 'e_o_k': [0.668759, 0.535007, 0.428005], 'p_i': 80, 'u_i': 4.5958},
        {'id': 5, 'e_m': 1.220649, 'e_o_k': [0.578898, 0.463119, 0.370495, 0.296396], 'p_i': 40, 'u_i': 4.0042},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET
